import numpy as np
from scipy.signal import hilbert

def get_stokes_vector(Ex, Ey, if_normalize=True):

    E_x = np.conj(hilbert(Ex, axis = 0))
    E_y = np.conj(hilbert(Ey, axis = 0))

    # 总光强 I
    I = np.mean(np.real(E_x)**2, axis=0) + np.mean(np.real(E_y)**2, axis=0)

    # 偏振分量 Q
    Q = np.mean(np.real(E_x)**2, axis=0) - np.mean(np.real(E_y)**2, axis=0)

    # 计算偏振分量 U
    E_a = (E_x + E_y) / np.sqrt(2)
    E_b = (E_y - E_x) / np.sqrt(2)
    U = np.mean(np.real(E_a)**2, axis=0) - np.mean(np.real(E_b)**2, axis=0)

    # 计算圆偏振分量 V
    E_r = (E_x + 1j * E_y) / np.sqrt(2)
    E_l = (E_x - 1j * E_y) / np.sqrt(2)
    V = np.mean(np.real(E_r)**2, axis=0) - np.mean(np.real(E_l)**2, axis=0)

    # 归一化
    stokes_vector = np.array([I, Q, U, V])
    if if_normalize:
        stokes_vector /= stokes_vector[0]
    
    return stokes_vector

def get_ellipse(stokes_vector):
    I, Q, U, V = stokes_vector
    # Calculate psi and chi
    psi = 0.5 * np.arctan2(U, Q)
    chi = 0.5 * np.arcsin(V/I)
    return np.array([psi, chi])

def get_polarization_degree(I, Q, U, V):
    p = np.sqrt(Q**2 + U**2 + V**2) / I
    return p

def get_skyrmion_number(stokes):
    # 假设 stokes_vectors 是一个形状为 (200, 200, 3) 的 numpy 数组，表示你的 Stokes 矢量场
    # 这里你可以替换为你的实际数据
    # stokes_vectors = np.random.rand(200, 200, 3)
    # stokes_vectors = stokes.transpose(2, 1, 0)
    stokes_vectors = np.array([stokes[1], stokes[2], stokes[3]]).transpose(2, 1, 0)

    # 1. 规范化 Stokes 矢量场
    norm = np.linalg.norm(stokes_vectors, axis=2, keepdims=True)
    stokes_vectors_normalized = stokes_vectors / norm

    # 2. 使用 np.gradient 计算偏导数
    # np.gradient 会计算每个分量在 x 和 y 方向的偏导数
    dS_dx = np.gradient(stokes_vectors_normalized, axis=0)  # 对 x 方向的偏导数
    dS_dy = np.gradient(stokes_vectors_normalized, axis=1)  # 对 y 方向的偏导数

    # 3. 计算交叉乘积
    cross_product = np.cross(dS_dx, dS_dy)

    # 计算斯格明子数密度
    skyrmion_density = np.einsum('ijk,ijk->ij', stokes_vectors_normalized, cross_product)

    # 4. 计算斯格明子数 Q
    Q = np.sum(skyrmion_density) / (4 * np.pi)

    print("Skyrmion number Q:", Q)
    return Q
