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

# import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def plot_3d_collection(fig, points, value, cmap=cm.gist_earth):

    # 创建线段
    segments = np.array([points[:-1], points[1:]]).transpose(1, 0, 2)

    # 生成颜色数据
    colors = value
    ax = fig.add_subplot(111, projection='3d')

    # 创建线集合
    lines = Line3DCollection(segments, cmap = cmap, linewidths=2)
    lines.set_array(colors)

    # 添加到坐标轴
    ax.add_collection(lines)

    # 设置坐标轴范围
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 4 * np.pi)

    return ax, lines