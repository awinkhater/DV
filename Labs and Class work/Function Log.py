import numpy as np
import matplotlib as plt
import seaborn as sns
import pandas as pd
from pandas_datareader import data
import yfinance as yf
from prettytable import PrettyTable
yf.pdr_override()
import scipy.stats
#Simple correlation coefficent
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

#================= Stock mean and pretty table
def stock_mean_frame1(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of mean values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

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


def stock_PT1(stocklist, func, title):
    df= func(stocklist)
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = df.columns
        x.float_format='.2'
    print(x.get_string)

#====== t test for correlation
def corr_t(D,a,b, alpha):
    '''
    :param D: a data frame
    :param a: an array of numbers or dataframe array
    :param b: an array of numbers or a dataframe column
    :return:
    '''
    n=len(D)
    r = corr_coeff(a,b)
    t_0= (r*((n-2)**0.5))/((1-(r**2))**0.5)
    p=scipy.stats.t.sf((t_0), n-3)
    if p < alpha:
        return("p=",p,"The correlation is significant, reject the null hypothesis")
    else:
        return("p=",p,"The correlation is not siginficant, fail to reject.")

#================ Partial correlation with a t test option
def parr_corr_t (D, h,g,w,alpha, t):
    '''

    :param D: A dataframe
    :param h: A column of dataframe
    :param g: A column of dataframe. A confounding variable to be excluded
    :param w: A column of dataframe
    :param alpha: the p-value threshold
    :return:
    '''

    r_hw = corr_coeff(h,w)
    r_gw = corr_coeff(g,w)
    r_gh = corr_coeff(g,h)

    r_hw_g= round((r_hw -r_gh * r_gw)/((1-r_gw**2)**(0.5)*(1-r_gh**2)**(0.5)),2)
    n= len(D)
    k = 1
    if t==1:
#t-test:
        t_0= r_hw_g*((n-2-k)/(1-r_hw_g**2))**0.5

        p = ((scipy.stats.t.sf(t_0, n - 3)))
        if abs(p) < alpha:
            return ("Parital Correlation=", r_hw_g, "p=", p, "The correlation is significant, reject the null hypothesis")
        else:
            return ("Parital Correlation=", r_hw_g, "p=", p, "The correlation is not siginficant, fail to reject.")
    else:
        return(r_hw_g)

#============ Correlation Table
def corr_PT1(D,a,b,c, title):
    df= corr_table_prep(D,a,b,c)
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = df.columns
        x.float_format='.2'
    print(x.get_string)

corr_PT1(df, df['AdBudget'], df['Sales'], df['GDP'], "Correlation Comparison Table")
 #===== t-test
from scipy import stats
stats.ttest_ind(rvs1, rvs2, equal_var=False)
