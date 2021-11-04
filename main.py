from statistics import mean, mode, median
from inputs import get_var_type, get_entry_method, get_data
from utils import get_plot_type, get_sub_type
from plot import plot
from constants import VarType, SubType

if __name__ == '__main__':
    var_type = get_var_type()
    entry_method = get_entry_method()
    data = get_data(var_type, entry_method)
    sub_type = get_sub_type(var_type, data)
    plot_type = get_plot_type(var_type, sub_type)

    print(f'Tipo: {var_type}')
    print(f'Sub-tipo: {sub_type}') if sub_type else None
    print(f'Gráfico: {plot_type}')
    print(f'Média: {mean(data)}') if var_type == VarType.QUANTITATIVE else None
    print(f'Moda: {mode(data)}') if sub_type == SubType.DISCRETE else None
    print(f'Mediana {median(data)}') if sub_type == SubType.CONTINUOUS else None

    plot(plot_type, data)