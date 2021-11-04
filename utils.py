class PlotType:
    PIE = 'pie'
    HISTOGRAM = 'histogram'
    BAR = 'bar'


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


def get_plot_type(var_type, data):
    if var_type == 1:
        return PlotType.PIE

    if var_type == 2:
        for item in data:
            if type(item) == float:
                return PlotType.HISTOGRAM
        
        return PlotType.BAR