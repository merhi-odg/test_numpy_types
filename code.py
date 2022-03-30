# modelop.slot.0:in-use
# modelop.slot.1:in-use

import numpy
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# modelop.init
def begin():
    pass
  
  
# modelop.score
def action(data):
    
    # data = {"case": <str>}
    case = data["case"].lower()
    
    dict_with_numpy_nan = {"a":1.3, "b":None, "c":-numpy.pi, "d":numpy.nan}
    dict_with_numpy_inf = {"a":1.3, "b":None, "c":-numpy.e , "d":numpy.inf, "e": -numpy.inf}
    dict_with_numpy_nan_and_inf = {"a":1.3, "b":None, "c":-numpy.pi, "d":numpy.inf, "e":numpy.nan}

    if case=="numpy_nan":
        output = dict_with_numpy_nan
    elif case=="numpy_inf":
        output = dict_with_numpy_inf
    elif case=="numpy_nan_and_inf":
        output = dict_with_numpy_nan_and_inf
    elif case=="nan_to_none":
        output = fix_numpy_nans_and_infs_in_dict(dict_with_numpy_nan)
    elif case=="inf_to_none":
        output = fix_numpy_nans_and_infs_in_dict(dict_with_numpy_inf)
    elif case=="nan_and_inf_to_none":
        output = fix_numpy_nans_and_infs_in_dict(dict_with_numpy_nan_and_inf)
        
    return output 


def fix_numpy_nans_and_infs_in_dict(values:dict) -> dict:
    """A function to change all numpy.nan and numpy.inf values in a flat dictionary to python Nones.

    Args:
        values (dict): Input dict to fix.

    Returns:
        dict: Fixed dict.
    """

    for key, val in values.items():
        # If value is numeric (not None), check for numpy.nan and numpy.inf
        # If True, change to None, else keep unchanged
        if val is not None:
            if numpy.isnan(val):
                values[key] = None
            elif numpy.isinf(val):
                logger.warning(
                    "Infinity encountered on column %s! Setting value to None.",
                    key
                )
                values[key] = None

    return values
