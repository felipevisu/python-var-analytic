from inputs import get_var_type, get_entry_method, get_data
from utils import get_plot_type
from plot import plot

var_type = get_var_type()
print(var_type)

entry_method = get_entry_method()

data = get_data(var_type, entry_method)
print(data)

plot_type = get_plot_type(var_type, data)
print(plot_type)

plot(plot_type, data)

