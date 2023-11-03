import matplotlib.pyplot as plt

def add_cax(fig: plt.Figure, axs: plt.Axes):
    #cax1 = fig.add_axes([axs.get_position().x0 + 0.05, axs.get_position().y1 + 0.05, 0.30, axs.get_position().height * 0.05])
    #cax2 = fig.add_axes([axs.get_position().x0 + 0.43, axs.get_position().y1 + 0.05, 0.30, axs.get_position().height * 0.05])
    cax3 = fig.add_axes([axs.get_position().x1 + 0.03, axs.get_position().y0 + 0.0, 0.02, axs.get_position().height])
    return cax3