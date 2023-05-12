import pandas as pd
from pandas_datareader import data
import yfinance as yf
from prettytable import PrettyTable
yf.pdr_override()

#If you want to add another stock add it here and run this code. It should appear in all the tables!
stocks=['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']

start_date='2000-01-01'
end_date='2023-02-14'



#2
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


stock_PT1(stocks,stock_mean_frame1,"Mean Value Compairison")
#3
def stock_Var_frame1(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of variance values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.var().values.tolist())
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

stock_PT1(stocks,stock_Var_frame1, "Variance Comparison")

#4
def stocks_SD_frame1 (stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of variance values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.std().values.tolist())
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

stock_PT1(stocks, stocks_SD_frame1, "Standard Deviation Compairison")
#5
def stocks_Med_frame1(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of variance values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.median().values.tolist())
        tdf.loc[len(tdf)] = list
    list2=['Maximum Value']
    list2= list2 +(tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3=['Minimum Value']
    list3= list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    tdf = tdf.set_index('Name')
    return(tdf)


stock_PT1(stocks,stocks_Med_frame1 ,"Median Value Compairison")


def stocks_mean_frame2(stocklist):
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
    tdf.set_index('Name')
    list2=['Maximum Value']
    list2= list2 +(tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3=['Minimum Value']
    list3= list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    tdf= tdf.set_index('Name')
    list4=['Company Name-Maximum']
    list4= list4+(tdf.idxmax().values.tolist())
    list5 = ['Company Name-Minimum']
    list5 = list5 + (tdf.idxmin().values.tolist())
    tdf.reset_index(drop=False, inplace=True)
    tdf.loc[len(tdf)] = list4
    tdf.loc[len(tdf)] = list5
    return(tdf)


stock_PT1(stocks, stocks_mean_frame2 ,"Mean Value Compairison")

#7

def stocks_Var_frame2(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of mean values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.var().values.tolist())
        tdf.loc[len(tdf)] = list
    tdf.set_index('Name')
    list2=['Maximum Value']
    list2= list2 +(tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3=['Minimum Value']
    list3= list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    tdf= tdf.set_index('Name')
    list4=['Company Name-Maximum']
    list4= list4+(tdf.idxmax().values.tolist())
    list5 = ['Company Name-Minimum']
    list5 = list5 + (tdf.idxmin().values.tolist())
    tdf.reset_index(drop=False, inplace=True)
    tdf.loc[len(tdf)] = list4
    tdf.loc[len(tdf)] = list5
    return(tdf)

stock_PT1(stocks,stocks_Var_frame2,"Variance Comparison")
#8
def stock_SD_frame2(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of mean values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list=[stocklist[i]]
        list= list+(df.std().values.tolist())
        tdf.loc[len(tdf)] = list
    tdf.set_index('Name')
    list2=['Maximum Value']
    list2= list2 +(tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3=['Minimum Value']
    list3= list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    tdf= tdf.set_index('Name')
    list4=['Company Name-Maximum']
    list4= list4+(tdf.idxmax().values.tolist())
    list5 = ['Company Name-Minimum']
    list5 = list5 + (tdf.idxmin().values.tolist())
    tdf.reset_index(drop=False, inplace=True)
    tdf.loc[len(tdf)] = list4
    tdf.loc[len(tdf)] = list5
    return(tdf)

stock_PT1(stocks,stock_SD_frame2, "Standard Deviation Compairison")
 #9
def stocks_Med2_frame2(stocklist):
    '''

    :param stocklist: This is a list of stocks for the yahoo api
    :return: A dataframe of mean values ready to be fed into the pretty table function
    '''
    tdf= pd.DataFrame(columns=['Name','High($)','Low($)','Open($)','Close($)', 'Adj Close($)', 'Volume'])

    for i in range(len(stocklist)):
        df = data.get_data_yahoo(stocklist[i], start=start_date, end=end_date)
        list = [stocklist[i]]
        list = list + (df.median().values.tolist())
        tdf.loc[len(tdf)] = list
    list2 = ['Maximum Value']
    list2 = list2 + (tdf.max().values.tolist())
    list2.pop(1)
    tdf.loc[len(tdf)] = list2
    list3 = ['Minimum Value']
    list3 = list3 + (tdf.min().values.tolist())
    list3.pop(1)
    tdf.loc[len(tdf)] = list3
    tdf = tdf.set_index('Name')
    list4 = ['Company Name-Maximum']
    list4 = list4 + (tdf.idxmax().values.tolist())
    list5 = ['Company Name-Minimum']
    list5 = list5 + (tdf.idxmin().values.tolist())
    tdf.reset_index(drop=False, inplace=True)
    tdf.loc[len(tdf)] = list4
    tdf.loc[len(tdf)] = list5
    return (tdf)

stock_PT1(stocks,stocks_Med2_frame2 ,"Median Value Compairison")
#10
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