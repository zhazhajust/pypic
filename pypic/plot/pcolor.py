import matplotlib.pyplot as plt

def pcolor(x, y, z, **kw):
    #im = plt.pcolormesh(z[:, 0]/1e-6, freq/1e12, np.abs(xf[:, :, 150]), cmap = "jet")
    if_fig = kw.pop("if_fig", None)
    xlabel = kw.pop("xlabel", None)
    ylabel = kw.pop("ylabel", None)
    xlim = kw.pop("xlim", None)
    ylim = kw.pop("ylim", None)
    figsize = kw.pop("figsize", None)
    clabel = kw.pop("clabel", None)
    if if_fig:
        plt.figure(figsize = figsize)
    im = plt.pcolormesh(x, y, z, **kw)
    cbar = plt.colorbar()
    if clabel:
        cbar.set_label(clabel)
    if ylim:
        plt.ylim(ylim)
    if xlim:
        plt.xlim(xlim)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    return im

