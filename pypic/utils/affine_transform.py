import numpy as np
from scipy.constants import c
from scipy.interpolate import RegularGridInterpolator

def affine_transform(z, time, Ey):
    t = time[:, 0]
    tau = time - z / c  # τ = t - z/c
    # 构造新的 τ 坐标
    z_left, z_right = z[0][-1], z[-1][0]
    t_start, t_end = tau.min(), tau.max()
    dt = t[1] - t[0]
    z_new = np.linspace(z_left, z_right, 1000)  # 生成新的 z 坐标
    t_new = np.arange(t_start, t_end, dt)  # 生成新的 t 坐标
    Z, Tau = np.meshgrid(z_new, t_new)  # 创建网格
    xi = z - c * time
    # 假设原始 z 和 time 是均匀网格
    interp = RegularGridInterpolator(
        (xi[0, :], time[:, 0]),  # 原始网格的 1D 坐标
        Ey.T,                     # 原始数据
        method='linear',
        bounds_error=False,
        fill_value=0.0
    )

    T = Tau + Z / c  # 计算新的时间坐标
    Xi = Z - c * T
    Ey_new = interp((Xi, T))  # 插值到新网格
    return z_new, t_new, Ey_new