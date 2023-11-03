from numpy import pi

#####constants#####

class Constants(object):
    def __init__(self, lambda_L = 0.8):
        wavelength = 2 * pi
        c = 1
        self.lambda_L = lambda_L
        self.um = wavelength/lambda_L
        self.fs = 0.3 * self.um/c
        return
    
__all__ = ['Constants']