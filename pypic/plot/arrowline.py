from matplotlib import pyplot as plt
from matplotlib import transforms
from math import sin,cos,atan,pi,sqrt,tan
import numpy as np
from types import MethodType #用于更改axes实例方法
plt.rc('font',family='Times New Roman') 

class arrow(): 
    '''
    arrow()向图中添加一个箭头, 准确说是没有尾巴的箭头
    参数: 
            ax: 要绘制的坐标区的句柄
            x: 起点和终点的x坐标
            y: 起点和终点的y坐标
            size: 绘制的箭头大小（箭头的基本大小是不依赖于坐标区的大小的）
            angle: 箭头顶端的张角（默认40度）
            d_frac: 控制绘制的箭头的尾部中部连接点距顶点的距离是标准状态的d_frac倍, 影响箭头样式
            color: 箭头填充的颜色
            style: 可选样式为full / above / below, 分别为标准样式、上三角、下三角
            **kw: 用于plt.fill的其他自定义参数
    '''
    def __init__(self,ax,x,y,size,angle=40,d_frac=1,color='#1f77b4',style='full',**kw):
        self.x=x
        self.y=y
        self.size=size
        self.angle=angle
        self.d_frac=d_frac
        self.color=color
        self.style=style
        self.kw=kw
        self.plt_arrow(ax)
        
    def plt_arrow(self,ax):
        base_d=0.1*self.size
        d=base_d*self.d_frac
        half_h=base_d*tan(self.angle/360*pi)
        X=[-d,-base_d,0,-base_d,-d]
        if self.style=='full': Y=[0,half_h,0,-half_h,0]
        elif self.style=='above': Y=[0,half_h,0,0,0]
        elif self.style=='below': Y=[0,0,0,-half_h,0]
        else: raise ValueError('style的值应为full/above/below')
        trans = (ax.figure.dpi_scale_trans+transforms.ScaledTranslation(self.x[1], self.y[1], ax.transData)) #设定两个变换, 一个使绘制出的箭头大小不依赖于坐标系而是屏幕, 一个将箭头移至坐标系中的指定坐标
        theta = self.calc_theta(ax,self.x,self.y)
        coords = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])@(np.array([X,Y])+np.array([[0.01],[0]])) #将坐标和旋转矩阵相乘, 加上的偏移量[[0.01],[0]]目的是解决绘制的箭头处于线条终点时顶端两侧由于线宽导致的像素露出
        self.handle = ax.fill(coords[0,:],coords[1,:],color=self.color,**self.kw, transform=trans)[0]
        
    @staticmethod
    def calc_theta(ax,x,y):
        '''
        计算两点连线和x轴的夹角
        此函数计算的夹角依赖于屏幕而不是坐标系
        参数: 
                ax: 要计算绝对角度的坐标系
                x: 起始点和终点的x坐标
                y: 起始点和终点的y坐标
        '''
#         bbox = ax.get_window_extent().transformed(ax.figure.dpi_scale_trans.inverted()) #https://stackoverflow.com/questions/19306510/determine-matplotlib-axis-size-in-pixels, 获取坐标区的bbox尺寸
#         ax_width=ax.axis()[1]-ax.axis()[0]
#         ax_height=ax.axis()[3]-ax.axis()[2]
#         t_w=(x[1]-x[0])/ax_width*bbox.width #获取线条的‘绝对宽度’
#         t_h=(y[1]-y[0])/ax_height*bbox.height
        p1=list(ax.transData.transform([x[0],y[0]])) #将坐标转为像素坐标
        p2=list(ax.transData.transform([x[1],y[1]]))
        t_h=(p2[1]-p1[1])
        t_w=(p2[0]-p1[0])
        if t_h>0 and t_w==0:
            theta=pi/2
        elif t_h<0 and t_w==0:
            theta=-pi/2
        elif t_h==0 and t_w==0:
            raise ValueError('请不要设置起始点和终点重合')
        else:
            theta=atan(t_h/t_w) #计算图线的‘绝对夹角’
            if t_h<0 and t_w<0:
                theta+=pi
            elif t_h>0 and t_w<0:
                theta+=pi
        return theta


class arrowline():
    '''
    arrowline类用于向坐标区中添加带箭头的线, 可以是多点的曲线, 目前只支持添加仅有一组x,y坐标的曲线, 不过应该够用了, 更复杂的绘图需求在此之上调用封装就好
    参数: 
            style: 添加箭头的模式, 可选参数: to、to_back、middle、equal_d
                to: 在终点添加
                to_back: 在终点和起点各添加一个朝向两端的箭头
                middle: 在曲线中间点位置添加箭头
                equal_d: 在曲线上每隔n个点添加一个箭头
            interval: 设置equal_d模式下添加箭头的点间隔
            self.arrows储存了所有箭头的句柄
            self.callback是matplotlib RsizeEvent回调的编号, 该回调用于命令行运行脚本后得到的图形界面中实时查看时, 在缩放窗口时箭头方位能正确变化
    '''
    def __init__(self,ax,x,y,cosys='rect',arrow_size=1,style='to',arrow_angle=40,d_frac=1,color='#1f77b4',arrow_style='full',interval=50,**kw):
        self.arrows=[]
        arrowline.set_ax(ax) #对当前ax进行初始化设置, 增加一些属性, 对axes实例的方法进行一些增添修改
        if cosys=='rect' or cosys=='polar':
            self.handle=ax.plot(x,y,color=color,**kw)[0]
        elif cosys=='loglog':
            self.handle=ax.loglog(x,y,color=color,**kw)[0]
            
        x,y,l=list(x),list(y),len(x)
        kw={'angle':arrow_angle,'d_frac':d_frac,'color':color,'style':arrow_style}
        if style=='to':
            l-=1
            self.arrows.append(arrow(ax,[x[l-1],x[l]],[y[l-1],y[l]],arrow_size,**kw))
        elif style=='to_back':
            l-=1
            self.arrows.append(arrow(ax,[x[l-1],x[l]],[y[l-1],y[l]],arrow_size,**kw))
            self.arrows.append(arrow(ax,[x[1],x[0]],[y[1],y[0]],arrow_size,**kw))
        elif style=='middle':
            if l%2==0:
                l=int(l/2)
                self.arrows.append(arrow(ax,[x[l-1],(x[l-1]+x[l])/2],[y[l-1],(y[l-1]+y[l])/2],arrow_size,**kw))
            else:
                l=int(l/2)
                self.arrows.append(arrow(ax,[x[l-1],x[l]],[y[l-1],y[l]],arrow_size,**kw))
        elif style=='equal_d':
            if type(interval)!=type(1):
                raise ValueError('interval应为正整数')
            if interval<=0:
                raise ValueError('请不要设置interval为小于等于零的数')
            i=interval
            while i<l:
                self.arrows.append(arrow(ax,[x[i-1],x[i]],[y[i-1],y[i]],arrow_size,**kw))
                i+=interval
        else:
            raise ValueError('请检查style参数是否正确')
        self.callback=ax
        ax.arrowlines.append(self)
        
    def remove(self): #彻底移除arrowline
        self.handle.axes.arrowlines.remove(self)
        self.handle.remove()
        for i in self.arrows:
            i.handle.remove()
            del i
        del self
    
    @property
    def callback(self):
        return self._callback
    
    @callback.setter
    def callback(self,ax):
        def resized(event):
            for i in self.arrows:
                i.handle.remove()
                i.plt_arrow(ax)
        self._callback=ax.figure.canvas.mpl_connect('resize_event', resized)
        
    @staticmethod
    def set_ax(ax):
        try:
            ax.prev_xlim
        except AttributeError: #如果不存在prev_xlim属性, 则进行初始化, 避免重复初始化
            ax.prev_xlim=ax.get_xlim()
            ax.prev_ylim=ax.get_ylim()
            ax.arrowlines=[]
            def check(self):
                xlim=self.get_xlim()
                ylim=self.get_ylim()
                if self.prev_xlim!=xlim or self.prev_ylim!=ylim:
                    self.prev_xlim=xlim
                    self.prev_ylim=ylim
                    for obj in self.arrowlines:
                        for i in obj.arrows:
                            i.handle.remove()
                            i.plt_arrow(ax)
            ax.check_xylim=MethodType(check, ax)
            ax.clear1=ax.clear #防止循环调用
            def new_clear(self):
                self.arrowlines=[]
                return self.clear1()
            ax.clear=MethodType(new_clear, ax) #更改ax原有的clear()方法以实现清空画布时同步清空arrowlines列表, 防止清空画布后遗留的arrowlines会重复绘制
            #ax._request_autoscale_view1=ax._request_autoscale_view
            ax._request_autoscale_view1=ax.autoscale_view
            def new_request_autoscale_view(self,tight=None, scalex=True, scaley=True):
                args=self._request_autoscale_view1(tight=tight,scalex=scalex,scaley=scaley)
                self.check_xylim()
                return args
            ax._request_autoscale_view=MethodType(new_request_autoscale_view, ax) #更改原有的_request_autoscale_view方法以使得每次坐标区的视图状态改变时箭头方向都能及时更新