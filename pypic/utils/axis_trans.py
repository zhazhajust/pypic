from numba import njit, prange
from numpy import interp

@njit(parallel=False)
def interp_data(data, axis_1, time, dx, dt, ret_times, total_axis, ret_data):
    for idx in range(data.shape[0]):
        #print(idx, data.shape[0], axis_1)
        x1 = interp(idx, [0, data.shape[0]], axis_1)
        ret_t = time - x1
        idx_x = round((x1 - total_axis[0])/dx)
        #print(x1, ret_axis[0], idx_x)
        idx_t = round((ret_t - ret_times[0])/dt)
        #print(ret_t, idx_t, idx_x)
        ret_data[idx_t, idx_x] = data[idx]