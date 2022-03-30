# modelop.slot.0:in-use
# modelop.slot.1:in-use

import numpy


# modelop.init
def begin():
    pass
  
  
# modelop.score
def action(data:dict)->dict:
    
    # data = {"case": <str>}
    case = data["case"].lower()
    
    dict_with_numpy_nan = {"a":1, "b":2.3, "c":-numpy.pi, "d":numpy.nan}
    dict_with_numpy_inf = {"a":1, "b":2.3, "c":-numpy.pi, "d":numpy.inf}
    
    if case=="numpy_nan":
        output = dict_with_numpy_nan
    elif case=="numpy_inf":
        output = dict_with_numpy_inf
    elif case=="python_none":
        output = fix_numpy_nans_in_dict(dict_with_numpy_nan)
    elif case=="python_inf":
        output = fix_numpy_infs_in_dict(dict_with_numpy_inf)
        
    return output 


def fix_numpy_nans_in_dict(values:dict) -> dict:
    """A function to change all numpy.nan values in a flat dictionary to python Nones.

    Args:
        values (dict): Input dict to fix.

    Returns:
        dict: Fixed dict.
    """

    for key, val in values.items():
        # Check for numpy.nan;
        # If True, change to None, else keep unchanged
        values[key] = val if not numpy.isnan(val) else None

    return values
  

def fix_numpy_infs_in_dict(values:dict) -> dict:
    """A function to change all numpy.inf values in a flat dictionary to python float('inf').

    Args:
        values (dict): Input dict to fix.

    Returns:
        dict: Fixed dict.
    """

    for key, val in values.items():
        # Check for numpy.inf;
        # If True, change to float('inf'), else keep unchanged
        values[key] = val if not numpy.isinf(val) else float('inf')

    return values
