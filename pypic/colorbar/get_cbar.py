from numpy import linspace
from matplotlib.pyplot import get_cmap, cm, colormaps, set_cmap

def reg_cmap(iname = 'jet'):
    oname = 'dist'    
    low = 0.15       
    high = 1
    #(position, [r,g,b,a] or #rrggbb)
    special = [(0,[1,1,1,1])]      
    cmap = get_cmap(iname)
    N = int((high - low) * 256)
    values = linspace(low,high,N)
    colors = cmap(values)
    colorlist = [(values[i],colors[i]) for i in range(N)]
    colorlist = special + colorlist
    cmap = cm.colors.LinearSegmentedColormap.from_list(oname,colorlist)
    #An other example: plt.cm.colors.LinearSegmentedColormap.from_list(‘cmap’, [‘#FFFFFF’, ‘#98F5FF’, ‘#00FF00’, ‘#FFFF00’,’#FF0000’, ‘#8B0000’], 256)
    colormaps.register(cmap=cmap, force = True)
    return cmap

def reg_cmap_transparent(iname, alpha):
    oname = iname + '_transparent'
    cmap = get_cmap(iname)
    values = np.linspace(0,1,256)
    colors = cmap(values)
    for i in range(256):
        colors[i][3] = alpha[i]
    colorlist = [(values[i],colors[i]) for i in range(256)]
    cmap = cm.colors.LinearSegmentedColormap.from_list(oname,colorlist)
    colormaps.register(cmap=cmap, force = True)
    return cmap

def create_alpha(func):
    return [ 1 if func(i)>1 else 0 if func(i)<0 else func(i) for i in range(256)]

#iname = 'jet'
#lambda x:(0.7 + (1/256*x) *0.3)
#lambda x:(np.exp(x/(256))-0.7)

def getTransCmap(iname = 'jet', func = lambda x: (0.7 + (1/256*x) *0.3)):#lambda x:(0.7 + (1/256*x) *0.3)):
    #plt.set_cmap(reg_cmap_transparent(iname,create_alpha(func)))#lambda x:(0.7 + (1/256*x) *0.3))))
    #cmap_trans = plt.get_cmap()
    #return cmap_trans
    return reg_cmap_transparent(iname, create_alpha(func))

def getCmap(iname = 'jet'):#lambda x:(0.7 + (1/256*x) *0.3)):
    #plt.set_cmap(reg_cmap(iname))#lambda x:(0.7 + (1/256*x) *0.3))))
    #cmap_trans = plt.get_cmap()
    #return cmap_trans
    return reg_cmap(iname)

if __name__ == '__main__':
    iname = 'jet'
    set_cmap(reg_cmap_transparent(iname,create_alpha(lambda x:(0.7 + (1/256*x) *0.3))))
    cmap_trans = get_cmap()

