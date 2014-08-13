# -*- coding: utf-8 -*-

from parameter import Parameter
from definitions import ParameterDefinitions as Prms


label = 'Storage ring'


parameter_list = [

  Parameter(
    name     = 'Storage ring beam energy',
    group    = 'LNLS',
    value    = Prms.sr_beam_energy,
    symbol   = r'<math>E</math>',
    units    = 'GeV',
    revision = '2014-08-04',
    deps     = [],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring beam gamma factor',
    group    = 'FAC',
    value    = Prms.sr_beam_gamma_factor,
    symbol   = r'<math>\gamma</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring beam energy'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring beam beta factor',
    group    = 'FAC',
    value    = Prms.sr_beam_beta_factor,
    symbol   = r'<math>\beta</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring beam velocity',
    group    = 'FAC',
    value    = Prms.sr_beam_velocity,
    symbol   = r'<math>v</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring beam beta factor'],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring beam magnetic rigidity',
    group    = 'FAC',
    value    = Prms.sr_beam_magnetic_rigidity,
    symbol   = r'<math>(B\rho)</math>',
    units    = 'T.m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam energy'],
    obs      = [r'<math>(B\rho) = \frac{p}{ec} = \frac{E}{ec^2}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring beam current',
    group    = 'FAC',
    value    = Prms.sr_beam_current,
    symbol   = r'<math>I</math>',
    units    = 'mA',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring lattice version',
    group    = 'FAC',
    value    = Prms.sr_lattice_version,
    symbol   = '',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring lattice circumference',
    group    = 'LNLS',
    value    = Prms.sr_lattice_circumference,
    symbol   = r'<math>C</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring lattice symmetry',
    group    = 'FAC',
    value    = Prms.sr_lattice_symmetry,
    symbol   = r'<math>N_\text{SUPERCELLS}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring number of long straight sections',
    group    = 'FAC',
    value    = Prms.sr_number_of_long_straight_sections ,
    symbol   = r'<math>N_\text{lss}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring number of short straight sections',
    group    = 'FAC',
    value    = Prms.sr_number_of_short_straight_sections ,
    symbol   = r'<math>N_\text{sss}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring length of long straight sections',
    group    = 'FAC',
    value    = Prms.sr_length_of_long_straight_sections,
    symbol   = r'<math>L_\text{lss}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring length of short straight sections',
    group    = 'FAC',
    value    = Prms.sr_length_of_short_straight_sections,
    symbol   = r'<math>L_\text{sss}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring harmonic number',
    group    = 'FAC',
    value    = Prms.sr_harmonic_number,
    symbol   = r'<math>h</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring RF cavity peak voltage',
    group    = 'FAC',
    value    = Prms.sr_rf_cavity_peak_voltage,
    symbol   = r'<math>V_\text{RF}</math>',
    units    = 'MV',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
  
  Parameter(
    name     = 'Storage ring revolution period',
    group    = 'FAC',
    value    = Prms.sr_revolution_period,
    symbol   = r'<math>T_\text{rev}</math>',
    units    = unicode('μs',encoding='utf-8'),
    revision = '2014-08-01',
    deps     = ['Storage ring lattice circumference',
                'Storage ring beam velocity'],
    obs      = [],
  ),
 
  Parameter(
    name     = 'Storage ring revolution frequency',
    group    = 'FAC',
    value    = Prms.sr_revolution_frequency,
    symbol   = r'<math>f_\text{rev}</math>',
    units    = u'MHz',
    revision = '2014-08-01',
    deps     = ['Storage ring revolution period'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring RF frequency',
    group    = 'FAC',
    value    = Prms.sr_rf_frequency,
    symbol   = r'<math>f_\text{RF}</math>',
    units    = u'MHz',
    revision = '2014-08-01',
    deps     = ['Storage ring revolution frequency',
                'Storage ring harmonic number'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring number of electrons',
    group    = 'FAC',
    value    = Prms.sr_number_of_electrons,
    symbol   = r'<math>N</math>',
    units    = u'',
    revision = '2014-08-01',
    deps     = ['Storage ring beam current',
                'Storage ring revolution period'],
    obs      = [],
  ),
 
  Parameter(
    name     = 'Storage ring number of B1 dipoles',
    group    = 'FAC',
    value    = Prms.sr_number_of_B1_dipoles,
    symbol   = r'<math>N_\text{B1}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
            
  Parameter(
    name     = 'Storage ring number of B2 dipoles',
    group    = 'FAC',
    value    = Prms.sr_number_of_B2_dipoles,
    symbol   = r'<math>N_\text{B2}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring number of B3 dipoles',
    group    = 'FAC',
    value    = Prms.sr_number_of_B3_dipoles,
    symbol   = r'<math>N_\text{B3}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
         
  Parameter(
    name     = 'Storage ring number of BC dipoles',
    group    = 'FAC',
    value    = Prms.sr_number_of_BC_dipoles,
    symbol   = r'<math>N_\text{BC}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                           
  Parameter(
    name     = 'Storage ring hardedge length of B1 dipoles',
    group    = 'FAC',
    value    = Prms.sr_hardedge_length_of_B1_dipoles,
    symbol   = r'<math>L_\text{B1}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                
  Parameter(
    name     = 'Storage ring hardedge length of B2 dipoles',
    group    = 'FAC',
    value    = Prms.sr_hardedge_length_of_B2_dipoles,
    symbol   = r'<math>L_\text{B2}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring hardedge length of B3 dipoles',
    group    = 'FAC',
    value    = Prms.sr_hardedge_length_of_B3_dipoles,
    symbol   = r'<math>L_\text{B3}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring hardedge length of BC dipoles',
    group    = 'FAC',
    value    = Prms.sr_hardedge_length_of_BC_dipoles,
    symbol   = r'<math>L_\text{BC}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring dipole low magnetic field',
    group    = 'FAC',
    value    = Prms.sr_dipole_low_magnetic_field,
    symbol   = r'<math>B_\text{low}</math>',
    units    = 'T',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                
  Parameter(
    name     = 'Storage ring dipole high magnetic field',
    group    = 'FAC',
    value    = Prms.sr_dipole_high_magnetic_field,
    symbol   = r'<math>B_\text{high}</math>',
    units    = 'T',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring dipole low magnetic field bending radius',
    group    = 'FAC',
    value    = Prms.sr_dipole_low_magnetic_field_bending_radius,
    symbol   = r'<math>\rho_\text{low}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring dipole low magnetic field'],
    obs      = [r'<math>\rho_\text{low} = \frac{ec/p}{B_\text{low}} = \frac{(B\rho)}{B_\text{low}}</math>'],
  ),
                
  Parameter(
    name     = 'Storage ring dipole high magnetic field bending radius',
    group    = 'FAC',
    value    = Prms.sr_dipole_high_magnetic_field_bending_radius,
    symbol   = r'<math>\rho_\text{high}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring dipole high magnetic field'],
    obs      = [r'<math>\rho_\text{high} = \frac{ec/p}{B_\text{high}} = \frac{(B\rho)}{B_\text{high}}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring dipole low magnetic field critical energy',
    group    = 'FAC',
    value    = Prms.sr_dipole_low_magnetic_field_critical_energy,
    symbol   = r'<math>\epsilon_\text{c,low}</math>',
    units    = 'keV',
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring dipole low magnetic field bending radius'],
    obs      = [r'<math>\epsilon_\text{c,low} = \frac{3}{2} \hbar c \frac{\gamma^3}{\rho_\text{low}}</math>'],
  ),
                
  Parameter(
    name     = 'Storage ring dipole high magnetic field critical energy',
    group    = 'FAC',
    value    = Prms.sr_dipole_high_magnetic_field_critical_energy,
    symbol   = r'<math>\epsilon_\text{c,high}</math>',
    units    = 'keV',
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring dipole high magnetic field bending radius'],
    obs      = [r'<math>\epsilon_\text{c,high} = \frac{3}{2} \hbar c \frac{\gamma^3}{\rho_\text{high}}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I1 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I1_from_dipoles,
    symbol   = r'<math>I_\text{1,DIP}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version','Storage ring optics mode'],
    obs      = [r'<math>I_\text{1,DIP} = \oint{\frac{\eta_x}{\rho_x}\,ds}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I2 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I2_from_dipoles,
    symbol   = r'<math>I_\text{2,DIP}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{2,DIP} = \oint{\frac{1}{\rho_x^2}\,ds}</math>'],
  ),
   
  Parameter(
    name     = 'Storage ring radiation integral I3 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I3_from_dipoles,
    symbol   = r'<math>I_\text{3,DIP}</math>',
    units    = '1/m^2',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{3,DIP} = \oint{\frac{1}{|\rho_x|^3}\,ds}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I4 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I4_from_dipoles,
    symbol   = r'<math>I_\text{4,DIP}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{4,DIP} = \frac{\eta_x(s_0) \tan \theta(s_0)}{\rho_x^2} + \oint{\frac{\eta_x}{\rho_x^3} \left(1 + 2 \rho_x^2 k\right)\,ds} + \frac{\eta_x(s_1) \tan \theta(s_1)}{\rho_x^2}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I5 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I5_from_dipoles,
    symbol   = r'<math>I_\text{5,DIP}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [r'<math>I_\text{5,DIP} = \oint{\frac{H_x}{|\rho_x|^3}\,ds}</math>',
                r"<math>H_x \equiv \gamma_x \eta_x^2 + 2 \alpha_x \eta_x \eta_x^' + \beta_x {\eta_x^'}^2</math>"],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I6 from dipoles',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I6_from_dipoles,
    symbol   = r'<math>I_\text{6,DIP}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [r'<math>I_\text{6,DIP} = \oint{k^2 \eta_x^2\,ds}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring radiation integral I1 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I1_from_IDs,
    symbol   = r'<math>I_\text{1,IDs}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [r'<math>I_\text{1,IDs} = \oint{\frac{\eta_x}{\rho_x}\,ds}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I2 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I2_from_IDs,
    symbol   = r'<math>I_\text{2,IDs}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{2,IDs} = \oint{\frac{1}{\rho_x^2}\,ds}</math>'],
  ),
   
  Parameter(
    name     = 'Storage ring radiation integral I3 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I3_from_IDs,
    symbol   = r'<math>I_\text{3,IDs}</math>',
    units    = '1/m^2',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{3,IDs} = \oint{\frac{1}{|\rho_x|^3}\,ds}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I4 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I4_from_IDs,
    symbol   = r'<math>I_\text{4,IDs}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version'],
    obs      = [r'<math>I_\text{4,IDs} = \frac{\eta_x(s_0) \tan \theta(s_0)}{\rho_x^2} + \oint{\frac{\eta_x}{\rho_x^3} \left(1 + 2 \rho_x^2 k\right)\,ds} + \frac{\eta_x(s_1) \tan \theta(s_1)}{\rho_x^2}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I5 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I5_from_IDs,
    symbol   = r'<math>I_\text{5,IDs}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [r'<math>I_\text{5,IDs} = \oint{\frac{H_x}{|\rho_x|^3}\,ds}</math>',
                r"<math>H_x \equiv \gamma_x \eta_x^2 + 2 \alpha_x \eta_x \eta_x^' + \beta_x {\eta_x^'}^2</math>"],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I6 from IDs',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I6_from_IDs,
    symbol   = r'<math>I_\text{6,IDs}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring beam magnetic rigidity',
                'Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [r'<math>I_\text{6,IDs} = \oint{k^2 \eta_x^2\,ds}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring radiation integral I1',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I1,
    symbol   = r'<math>I_\text{1}</math>',
    units    = 'm',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I1 from dipoles',
                'Storage ring radiation integral I1 from IDs'],
    obs      = [r'<math>I_\text{1} = I_\text{1,DIP} + I_\text{1,IDs}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I2',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I2,
    symbol   = r'<math>I_\text{2}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I2 from dipoles',
                'Storage ring radiation integral I2 from IDs'],
    obs      = [r'<math>I_\text{2} = I_\text{2,DIP} + I_\text{2,IDs}</math>'],
  ),
   
  Parameter(
    name     = 'Storage ring radiation integral I3',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I3,
    symbol   = r'<math>I_\text{3}</math>',
    units    = '1/m^2',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I3 from dipoles',
                'Storage ring radiation integral I3 from IDs'],
    obs      = [r'<math>I_\text{3} = I_\text{3,DIP} + I_\text{3,IDs}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I4',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I4,
    symbol   = r'<math>I_\text{4}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I4 from dipoles',
                'Storage ring radiation integral I4 from IDs'],
    obs      = [r'<math>I_\text{4} = I_\text{4,DIP} + I_\text{4,IDs}</math>'],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I5',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I5,
    symbol   = r'<math>I_5</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I5 from dipoles',
                'Storage ring radiation integral I5 from IDs'],
    obs      = [r'<math>I_5 = I_\text{5,DIP} + I_\text{5,IDs}</math>',
                r"<math>H_x \equiv \gamma_x \eta_x^2 + 2 \alpha_x \eta_x \eta_x^' + \beta_x {\eta_x^'}^2</math>"],
  ),
                  
  Parameter(
    name     = 'Storage ring radiation integral I6',
    group    = 'FAC',
    value    = Prms.sr_radiation_integral_I6,
    symbol   = r'<math>I_\text{6}</math>',
    units    = '1/m',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I6 from dipoles',
                'Storage ring radiation integral I6 from IDs'],
    obs      = [r'<math>I_\text{6} = I_\text{6,DIP} + I_\text{6,IDs}</math>'],
  ),
   
  Parameter(
    name     = 'Storage ring optics mode',
    group    = 'FAC',
    value    = Prms.sr_optics_mode,
    symbol   = '',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [],
  ),
  
  Parameter(
    name     = 'Storage ring horizontal betatron tune',
    group    = 'FAC',
    value    = Prms.sr_horizontal_betatron_tune,
    symbol   = r'<math>\nu_x</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),
                
  Parameter(
    name     = 'Storage ring vertical betatron tune',
    group    = 'FAC',
    value    = Prms.sr_vertical_betatron_tune,
    symbol   = r'<math>\nu_y</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring synchrotron tune',
    group    = 'FAC',
    value    = Prms.sr_synchrotron_tune,
    symbol   = r'<math>\nu_s</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),
  
  Parameter(
    name     = 'Storage ring horizontal natural chromaticity',
    group    = 'FAC',
    value    = Prms.sr_horizontal_natural_chromaticity,
    symbol   = r'<math>\xi_{x,0}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),
                
  Parameter(
    name     = 'Storage ring vertical natural chromaticity',
    group    = 'FAC',
    value    = Prms.sr_vertical_natural_chromaticity,
    symbol   = r'<math>\xi_{y,0}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring horizontal chromaticity',
    group    = 'FAC',
    value    = Prms.sr_horizontal_chromaticity,
    symbol   = r'<math>\xi_x</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),
                
  Parameter(
    name     = 'Storage ring vertical chromaticity',
    group    = 'FAC',
    value    = Prms.sr_vertical_chromaticity,
    symbol   = r'<math>\xi_y</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring lattice version',
                'Storage ring optics mode'],
    obs      = [],
  ),

  Parameter(
    name     = 'Storage ring energy loss per turn from dipoles',
    group    = 'FAC',
    value    = Prms.sr_energy_loss_per_turn_from_dipoles,
    symbol   = r'<math>U_\text{0,DIP}</math>',
    units    = 'keV',
    revision = '2014-08-01',
    deps     = ['Storage ring beam energy',
                'Storage ring radiation integral I2 from dipoles'],
    obs      = [r'<math>U_\text{0,DIP} = \oint{P_\gamma dt} = \frac{C_\gamma}{2\pi} E^4_0 I_\text{2,DIP}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring overvoltage from dipoles',
    group    = 'FAC',
    value    = Prms.sr_overvoltage_from_dipoles,
    symbol   = r'<math>q_\text{DIP}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring RF cavity peak voltage',
                'Storage ring energy loss per turn from dipoles'],
    obs      = [r'<math>q_\text{DIP} = \frac{eV_\text{RF}}{U_\text{0,DIP}}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring synchronous phase from dipoles',
    group    = 'FAC',
    value    = Prms.sr_synchronous_phase_from_dipoles,
    symbol   = r'<math>\phi_0</math>',
    units    = unicode('°',encoding='utf-8'),
    revision = '2014-08-01',
    deps     = ['Storage ring overvoltage from dipoles'],
    obs      = [r'<math>\phi_0 = \pi - \arcsin\left(\frac{1}{q_\text{DIP}}\right)</math>'],
  ),
                            
  Parameter(
    name     = 'Storage ring linear momentum compaction from dipoles',
    group    = 'FAC',
    value    = Prms.sr_linear_momentum_compaction_from_dipoles,
    symbol   = r'<math>\alpha_\text{1,DIP}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I1 from dipoles',
                'Storage ring lattice circumference'],
    obs      = [r'<math>\alpha_\text{1,DIP} = \frac{I_\text{1,DIP}}{C}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring RF energy acceptance from dipoles',
    group    = 'FAC',
    value    = Prms.sr_rf_energy_acceptance_from_dipoles,
    symbol   = r'<math>\epsilon_\text{max,DIP}</math>',
    units    = '%',
    revision = '2014-08-01',
    deps     = ['Storage ring overvoltage from dipoles',
                'Storage ring beam energy',
                'Storage ring energy loss per turn from dipoles',
                'Storage ring harmonic number',
                'Storage ring linear momentum compaction from dipoles'],
    obs      = [r'<math>\epsilon_\text{max,DIP} = \sqrt{\frac{1}{\pi h \alpha_{x,\text{DIP}} \frac{U_\text{0,DIP}}{E} F(q_\text{DIP})}</math>',
                r'<math>F(q) = 2 \left( \sqrt{q^2 - 1} - \cos^{-1} (1/q) \right)</math>'],
  ),
                            
  Parameter(
    name     = 'Storage ring horizontal damping partition number from dipoles',
    group    = 'FAC',
    value    = Prms.sr_horizontal_damping_partition_number_from_dipoles,
    symbol   = r'<math>J_{x,\text{DIP}}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I2 from dipoles',
                'Storage ring radiation integral I4 from dipoles'],
    obs      = [r'<math>J_{x,\text{DIP}} = 1 - \frac{I_\text{4,DIP}}{I_\text{2,DIP}}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring vertical damping partition number from dipoles',
    group    = 'FAC',
    value    = Prms.sr_vertical_damping_partition_number_from_dipoles,
    symbol   = r'<math>J_{y,\text{DIP}}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [r'<math>J_{y,\text{DIP}} = 1 - \frac{I_\text{4y,DIP}}{I_\text{2,DIP}} \equiv 1</math>',
                'Vertical damping partition number is identically one for error-free machines for which vertical dispersion functions are zero everywhere.'],
  ),
  
  Parameter(
    name     = 'Storage ring longitudinal damping partition number from dipoles',
    group    = 'FAC',
    value    = Prms.sr_longitudinal_damping_partition_number_from_dipoles,
    symbol   = r'<math>J_{s,\text{DIP}}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring horizontal damping partition number from dipoles',
               'Storage ring vertical damping partition number from dipoles'],
    obs      = [r'<math>J_{s,\text{DIP}} = 4 - J_{x,\text{DIP}} - J_{y,\text{DIP}}</math>',
                "Its value is derived from Robinson's sum rule."],
  ),
                            
  Parameter(
    name     = 'Storage ring natural emittance from dipoles',
    group    = 'FAC',
    value    = Prms.sr_natural_emittance_from_dipoles,
    symbol   = r'<math>\epsilon_\text{0,DIP}</math>',
    units    = unicode('nm⋅rad',encoding='utf-8'),
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring horizontal damping partition number from dipoles',
                'Storage ring radiation integral I5 from dipoles',
                'Storage ring radiation integral I2 from dipoles'],
    obs      = [r'<math>\epsilon_\text{0,DIP} = C_\text{q} \frac{\gamma^2}{J_{x,\text{DIP}}} \frac{I_\text{5,DIP}}{I_\text{2,DIP}}</math>'],
  ),
                            
  Parameter(
    name     = 'Storage ring natural energy spread from dipoles',
    group    = 'FAC',
    value    = Prms.sr_natural_energy_spread_from_dipoles,
    symbol   = r'<math>\sigma_{\delta,\text{DIP}}</math>',
    units    = '%',
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring radiation integral I2 from dipoles',
                'Storage ring radiation integral I3 from dipoles',
                'Storage ring radiation integral I4 from dipoles'],
    obs      = [r'<math>\sigma_{\delta,\text{DIP}} = \sqrt{C_\text{q} \gamma^2 \frac{I_\text{3,DIP}}{2 I_\text{2,DIP} + I_\text{4,DIP}}}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring energy loss per turn from IDs',
    group    = 'FAC',
    value    = Prms.sr_energy_loss_per_turn_from_IDs,
    symbol   = r'<math>U_\text{0,IDs}</math>',
    units    = 'keV',
    revision = '2014-08-01',
    deps     = ['Storage ring beam energy',
                'Storage ring radiation integral I2 from IDs'],
    obs      = [r'<math>U_\text{0,IDs} = \oint{P_\gamma dt} = \frac{C_\gamma}{2\pi} E^4_0 I_\text{2,IDs}</math>'],
  ),
  
  Parameter(
    name     = 'Storage ring energy loss per turn',
    group    = 'FAC',
    value    = Prms.sr_energy_loss_per_turn,
    symbol   = r'<math>U_\text{0}</math>',
    units    = 'keV',
    revision = '2014-08-01',
    deps     = ['Storage ring beam energy',
                'Storage ring radiation integral I2'],
    obs      = [r'<math>U_\text{0} = \oint{P_\gamma dt} = \frac{C_\gamma}{2\pi} E^4_0 I_\text{2}</math>'],
  ),

  Parameter(
    name     = 'Storage ring overvoltage',
    group    = 'FAC',
    value    = Prms.sr_overvoltage,
    symbol   = r'<math>q</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring RF cavity peak voltage',
                'Storage ring energy loss per turn'],
    obs      = [r'<math>q = \frac{eV_\text{RF}}{U_\text{0}}</math>'],
  ),
 
  Parameter(
    name     = 'Storage ring synchronous phase',
    group    = 'FAC',
    value    = Prms.sr_synchronous_phase,
    symbol   = r'<math>\phi_0</math>',
    units    = unicode('°',encoding='utf-8'),
    revision = '2014-08-01',
    deps     = ['Storage ring overvoltage'],
    obs      = [r'<math>\phi_0 = \pi - \arcsin\left(\frac{1}{q}\right)</math>'],
  ),

  Parameter(
    name     = 'Storage ring linear momentum compaction',
    group    = 'FAC',
    value    = Prms.sr_linear_momentum_compaction,
    symbol   = r'<math>\alpha_\text{1}</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I1',
                'Storage ring lattice circumference'],
    obs      = [r'<math>\alpha_\text{1} = \frac{I_\text{1}}{C}</math>'],
  ),

  Parameter(
    name     = 'Storage ring RF energy acceptance',
    group    = 'FAC',
    value    = Prms.sr_rf_energy_acceptance,
    symbol   = r'<math>\epsilon_\text{max}</math>',
    units    = '%',
    revision = '2014-08-01',
    deps     = ['Storage ring overvoltage',
                'Storage ring beam energy',
                'Storage ring energy loss per turn',
                'Storage ring harmonic number',
                'Storage ring linear momentum compaction'],
    obs      = [r'<math>\epsilon_\text{max} = \sqrt{\frac{1}{\pi h \alpha_x} \frac{U_0}{E} F(q)}</math>',
                r'<math>F(q) = 2 \left( \sqrt{q^2 - 1} - \cos^{-1} (1/q) \right)</math>'],
  ),

  Parameter(
    name     = 'Storage ring horizontal damping partition number',
    group    = 'FAC',
    value    = Prms.sr_horizontal_damping_partition_number,
    symbol   = r'<math>J_x</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring radiation integral I2',
                'Storage ring radiation integral I4'],
    obs      = [r'<math>J_x = 1 - \frac{I_\text{4}}{I_\text{2}}</math>'],
  ),

  Parameter(
    name     = 'Storage ring vertical damping partition number',
    group    = 'FAC',
    value    = Prms.sr_vertical_damping_partition_number,
    symbol   = r'<math>J_y</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = [],
    obs      = [r'<math>J_y = 1 - \frac{I_{4,y}}{I_\text{2}} \equiv 1</math>',
                'Vertical damping partition number is identically one for error-free machines for which vertical dispersion functions are zero everywhere.'],
  ),

  Parameter(
    name     = 'Storage ring longitudinal damping partition number',
    group    = 'FAC',
    value    = Prms.sr_longitudinal_damping_partition_number,
    symbol   = r'<math>J_s</math>',
    units    = '',
    revision = '2014-08-01',
    deps     = ['Storage ring horizontal damping partition number',
                'Storage ring vertical damping partition number'],
    obs      = [r'<math>J_s = 4 - J_x - J_y</math>',
                "Its value is derived from Robinson's sum rule."],
  ),
 
  Parameter(
    name     = 'Storage ring natural emittance',
    group    = 'FAC',
    value    = Prms.sr_natural_emittance,
    symbol   = r'<math>\epsilon_0</math>',
    units    = unicode('nm⋅rad',encoding='utf-8'),
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring horizontal damping partition number',
                'Storage ring radiation integral I5',
                'Storage ring radiation integral I2'],
    obs      = [r'<math>\epsilon_0 = C_\text{q} \frac{\gamma^2}{J_x} \frac{I_\text{5}}{I_\text{2}}</math>'],
  ),

  Parameter(
    name     = 'Storage ring natural energy spread',
    group    = 'FAC',
    value    = Prms.sr_natural_energy_spread,
    symbol   = r'<math>\sigma_\delta</math>',
    units    = '%',
    revision = '2014-08-01',
    deps     = ['Storage ring beam gamma factor',
                'Storage ring radiation integral I2',
                'Storage ring radiation integral I3',
                'Storage ring radiation integral I4'],
    obs      = [r'<math>\sigma_\delta = \sqrt{C_\text{q} \gamma^2 \frac{I_\text{3}}{2 I_\text{2} + I_\text{4}}}</math>'],
  ),

  Parameter(
    name     = 'Storage ring horizontal betatron frequency',
    group    = 'FAC',
    value    = Prms.sr_horizontal_betatron_frequency,
    symbol   = r'<math>f_x</math>',
    units    = 'kHz',
    revision = '2014-08-01',
    deps     = ['Storage ring revolution frequency',
                'Storage ring horizontal betatron tune'],
    obs      = [r'<math>f_x = f_\text{rev} \left( \nu_x - \lfloor \nu_x\rfloor \right)</math>'],
  ),
                
  Parameter(
    name     = 'Storage ring vertical betatron frequency',
    group    = 'FAC',
    value    = Prms.sr_vertical_betatron_frequency,
    symbol   = r'<math>f_y = f_\text{rev} \left( \nu_y - \lfloor \nu_y\rfloor \right)</math>',
    units    = 'kHz',
    revision = '2014-08-01',
    deps     = ['Storage ring revolution frequency',
                'Storage ring vertical betatron tune'],
    obs      = [],
  ),
                  
  Parameter(
    name     = 'Storage ring synchrotron frequency',
    group    = 'FAC',
    value    = Prms.sr_synchrotron_frequency,
    symbol   = r'<math>f_s = f_\text{rev} \left( \nu_s - \lfloor \nu_s\rfloor \right)</math>',
    units    = 'kHz',
    revision = '2014-08-01',
    deps     = ['Storage ring revolution frequency',
                'Storage ring synchrotron tune'],
    obs      = [],
  ),
 
]
