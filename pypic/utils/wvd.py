import numpy as np
from scipy.signal import hilbert
from tftb.processing import WignerVilleDistribution

def wvd(field, t):
    """
    计算 Wigner-Ville 分布
    :param field: 信号数据
    :param z: 空间坐标
    :return: Wigner-Ville 分布结果
    """
    field_complex = hilbert(field)  # 返回复数，包含瞬时相位和包络
    signal = field_complex
    # # 构造频率坐标轴（Hz）\
    dt = t[1] - t[0]  # 时间步长
    freq_s = 1/dt  # sampling frequency

    # 创建 Wigner-Ville 分布对象
    wvd = WignerVilleDistribution(signal)
    tfr, t_vals, f_vals = wvd.run()
    f_vals = f_vals*freq_s
    t_vals = t_vals*dt
    return tfr, t_vals, f_vals
