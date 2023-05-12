import numpy as np
import pandas as pd
def corr_coeff (x,y):
    '''
    :param x: an array of n numbers
    :param y: an array of n numbers
    :return: the correlation between x and y
    num is the numerator
    denx is the x side of the denominator in the sqrt
    deny is the y side of the denominator in the sqrt
    den is the final denominator post sqrt
    '''

    num=0
    denx=0
    deny=0

    x_b= np.mean(x)
    y_b= np.mean(y)
    for i in range (0, len(x)):
        num+= (x[i]-x_b)*(y[i]-y_b)
        dx= (x[i]-x_b)
        dy= (y[i]-y_b)
        denx+=np.power(dx,2 )
        deny+=np.power(dy, 2 )
    total= num/(np.sqrt((denx)*(deny)))
    return (total)


class skewness:
    def __init__(self, data, order):
        self.data= np.array(data)
        self.order= order
    def sk_ew (self):
        N=len(self.data)
        m_i= (1/N) *np.sum((self.data- np.mean(self.data))**self.order)
        return m_i

def stockmvc_ptformat(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of mean values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Volume', 'Adj Close'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.mean().values.tolist())
        tdf.loc[len(tdf)] = list
    list2=['Maximum Value']
    list2= list2 +(tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3=['Minimum Value']
    list3= list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    return(tdf)