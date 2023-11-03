import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def plot_lines(axs, x, y, ek, **kwargs):
    cmap = kwargs.pop('cmap', None)
    clim = kwargs.pop('clim', None)
    
    cur_x = x[:]
    cur_y = y[:]
    cur_dydx = ek[:]
    points = np.array([cur_x, cur_y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    if clim:
        norm = plt.Normalize(*clim)
    else:
        norm = plt.Normalize(cur_dydx.min(), cur_dydx.max())
    lc = LineCollection(segments, cmap = cmap, norm=norm)
    lc.set_array(cur_dydx)
    lc.set_linewidth(1.0)
    line = axs.add_collection(lc)

    return line