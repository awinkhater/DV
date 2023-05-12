import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import yfinance as yf
yf.pdr_override()
#1
stocks=['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']

start_date='2000-01-01'
end_date='2023-02-15'
df = data.get_data_yahoo(stocks[0], start=start_date, end=end_date)
#2
def stock_plot(col, C):
    k = 0
    plt.figure(figsize= (16,8))
    for i in stocks:
        if col== 'Volume':
            k +=1
            df=data.get_data_yahoo(i,start=start_date, end=end_date)
            plt.subplot (3,2,k)
            plt.plot(df[col], color= C, label=f'{col}')
            #This hides the scientific notation
            plt.ticklabel_format(style='plain', axis='y')
            plt.ylabel(f"{col} Shares")
            plt.xlabel('Date')
            plt.legend()
            plt.grid()
            plt.title(f'{col} {i}')
        else:
            k += 1
            df = data.get_data_yahoo(i, start=start_date, end=end_date)
            plt.subplot(3, 2, k)
            plt.plot(df[col], color=C, label=f'{col}')
            plt.ylabel(f"{col} USD ($)")
            plt.xlabel('Date')
            plt.legend()
            plt.grid()
            plt.title(f'{col} {i}')
    plt.tight_layout()

    plt.show()

stock_plot('High', 'b')
#3
stock_plot('Low', 'r')
stock_plot('Open', 'g')
stock_plot('Close', 'c')
stock_plot('Volume', 'k')
stock_plot('Adj Close', 'm')

#4
def stock_hist(col, C):
    k = 0
    plt.figure(figsize= (16,8))
    for i in stocks:
        if col== 'Volume':
            k +=1
            df=data.get_data_yahoo(i,start=start_date, end=end_date)
            plt.subplot (3,2,k)
            plt.hist(df[col], bins=50, color=C, label=f'{col}')
            plt.ylabel(f"{col} Shares")
            plt.xlabel('Date')
            plt.grid()
            plt.title(f'{col} {i}')
        else:
            k += 1
            df = data.get_data_yahoo(i, start=start_date, end=end_date)
            plt.subplot(3, 2, k)
            plt.hist(df[col], bins=50, color=C, label=f'{col}')
            plt.ylabel(f"{col} USD ($)")
            plt.xlabel('Date')
            plt.grid()
            plt.title(f'{col} {i}')
    plt.tight_layout()

    plt.show()

stock_hist('High', 'b')
#5
stock_hist('Low','r')
stock_hist('Open','g')
stock_hist('Close','c')
stock_hist('Volume','k')
stock_hist('Adj Close','m')

#6
def table_pretty(df,title):
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = df.columns
        x.float_format='.2'
    print(x.get_string)
def stock_corr(stocklist, stock):
    for i in range( len(stocklist)):
        if stocklist[i]== stock:
            df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
            df.reset_index(drop=True, inplace=True)
            C= df.corr(method='pearson')

    table_pretty(C, "Stock Correlation Matrix")

print(stock_corr(stocks, 'AAPL'))
#7
print(stock_corr(stocks, 'AAPL'))
print(stock_corr(stocks, 'ORCL'))
print(stock_corr(stocks, 'TSLA'))
print(stock_corr(stocks, 'IBM'))
print(stock_corr(stocks, 'YELP'))
print(stock_corr(stocks, 'MSFT'))
#8
def corr_coeff(x,y):
    '''
    :param x: an array of numbers
    :param y: an array of numbers
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
    total= round(num/(np.sqrt((denx)*(deny))),2)
    return(total)

def stock_sm(stock, C):
    k=0
    L= len(stocks)
    AL=['High', 'Low', 'Open' , 'Close','Volume', 'Adj Close']
    plt.figure(figsize=(16, 16))
    df = data.get_data_yahoo(stocks, start=start_date, end=end_date)
    df=df.dropna()
    row=0
    col=0
    for j in AL:
        col=0
        row= row+1
        for i in AL:
            col= col+1
            k += 1
            if row < col:
                I = df[i][stock]
                J=df[j][stock]
                plt.subplot(L, L, k)
                plt.scatter(I, J, color=C, label=f'{i} & {j}')
                plt.ylabel(f"{i} USD$")
                plt.xlabel(f'{j} USD$')
                plt.grid()
                plt.title(f'r={corr_coeff(J, I)}')
            else:
                I = df[i][stock]
                J = df[j][stock]
                plt.subplot(L, L, k)
                plt.scatter(J, I, color=C, label=f'{j} & {i}')
                plt.ylabel(f"{j} USD$")
                plt.xlabel(f'{i} USD$')
                plt.grid()
                plt.title(f'r={corr_coeff(J, I)}')

    plt.tight_layout()

    plt.show()

stock_sm('AAPL', 'b')

#9
stock_sm('ORCL', 'r')
stock_sm('TSLA', 'k')
stock_sm('MSFT', 'g')
stock_sm('IBM', 'c')
stock_sm('YELP', 'm')

#10
Df = data.get_data_yahoo(stocks[0], start=start_date, end=end_date)
plt.figure(figsize=(16,16))
pd.plotting.scatter_matrix(Df, hist_kwds= {'bins': 50} , alpha = 0.5, s = 10, diagonal = 'kde')
plt.ticklabel_format(style='plain')
plt.tight_layout()
plt.show()