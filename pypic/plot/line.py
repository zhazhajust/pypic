import matplotlib.pyplot as plt

def plot(x, y, *args, **kw):
    if_fig = kw.pop("if_fig", None)
    xlabel = kw.pop("xlabel", None)
    ylabel = kw.pop("ylabel", None)
    xlim = kw.pop("xlim", None)
    ylim = kw.pop("ylim", None)
    figsize = kw.pop("figsize", None)
    if if_fig:
        plt.figure(figsize=figsize)
    lines = plt.plot(x, y, *args, **kw)
    if ylim:
        plt.ylim(ylim)
    if xlim:
        plt.xlim(xlim)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    return lines