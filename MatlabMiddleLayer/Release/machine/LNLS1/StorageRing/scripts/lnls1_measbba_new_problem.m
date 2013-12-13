function bba = lnls1_measbba(varargin)
%Faz medida BBA (Beam-Based alignment)
%
%Hist�ria: 
%
%2010-09-13: coment�rios iniciais no c�digo.


%% inicializa��es b�sicas
if ~strcmpi(getmode('BEND'), 'Online'), switch2online; end

for i=1:length(varargin)
    if ischar(varargin{i}) && strcmpi(varargin{i},'Archive')
        default_filename = varargin{i+1};
    end
end

%% Pede ao usu�rio, se for o caso, que defina onde os dados da medidas ser�o gravados
if ~exist('default_filename','var')
    default_dir      = fullfile(getfamilydata('Directory', 'DataRoot'), 'Optics', datestr(now, 'yyyy-mm-dd'));
    if ~exist(default_dir, 'dir')
        mkdir(default_dir); 
        dir_created = true;
    end
    default_filename = ['bba_' datestr(now, 'yyyy-mm-dd_HH-MM-SS') '.mat'];
    [FileName,PathName] = uiputfile('*.mat','Arquivo a ser salvo com medidas', fullfile(default_dir, default_filename));
    if FileName==0
        if exist('dir_created', 'var') && dir_created, rmdir(default_dir); end
        return; 
    end
    default_filename = fullfile(PathName, FileName);
end

%% configura��es iniciais
if exist(default_filename, 'file')
    load(default_filename); 
else   
    bba = load_default_bba_config;
    bba.default_filename = default_filename;
    bba.configs.shunts.pause         = 1;
    bba.configs.shunts.nr_cycles     = 3;
    bba.configs.correctors.pause     = 2; 
    bba.configs.bpms.pause           = 0.5;
    bba.configs.bpms.nr_measurements = 5;
end

%% medida BBA
if ~isfield(bba, 'final_machineconfig')
    
    % ajustes iniciais
    setbpmaverages(bba.configs.bpms.pause, bba.configs.bpms.nr_measurements);
    fprintf('%s: desligando corre��o de �rbita autom�tica\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
    lnls1_auto_orb_corr_off;
    fprintf('%s: ligando shunts\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
    lnls1_quad_shunts_on;
    fprintf('%s: abrindo dispositivos de inser��o\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
    init_IDS = lnls1_set_id_configurations({'AON11GAP', 'AWG01GAP'});
    IDS(1) = struct('channel_name', 'AON11GAP', 'value', 300, 'tolerance', 0.5);
    IDS(2) = struct('channel_name', 'AWG01GAP', 'value', 180, 'tolerance', 0.5);
    lnls1_set_id_configurations(IDS);
    
    % mede bba
    bba.initial_time_stamp    = datestr(now, 'yyyy-mm-dd_HH-MM-SS');
    fprintf('%s: IN�CIO DE MEDIDAS BBA\n', bba.initial_time_stamp);
    bba.initial_machineconfig = getmachineconfig;
    %if isfield(bba, 'bpm_x'), bba.bpm_x = do_bba('HCM', bba.bpm_x, bba.configs); end
    %if isfield(bba, 'bpm_y'), bba.bpm_y = do_bba('VCM', bba.bpm_y, bba.configs); end
    if isfield(bba, 'bpm_x'), bba = do_bba('HCM', bba); end
    if isfield(bba, 'bpm_y'), bba = do_bba('VCM', bba); end
    bba.final_time_stamp = datestr(now, 'yyyy-mm-dd_HH-MM-SS');
    bba.final_machineconfig = getmachineconfig;
    fprintf('%s: FIM DE MEDIDAS BBA\n', bba.initial_time_stamp);
    
    % volta IDs aa config original
    fprintf('%s: voltando dispositivos de inser��o � configura��o original\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
    lnls1_set_id_configurations(init_IDS);

end

bba = faz_analise(bba);
bba = salva_dados(bba);

%% remove diret�rio se vazio
pathstr = fileparts(bba.default_filename);
files = dir(pathstr);
if (length(files)<3) 
    rmdir(PathName); 
end

function bba = faz_analise(bba0)

bba = bba0;

%% faz an�lise das medidas
fprintf('\n%s: [AN�LISE BBA HORIZONTAL]\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
if isfield(bba, 'bpm_x'), bba.bpm_x = analysis_bba('BPMx', bba.bpm_x); end
fprintf('\n%s: [AN�LISE BBA VERTICAL]\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
if isfield(bba, 'bpm_y'), bba.bpm_y = analysis_bba('BPMy', bba.bpm_y); end

function bba = salva_dados(bba0)

bba = bba0;

%% salva dados
fprintf('\n%s: salvando dados\n', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
pathstr = fileparts(bba.default_filename);
if ~exist(pathstr, 'dir')
    mkdir(pathstr); 
end
save(bba.default_filename, 'bba');

%% registra experimento no hist�rico
registra_historico(bba);

function bba = load_default_bba_config

% --- monitores horizontais ---
n=0;



%% AMP01B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP01B';
bba.bpm_x{n}.shunt                = 'AQF01B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH07B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.078, +0.122, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.122,+0.058,7);
bba.bpm_x{n}.power_supply_off     = {};


%% AMP02A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP02A';
bba.bpm_x{n}.shunt                = 'AQF02A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH09B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(+0.015, +0.215, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.303,+0.050,7) ;
bba.bpm_x{n}.power_supply_off     = {};


%% AMP02B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP02B';
bba.bpm_x{n}.shunt                = 'AQF02B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH07A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.265, -0.065, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(+0.005,+0.393,7);
bba.bpm_x{n}.power_supply_off     = {};


%% AMP03A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP03A';
bba.bpm_x{n}.shunt                = 'AQF03A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH09A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.117, +0.083, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.077,+0.091,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP03B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP03B';
bba.bpm_x{n}.shunt                = 'AQF03B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH09B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.109, +0.091, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.087,+0.083,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP03C
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP03C';
bba.bpm_x{n}.shunt                = 'AQF03B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH09B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.044, +0.156, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.219,+0.219,7);
bba.bpm_x{n}.power_supply_off     = {};



%% AMP04A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP04A';
bba.bpm_x{n}.shunt                = 'AQF04A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH11B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.292, -0.092, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.048,+0.339,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP04B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP04B';
bba.bpm_x{n}.shunt                = 'AQF04B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH09A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(+0.108, +0.308, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.310,+0.047,7);
bba.bpm_x{n}.power_supply_off     = {};



%% AMP05A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP05A';
bba.bpm_x{n}.shunt                = 'AQF05A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH11A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.075, +0.125, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.109,+0.079,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP05B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP05B';
bba.bpm_x{n}.shunt                = 'AQF05B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH11B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.104, +0.096, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.085,+0.099,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP06A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP06A';
bba.bpm_x{n}.shunt                = 'AQF06A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH01A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.057, +0.143, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.193,+0.183,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP06B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP06B';
bba.bpm_x{n}.shunt                = 'AQF06B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH11A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.138, +0.062, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.135,+0.258,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP07A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP07A';
bba.bpm_x{n}.shunt                = 'AQF07A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH01A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.101, +0.099, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.069,+0.105,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP07B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP07B';
bba.bpm_x{n}.shunt                = 'AQF07B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH01B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.068, +0.132, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.095,+0.080,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP08A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP08A';
bba.bpm_x{n}.shunt                = 'AQF08A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH03B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.107, +0.093, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.156,+0.201,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP08B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP08B';
bba.bpm_x{n}.shunt                = 'AQF08B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH01A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.109, +0.091, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.149,+0.217,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP09A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP09A';
bba.bpm_x{n}.shunt                = 'AQF09A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH03A';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.102, +0.098, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.085,+0.091,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP09B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP09B';
bba.bpm_x{n}.shunt                = 'AQF09B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH03B';
%bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.111, +0.089, 5);
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.073,+0.099,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP10A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP10A';
bba.bpm_x{n}.shunt                = 'AQF10A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH05B';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.225,+0.187,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP10B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP10B';
bba.bpm_x{n}.shunt                = 'AQF10B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH03A';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.134,+0.241,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMU11A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMU11A';
bba.bpm_x{n}.shunt                = 'AQF11A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH05A';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.116,+0.078,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMU11B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMU11B';
bba.bpm_x{n}.shunt                = 'AQF11B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH05B';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.125,+0.064,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP12A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP12A';
bba.bpm_x{n}.shunt                = 'AQF12A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH07B';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.203,+0.182,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP12B
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP12B';
bba.bpm_x{n}.shunt                = 'AQF12B';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH05A';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.178,+0.238,7);
bba.bpm_x{n}.power_supply_off     = {};
%% AMP01A
n=n+1;
bba.bpm_x{n}.bpm                  = 'AMP01A';
bba.bpm_x{n}.shunt                = 'AQF01A';
bba.bpm_x{n}.shunt_delta_amp      = 1.0;
bba.bpm_x{n}.corrector            = 'ACH07A';
bba.bpm_x{n}.corrector_grid_mrad  = linspace(-0.073,+0.109,7);
bba.bpm_x{n}.power_supply_off     = {};


%% --- monitores verticais ---
n=0;


%% AMP01B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP01B';
bba.bpm_y{n}.shunt                = 'AQF01B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.095, +0.105, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.091,+0.067,7);
bba.bpm_y{n}.power_supply_off     = {};
%% AMP02A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP02A';
bba.bpm_y{n}.shunt                = 'AQF02A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.109, +0.091, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.116,+0.116,7);
bba.bpm_y{n}.power_supply_off     = {};
%% AMP02B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP02B';
bba.bpm_y{n}.shunt                = 'AQF02B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV09B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.119, +0.081, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.135,+0.119,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP03A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP03A';
bba.bpm_y{n}.shunt                = 'AQF03A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV09A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.097, +0.103, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.083,+0.095,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP03B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP03B';
bba.bpm_y{n}.shunt                = 'AQF03B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV09B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.106, +0.094, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.098,+0.109,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP03C
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP03C';
bba.bpm_y{n}.shunt                = 'AQF03B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV01A';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.044,+0.054,7); 
bba.bpm_y{n}.power_supply_off     = {};


%% AMP04A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP04A';
bba.bpm_y{n}.shunt                = 'AQF04A';
bba.bpm_y{n}.shunt_delta_amp      = 3.0;
bba.bpm_y{n}.corrector            = 'ACV03B';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.230,+0.134,7);
bba.bpm_y{n}.power_supply_off     = {};



%% AMP04B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP04B';
bba.bpm_y{n}.shunt                = 'AQF04B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.127,+0.111,7); 
bba.bpm_y{n}.power_supply_off     = {};


%% AMP05A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP05A';
bba.bpm_y{n}.shunt                = 'AQF05A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.087,+0.073,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP05B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP05B';
bba.bpm_y{n}.shunt                = 'AQF05B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11B';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.077,+0.091,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP06A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP06A';
bba.bpm_y{n}.shunt                = 'AQF06A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.144,+0.084,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP06B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP06B';
bba.bpm_y{n}.shunt                = 'AQF06B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07A';
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.107,+0.107,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP07A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP07A';
bba.bpm_y{n}.shunt                = 'AQF07A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV09B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.102, +0.098, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.079,+0.081,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP07B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP07B';
bba.bpm_y{n}.shunt                = 'AQF07B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV01B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.100, +0.100, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.080,+0.072,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP08A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP08A';
bba.bpm_y{n}.shunt                = 'AQF08A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.166, +0.034, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.126,+0.086,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP08B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP08B';
bba.bpm_y{n}.shunt                = 'AQF08B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV03B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.091, +0.109, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.210,+0.166,7);
bba.bpm_y{n}.power_supply_off     = {};
%% AMP09A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP09A';
bba.bpm_y{n}.shunt                = 'AQF09A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.082, +0.118, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.039,+0.141,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP09B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP09B';
bba.bpm_y{n}.shunt                = 'AQF09B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.162, +0.038, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.044,+0.114,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP10A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP10A';
bba.bpm_y{n}.shunt                = 'AQF10A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV09B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.127, +0.073, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.134,+0.111,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP10B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP10B';
bba.bpm_y{n}.shunt                = 'AQF10B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.087, +0.113, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.141,+0.088,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMU11A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMU11A';
bba.bpm_y{n}.shunt                = 'AQF11A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.100, +0.100, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.122,+0.084,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMU11B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMU11B';
bba.bpm_y{n}.shunt                = 'AQF11B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.109, +0.091, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.084,+0.146,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP12A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP12A';
bba.bpm_y{n}.shunt                = 'AQF12A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV11B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.095, +0.105, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.108,+0.131,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP12B
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP12B';
bba.bpm_y{n}.shunt                = 'AQF12B';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07B';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.077, +0.123, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.103,+0.118,7); 
bba.bpm_y{n}.power_supply_off     = {};
%% AMP01A
n=n+1;
bba.bpm_y{n}.bpm                  = 'AMP01A';
bba.bpm_y{n}.shunt                = 'AQF01A';
bba.bpm_y{n}.shunt_delta_amp      = 1.0;
bba.bpm_y{n}.corrector            = 'ACV07A';
%bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.078, +0.122, 5);
bba.bpm_y{n}.corrector_grid_mrad  = linspace(-0.060,+0.103,7); 
bba.bpm_y{n}.power_supply_off     = {};

function new_bba = do_bba(corrector_family, original_bba)

configs = original_bba.configs;
new_bba = original_bba;

% seleciona HORIZ ou VERT
if strcmpi(corrector_family, 'HCM')
    bba_data = original_bba.bpm_x;
else
    bba_data = original_bba.bpm_y;
end;
    
for i=1:length(bba_data)
   
    % prepara dados
    
    bba = bba_data{i};
    shunt_device = common2dev(bba.shunt, 'QUADSHUNT');
    corrector_device = common2dev(bba.corrector, corrector_family);
    initial_values_power_supply_off = zeros(1,length(bba.power_supply_off));
    for j=1:length(bba.power_supply_off)
        initial_values_power_supply_off(j) = getpv(bba.power_supply_off{j}, 'Setpoint');
    end
    initial_value_corrector = getpv(corrector_family, 'Setpoint', corrector_device, 'Physics');    
    bba.dcct = getdcct;
    
    fprintf('\n');
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': [%s]\n'], bba.bpm);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': shunt %s\n'], bba.shunt);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corretora %s\n'], bba.corrector);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % cicla shunt
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': ciclando shunt\n']);
    for j=1:configs.shunts.nr_cycles
        init_shunt = getpv('QUADSHUNT', 'Monitor', shunt_device);
        steppv('QUADSHUNT','Setpoint', bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        final_shunt = getpv('QUADSHUNT', 'Monitor', shunt_device);
        if (abs(final_shunt - init_shunt - bba.shunt_delta_amp) > 0.1)
            bba.obs = 'problema durante ciclagem de shunt'; 
            fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': %s\n'], bba.obs); 
        end;
        steppv('QUADSHUNT','Setpoint', -bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % zera fontes entre quadrupolo e bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': zerando poss�veis fontes entre bpm e quadrupolo\n']);
    for j=1:length(bba.power_supply_off)
        setpv(bba.power_supply_off{j}, 0);
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % varre posi��o do feixe no bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': varrendo corretora (�rbita) [mrad]: ']);
    for j=1:length(bba.corrector_grid_mrad)
        
        fprintf('%+6.3f ', bba.corrector_grid_mrad(j));
        
        % ajusta corretora
        setpv(corrector_family, initial_value_corrector + bba.corrector_grid_mrad(j)/1000, corrector_device, 'Physics');
        pause(configs.correctors.pause);
        
        % registra �rbita original
        bba.orbit0{j} = [getx gety];
        
        % varia shunt
        steppv('QUADSHUNT','Setpoint', bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        
        % registra �rbita final
        bba.orbit1{j} = [getx gety];
        
        % restaura shunt
        steppv('QUADSHUNT','Setpoint', -bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        
    end
    fprintf('\n');
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % restaura valor original da corretora
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': restaurando valor original da corretora\n']);
    setpv(corrector_family, initial_value_corrector, corrector_device, 'Physics');
    pause(configs.correctors.pause);
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % restaura fontes entre quadrupolo e bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': restaurando fontes entre bpm e quadrupolo\n']);
    for j=1:length(bba.power_supply_off)
        setpv(bba.power_supply_off{j}, initial_values_power_supply_off{j});
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    bba_data{i} = bba;
   
    
    % seleciona HORIZ ou VERT
    if strcmpi(corrector_family, 'HCM')
        new_bba.bpm_x = bba_data;
    else
        new_bba.bpm_y = bba_data;
    end;
    
    % faz analise
    new_bba = faz_analise(new_bba);
    
    % salva dados
    new_bba = salva_dados(new_bba);

    
end



bba_data = original_bba_data;

for i=1:length(bba_data)
   
    % prepara dados
    bba = bba_data{i};
    shunt_device = common2dev(bba.shunt, 'QUADSHUNT');
    corrector_device = common2dev(bba.corrector, corrector_family);
    initial_values_power_supply_off = zeros(1,length(bba.power_supply_off));
    for j=1:length(bba.power_supply_off)
        initial_values_power_supply_off(j) = getpv(bba.power_supply_off{j}, 'Setpoint');
    end
    initial_value_corrector = getpv(corrector_family, 'Setpoint', corrector_device, 'Physics');    
    bba.dcct = getdcct;
    
    fprintf('\n');
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': [%s]\n'], bba.bpm);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': shunt %s\n'], bba.shunt);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corretora %s\n'], bba.corrector);
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % cicla shunt
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': ciclando shunt\n']);
    for j=1:configs.shunts.nr_cycles
        init_shunt = getpv('QUADSHUNT', 'Monitor', shunt_device);
        steppv('QUADSHUNT','Setpoint', bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        final_shunt = getpv('QUADSHUNT', 'Monitor', shunt_device);
        if (abs(final_shunt - init_shunt - bba.shunt_delta_amp) > 0.1)
            bba.obs = 'problema durante ciclagem de shunt'; 
            fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': %s\n'], bba.obs); 
        end;
        steppv('QUADSHUNT','Setpoint', -bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % zera fontes entre quadrupolo e bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': zerando poss�veis fontes entre bpm e quadrupolo\n']);
    for j=1:length(bba.power_supply_off)
        setpv(bba.power_supply_off{j}, 0);
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % varre posi��o do feixe no bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': varrendo corretora (�rbita) [mrad]: ']);
    for j=1:length(bba.corrector_grid_mrad)
        
        fprintf('%+6.3f ', bba.corrector_grid_mrad(j));
        
        % ajusta corretora
        setpv(corrector_family, initial_value_corrector + bba.corrector_grid_mrad(j)/1000, corrector_device, 'Physics');
        pause(configs.correctors.pause);
        
        % registra �rbita original
        bba.orbit0{j} = [getx gety];
        
        % varia shunt
        steppv('QUADSHUNT','Setpoint', bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        
        % registra �rbita final
        bba.orbit1{j} = [getx gety];
        
        % restaura shunt
        steppv('QUADSHUNT','Setpoint', -bba.shunt_delta_amp, shunt_device);
        pause(configs.shunts.pause);
        
    end
    fprintf('\n');
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % restaura valor original da corretora
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': restaurando valor original da corretora\n']);
    setpv(corrector_family, initial_value_corrector, corrector_device, 'Physics');
    pause(configs.correctors.pause);
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    % restaura fontes entre quadrupolo e bpm
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': restaurando fontes entre bpm e quadrupolo\n']);
    for j=1:length(bba.power_supply_off)
        setpv(bba.power_supply_off{j}, initial_values_power_supply_off{j});
    end
    bba.dcct = [bba.dcct getdcct];
    fprintf([datestr(now, 'yyyy-mm-dd_HH-MM-SS') ': corrente = %f mA\n'], bba.dcct(end));
    
    bba_data{i} = bba;
   
    
end

function bba = analysis_bba(family_name, original_bba)

bba = original_bba;

if strcmpi(family_name, 'BPMx'), direction = 1; else direction = 2; end;

for i=1:length(bba)
    bpm = bba{i};
    
    if ~isfield(bpm, 'orbit1'), continue; end; 
     
    bpm_element = dev2elem(family_name, common2dev(bpm.bpm, family_name));
    rms = zeros(1,length(bpm.orbit1));
    pos_bpm = zeros(1,length(bpm.orbit1));
    
    for j=1:length(bpm.orbit1)
        cod    = bpm.orbit1{j} - bpm.orbit0{j};
        rms(j) = sum(cod(:,direction).^2)/length(cod(:,direction));
        pos_bpm(j)  = bpm.orbit0{j}(bpm_element, direction);
    end
    
    pc =  polyfit(pos_bpm, rms, 2);
    b  =  pc(1);
    x0 = -pc(2)/(2*b);
    a  =  pc(3) - b*x0^2;
    
    bpm.offset  = x0;
    if (bpm.offset > max(pos_bpm)) || (bpm.offset < min(pos_bpm)), bpm.extrapolation = true; else bpm.extrapolation = false; end;
    
    rms1    = a;
    rms2    = b*(pos_bpm - x0).^2;
    rms_fit = rms1 + rms2;
    
    s1 = sum((rms_fit - rms).^2);
    s2 = sum((rms - mean(rms)).^2);
    bpm.coeff_determination = 1 - s1/s2;
    if (rms1 > 50*10^-6), bpm.coeff_determination = -1; end
    if (max(abs(rms2)) < 1*10^-6), bpm.coeff_determination = -2; end
        
    if (bpm.coeff_determination < 0.99), plot_bba(bpm, direction, pos_bpm, rms); end;
    
    bpm.pos_bpm = pos_bpm;
    bpm.rms = rms;
    
    % recalcula janela de kick centrada no offset e que gere desvios de
    % �rbita de +/- 1 mm
    delta = sort(interp1(pos_bpm, bpm.corrector_grid_mrad, bpm.offset + [-1 +1], 'spline', 'extrap'));
    bpm.new_corrector_grid_mrad = linspace(delta(1), delta(2), length(bpm.corrector_grid_mrad));
    
    % mostra resultado na an�lise:
    fprintf('[%s_%s] offset:%+5.0f um (%4.2f), novo_intervalo: [%+6.3f,%+6.3f] mrad, extrapola��o:%i\n', family_name, bpm.bpm, 1000*bpm.offset, bpm.coeff_determination, delta(1), delta(2), bpm.extrapolation);
    % insere dados de an�lise na estrutura
    bba{i} = bpm;
end

function plot_bba(bpm, direction, pos_bpm, rms)

if direction==1, bpm_label = [bpm.bpm '-H']; else bpm_label = [bpm.bpm '-V']; end;
figure('Name', bpm_label);
scatter(1e3*pos_bpm, 1e6*rms, 'filled');
xlabel('Posi��o [\mum]'); 
ylabel('RMS da distor��o de �rbita [\mum^2]');
hold all;
pc = polyfit(pos_bpm,rms,2);
x = linspace(pos_bpm(1), pos_bpm(end), 30);
y = pc(1) * x.^2 + pc(2) * x + pc(3);
plot(1e3*x,1e6*y);
title(['BBA do ' bpm_label ' (' num2str(bpm.coeff_determination) ')']);

function registra_historico(bba)

def_bpm_names = [ ...
    'AMP01B'; ...
    'AMP02A'; 'AMP02B'; 'AMP03A'; 'AMP03B'; 'AMP03C'; 'AMP04A'; 'AMP04B'; ...
    'AMP05A'; 'AMP05B'; 'AMP06A'; 'AMP06B'; 'AMP07A'; 'AMP07B'; ...
    'AMP08A'; 'AMP08B'; 'AMP09A'; 'AMP09B'; 'AMP10A'; 'AMP10B'; ...
    'AMU11A'; 'AMU11B'; 'AMP12A'; 'AMP12B'; 'AMP01A' ];

bba_data_file = 'C:\Arq\MatlabMiddleLayer\Release\machine\LNLS1\StorageRingData\User\Optics\bba_data.mat';
bba_data = [];
if exist(bba_data_file, 'file'), load(bba_data_file); end;
data.time_stamp = bba.initial_time_stamp;
data.offsets = NaN * ones(size(def_bpm_names,1),2);

if isfield(bba, 'bpm_x')
for i=1:length(bba.bpm_x)
    for j=1:size(def_bpm_names)
        if strcmpi(def_bpm_names(j,:),bba.bpm_x{i}.bpm)
            try
                data.offsets(j,1) = bba.bpm_x{i}.offset;
            catch
            end;
        end
    end
end
end

if isfield(bba, 'bpm_y')
for i=1:length(bba.bpm_y)
    for j=1:size(def_bpm_names)
        if strcmpi(def_bpm_names(j,:),bba.bpm_y{i}.bpm)
            try
                data.offsets(j,2) = bba.bpm_y{i}.offset;
            catch
            end
        end
    end
end
end

if ~isempty(bba_data)
    is_match = false;
    for i=1:length(bba_data)
        is_match = is_match || strcmpi(data.time_stamp, bba_data(i).time_stamp);
        if is_match, break; end
    end
    if is_match,
        bba_data(i) = data;
    else
        bba_data(end+1) = data;
    end
else
    bba_data = data; 
end

save(bba_data_file, 'bba_data');
assignin('base', 'bba_data', bba_data);

bba_data_file = strrep(bba_data_file, '.mat', '.txt');

fp = fopen(bba_data_file, 'w');
fprintf(fp, 'DATA\tHORA\t');
pvs = family2common('BPMx');
for i=1:size(pvs,1);
    fprintf(fp, '%sH\t', pvs(i,:));
end
for i=1:size(pvs,1);
    fprintf(fp, '%sV\t', pvs(i,:));
end
fprintf(fp, '\r\n');


for j=1:length(bba_data)
    data = bba_data(j);
    dn = datenum(data.time_stamp, 'yyyy-mm-dd_HH-MM-SS');
    ts = datestr(dn, 'dd/mm/yyyy HH:MM:SS');
    fprintf(fp, '%s\t', ts);
    for i=1:size(data.offsets,1)
        fprintf(fp, '%f\t', data.offsets(i,1));
    end
    for i=1:size(data.offsets,1)
        fprintf(fp, '%f\t', data.offsets(i,2));
    end
    fprintf(fp, '\r\n');
end
fclose(fp);