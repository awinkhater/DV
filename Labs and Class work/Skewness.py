import numpy as np

class skewness:
    def __init__(self, data, order):
        self.data= np.array(data)
        self.order= order
    def sk_ew (self):
        N=len(self.data)
        m_i= (1/N) *np.sum((self.data- np.mean(self.data))**self.order)
        return m_i