function machine = lnls_latt_err_apply_errors(name, machine, errors, increment)
%
%  Apply the errors generated by generate_errors to the ring model.
%
%  INPUTS:
%    name     : name of the file to save input parameters
%    machine  : might be a model of the ring or a cell array of models of
%               the ring;
%    errors   : structure of errors to be applied (for more details see
%               generate_errors help;
%    increment: float defining the fraction of the errors which will be
%               additively applied to the machines.
%
%  OUTPUT:
%    machine  : cell array of ring models with errors.
%
%  modified 2015/03/05 by Fernando.
%
% SEE ALSO: lnls_latt_err_apply_errors, lnls_latt_err_correct_cod, 
% lnls_latt_err_correct_coupling, lnls_latt_err_correct_optics,
% lnls_latt_err_correct_tune_machines

nr_machines = size(errors.errors_x, 1);

save([name,'_apply_errors_input.mat'], 'errors', 'increment');

if ~iscell(machine{1})
    machine = repmat({machine},nr_machines,1);
end

if length(machine) ~= nr_machines
    warning('MATLAB:DifferentSizes',...
        'Incompatibility between errors and machine lengths.\n Using minimum of both.');
    nr_machines = min([length(machine),nr_machines]);
end

dim = get_dim(machine{1});
family_data = sirius_si_family_data(machine{1});
bpm = family_data.bpm.ATIndex;

sext_idx = findcells(machine{1}, 'PolynomB');
fprintf('    --------------------------------------------------------------- \n');
fprintf('   |           codx [mm]           |           cody [mm]           |\n');
fprintf('   |      all             bpm      |      all             bpm      |\n');
fprintf('   | (max)   (rms) | (max)   (rms) | (max)   (rms) | (max)   (rms) |\n');
fprintf('---|---------------------------------------------------------------|\n');
%fprintf('001| 13.41   14.32 | 13.41   14.32 | 13.41   14.32 | 13.41   14.32 |\n');
for i=1:nr_machines
    machine{i}    = apply_errors_one_machine(machine{i}, errors, i, increment);
    the_ring = setcellstruct(machine{i}, 'PolynomB', sext_idx, 0, 1, 3);
    [codx, cody] = calc_cod(the_ring, dim);
    [x_max_all,x_rms_all] = get_max_rms(codx,1e3);
    [x_max_bpm,x_rms_bpm] = get_max_rms(codx(bpm),1e3);
    [y_max_all,y_rms_all] = get_max_rms(cody,1e3);
    [y_max_bpm,y_rms_bpm] = get_max_rms(cody(bpm),1e3);
    fprintf('%03i| %5.2f   %5.2f | %5.2f   %5.2f | %5.2f   %5.2f | %5.2f   %5.2f |\n',i,x_max_all,x_rms_all,x_max_bpm,x_rms_bpm,y_max_all,y_rms_all,y_max_bpm,y_rms_bpm);
end
fprintf('------------------------------------------------------------------- \n');


function the_ring = apply_errors_one_machine(the_ring0, errors, machine, fraction)

the_ring  = the_ring0;

err = fraction * errors.errors_x(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_misalignmentX(err(idx), idx, the_ring);

err = fraction * errors.errors_y(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_misalignmentY(err(idx), idx, the_ring);

err = fraction * errors.errors_roll(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_rotation_ROLL(err(idx), idx, the_ring);

err = fraction * errors.errors_yaw(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_rotation_YAW(err(idx), idx, the_ring);

err = fraction * errors.errors_pitch(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_rotation_PITCH(err(idx), idx, the_ring);

err = fraction * errors.errors_e(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_excitation(err(idx), idx, the_ring);

err = fraction * errors.errors_e_kdip(machine,:);
idx = find(err ~= 0)';
the_ring  = lnls_set_excitation_Kdip(err(idx), idx, the_ring);



function [maxv,rmsv] = get_max_rms(v,f)
    maxv = f*max(abs(v));
    rmsv = f*sqrt(sum(v.^2)/length(v));