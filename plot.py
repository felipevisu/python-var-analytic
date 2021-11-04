import matplotlib.pyplot as plt
from utils import PlotType

def plot_pie(data):
    labels = []
    for item in data:
        if item not in labels:
            labels.append(item)
    
    values = []
    for label in labels:
        value = data.count(label)
        values.append(value)

    _, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%d%%')
    ax1.axis('equal')
    plt.title('Gráfico de setores')
    plt.show()


def plot_bar(data):
    labels = []
    for item in data:
        if item not in labels:
            labels.append(item)
    
    values = []
    for label in labels:
        value = data.count(label)
        values.append(value)

    _, ax1 = plt.subplots()
    ax1.bar(labels, values)
    plt.title('Gráfico de barras')
    plt.show()


def plot_histogram(data):
    _, ax1 = plt.subplots()
    ax1.hist(data, density=True)
    plt.title('Histograma')
    plt.show()


def plot(plot_type, data):
    if plot_type == PlotType.PIE:
        return plot_pie(data)

    if plot_type == PlotType.BAR:
        return plot_bar(data)

    if plot_type == PlotType.HISTOGRAM:
        return plot_histogram(data)