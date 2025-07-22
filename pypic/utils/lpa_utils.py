import numpy as np

def calculate_emittance_spot(ux, uy, x, y):
    """
    通过发射度计算理论最小焦斑
    
    参数:
        ux, uy: 归一化横向动量 (px/p0, py/p0)
        x, y: 横向位置 (m)
    
    返回:
        (sigma_x_min, sigma_y_min, emittance_x, emittance_y)
    """
    # 计算发射度 (几何发射度)
    emittance_x = np.sqrt(np.mean(x**2)*np.mean(ux**2) - np.mean(x*ux)**2)
    emittance_y = np.sqrt(np.mean(y**2)*np.mean(uy**2) - np.mean(y*uy)**2)
    
    # 最小焦斑（在聚焦点β=β*，α=0）
    beta_x = np.mean(x**2) / emittance_x
    beta_y = np.mean(y**2) / emittance_y
    
    sigma_x_min = np.sqrt(emittance_x * beta_x)
    sigma_y_min = np.sqrt(emittance_y * beta_y)
    
    return sigma_x_min, sigma_y_min, emittance_x, emittance_y

# lpa_utils.py

import numpy as np
from sklearn.cluster import KMeans

def extract_accelerated_electrons(x, y, z, ux, uy, uz, features=None, n_clusters=2):
    """
    使用 K-means 聚类从 PIC 模拟粒子数据中提取加速电子。

    参数:
        x, y, z, ux, uy, uz : np.ndarray
            粒子位置和动量数组，长度应一致
        features : np.ndarray (N, M) 或 None
            要用于聚类的特征数组（如 uz 或多维动量）。如果为 None，则默认使用 uz。
        n_clusters : int
            聚类簇数，默认 2

    返回:
        dict，包含加速电子的各字段数组和聚类信息
    """
    assert len(x) == len(ux), "输入数组长度不一致"

    if features is None:
        features = np.column_stack((uz,))
    else:
        assert features.shape[0] == len(x), "features 行数必须等于粒子数"
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    labels = kmeans.fit_predict(features)
    centroids = kmeans.cluster_centers_.squeeze()

    # 选择聚类中心最大值对应的簇作为加速电子
    if centroids.ndim > 0:
        accelerated_label = np.argmax(np.linalg.norm(centroids, axis=-1))
    else:
        accelerated_label = np.argmax(centroids)

    accelerated_indices = np.where(labels == accelerated_label)[0]

    return {
        'indices': accelerated_indices,
        'x': x[accelerated_indices],
        'y': y[accelerated_indices],
        'z': z[accelerated_indices],
        'ux': ux[accelerated_indices],
        'uy': uy[accelerated_indices],
        'uz': uz[accelerated_indices],
        'labels': labels,
        'centroids': centroids
    }
