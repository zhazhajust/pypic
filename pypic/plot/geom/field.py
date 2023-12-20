import matplotlib.pyplot as plt
#from ..constants import um

def plot(x, y, ey_data, **kwargs):
    figsize = kwargs.pop("figsize", [4, 3])
    xlabel = kwargs.pop("xlabel", "X [um]")
    ylabel = kwargs.pop("ylabel", "X [um]")
    clabel = kwargs.pop("clabel", "a.u.")
    plt.figure(figsize=figsize)
    plt.pcolormesh(x, y, ey_data.T, **kwargs)
    cbar = plt.colorbar()
    cbar.set_label(clabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return
