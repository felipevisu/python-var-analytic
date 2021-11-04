from constants import PlotType, VarType, SubType


def clear_value(value):
    value = value.replace(',', '.')

    try:
        value = int(value)
        return value
    except Exception:
        pass

    try:
        value = float(value)
        return value
    except Exception:
        pass

    return None


def get_sub_type(var_type, data):
    if var_type == VarType.QUANTITATIVE:
        for item in data:
            if type(item) == float:
                return SubType.CONTINUOUS
        return SubType.DISCRETE
    
    return None


def get_plot_type(var_type, sub_type):
    if var_type == VarType.QUALITATIVE:
        return PlotType.PIE

    if var_type == VarType.QUANTITATIVE:
        if sub_type == SubType.CONTINUOUS:
            return PlotType.HISTOGRAM
        
        return PlotType.BAR