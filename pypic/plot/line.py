import matplotlib.pyplot as plt

def plot(x, y, **kwargs):
    figsize = kwargs.pop("figsize", [4, 3])
    xlabel = kwargs.pop("xlabel", "X [um]")
    ylabel = kwargs.pop("ylabel", "X [um]")
    plt.figure(figsize=figsize)
    lines = plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return lines