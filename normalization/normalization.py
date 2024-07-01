import numpy as np
from copy import deepcopy as cp

def normalize_ref(entry, ref_electrode):
    """
    Takes the CVEntry and returns the potential shift introduced by changing
    the reference electrode name. I.e.:
    
        \Delta_E_ref = E_ref[current ref electrode] - E_ref[new ref electrode]
        
    This delta E_ref will be applied to the potential of the CVEntry, essentially 
    shifting the CV on the x-axis.
    """
    entry_ref = entry.get_electrode('REF')['type']
    refs = {
        'Ag/AgCl': 4.637,
        'Ag/AgCl-sat': 4.637,
        'Ag/AgCl_3M': 4.637,
        'Hg/HgO/0.1 M NaOH': 4.9, ### Dummy data
        'RHE': 4.44, ### Dummy Data
        'SCE': 4.688,
        'wire': 5.55, ### Dummy Data,
        'SHE': 4.44,
        'NCE': 4.720
    }
    return refs[entry_ref] - refs[ref_electrode]

def normalize_electrolyte_concentration(entry, c_ref, ion):
    """
    Applies nernstian corrections to the CV, based on the concentration of the 
    electrolyte concentration, more specifically the given ion.
    The introduced shift is added to the x-axis.
    """
    components = entry.system.electrolyte.components
    comp = [i for i in components if ion in i['name']][0]
    c = comp['concentration']
    unit = c['unit'] ; val = cp(c['value'])
    if unit == 'mmol / l':
        factor = 1.e-03
    elif unit == 'umol / l':
        factor = 1.e-06
    else:
        factor = 1.
    T = entry.system.electrolyte.temperature
    T_val = T.value ; T_unit = T.unit
    if T_unit != 'K':
        raise ValueError(f'do not understand unit {T_unit}')
    k_B  = 8.6173324e-05
    mu_ref = k_B * 300. * np.log(c_ref)
    mu_entry = k_B * T_val * np.log(val * factor)
    return mu_entry - mu_ref

def normalize_scan_rate(entry, ref_scan_rate):
    """
    Applies a scan rate normalization, which is applied to the current of the plot.
    """
    scan_rate = entry.figure_description.scan_rate
    val = scan_rate.value
    unit = scan_rate.unit
    return (val / 1000.) / ref_scan_rate
