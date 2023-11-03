"""
=================
An animated image
=================

This example demonstrates how to animate an image.
"""
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.animation as animation
from functools import partial

def make_grid_animation(x_lab, y_lab, Ey, **kwargs):
    
    save_dir = kwargs.pop("save_dir", None)
    times = kwargs.pop("times", None)
    clim = kwargs.pop("clim", None)
    cmap = kwargs.pop("cmap", None)
    xlim = kwargs.pop("xlim", None)
    ylim = kwargs.pop("ylim", None)
    yscale = kwargs.pop("yscale", "linear")
    ylabel = kwargs.pop("ylabel", "Y [um]")
    xlabel = kwargs.pop("xlabel", "X [um]")
    step = kwargs.pop("step", None)
    figsize = kwargs.pop("figsize", [5, 2])
    fps = kwargs.pop("fps", 10)
    if_log_norm = kwargs.pop("if_log_norm", None)
    quantile = kwargs.pop("quantile", 0.1)
    
    Field = Ey[0]
    fig = plt.figure(figsize = figsize)
    plt.yscale(yscale)
    if if_log_norm:
        print("if_log_norm", if_log_norm)
        plotField = Field[np.abs(y_lab) < ylim[1], : ][:, (x_lab > xlim[0]) & (x_lab < xlim[1])]
        vmax = plotField.max()
        vmin = np.quantile(plotField, quantile)
        im = plt.pcolormesh(x_lab[(x_lab > xlim[0]) & (x_lab < xlim[1])],
                            y_lab[np.abs(y_lab) < ylim[1]], 
                            plotField,
                            cmap = cmap, norm = LogNorm(vmin, vmax),
                            animated = True)
    else:
        print("if_log_norm", if_log_norm)
        im = plt.pcolormesh(x_lab[(x_lab > xlim[0]) & (x_lab < xlim[1])],
                        y_lab[np.abs(y_lab) < ylim[1]], 
                        Field[np.abs(y_lab) < ylim[1], : ][:, (x_lab > xlim[0]) & (x_lab < xlim[1])],
                        cmap = cmap,
                        animated = True)
    plt.colorbar()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlim)
    plt.ylim(ylim)
    text = plt.title(f"time: {times[0]:.3f} [ps]")
    plt.tight_layout()

    #max_idx = Ey.shape
    
    def updatefig(frame, im, *, times, Ey, step, xlim, ylim, clim, text):
        idx = frame #* step
        Field = Ey[idx]
        cmin = Field.min()
        ###############
        ###############
        fresh_data = Field[np.abs(y_lab) < ylim[1], : ][:, (x_lab > xlim[0]) & (x_lab < xlim[1])]
        im.set_array(fresh_data)
        if clim:
            plt.clim(clim)
        else:
            if if_log_norm:
                vmax = fresh_data.max()
                vmin = np.quantile(fresh_data, quantile)
                plt.clim([vmin, vmax])
            else:
                vmax = fresh_data.max()
                vmin = fresh_data.min()
                if vmin < 0:
                    plt.clim([-vmax, vmax])
                else:
                    plt.clim([vmin, vmax])
        text.set_text(f"time: {times[idx]:.3f} [ps]")
        idx += step
        return im,

    ani = animation.FuncAnimation(fig, partial(updatefig, im = im, times = times, Ey = Ey, step = step, xlim = xlim, 
                                ylim = ylim,clim = clim, text = text), frames = tqdm(range(0, Ey.shape, step)),
                                blit = True, interval = fps)

    ani.save(save_dir, fps = fps)
    
    return