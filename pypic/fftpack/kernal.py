from numpy import sqrt, ndarray, pi, exp, sum, power
from numba import njit

def pdf(x,mu,sigma,n): 
    #mu 平均值，sigma:标准差
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**n/(2*sigma**2))

@njit
def gaussian_kernal(data: ndarray, res: ndarray, sigma: ndarray, order: float = 2):
    m, n = data.shape
    mu0 = 0
    sigma0 = 1
    for i in range(m):
        for j in range(n):
            r = sqrt(((i - m/2)/sigma[1])**2 + ((j - n/2)/sigma[0])**2)
            #res[i, j] = 1/(sigma0*sqrt(2*pi))*exp(-(r-mu0)**2/(2*sigma0**2))
            res[i, j] = 1/(sigma0*sqrt(2*pi))*exp(-1/2*power(r-mu0/sigma0, order))
    res /= sum(res)
    return