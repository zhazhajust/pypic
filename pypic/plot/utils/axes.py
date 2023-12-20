def make_axes(fig, ax, rec = [0.05, 1.08, 0.30, 0.05]):
    #######
    ax_pos = ax.get_position()
    # cax1 = fig.add_axes([ax_pos.x0 + 0.05, ax_pos.y1 + 0.08, 0.30, ax_pos.height * 0.05])
    # cax2 = fig.add_axes([ax_pos.x0 + 0.43, ax_pos.y1 + 0.08, 0.30, ax_pos.height * 0.05])
    # return cax1, cax2
    cax1 = fig.add_axes([ax_pos.x0 + rec[0], ax_pos.y1 + rec[1],
                         rec[2], ax_pos.height * rec[3]])
    return cax1
    
def make_cbar(fig, im1, cax1):
    cbar1 = fig.colorbar(im1, cax = cax1, orientation = 'horizontal', location = 'top')
    return cbar1, cbar2