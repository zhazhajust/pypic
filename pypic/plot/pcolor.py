import matplotlib.pyplot as plt
from .utils.get_cax import add_cax

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
        fig, ax = plt.subplots(figsize = figsize)
    im = ax.pcolormesh(x, y, z, **kw)
    cax = add_cax(fig, ax)
    cbar = fig.colorbar(im, cax)
    if clabel:
        cbar.set_label(clabel)
    if ylim:
        ax.set_ylim(ylim)
    if xlim:
        ax.set_xlim(xlim)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return im, fig, ax
