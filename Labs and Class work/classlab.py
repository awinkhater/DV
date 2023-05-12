# This is a sample Python script.fr
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Toolbox import corr_coeff
from pandas_datareader import data
import seaborn as sns
from Skewness import skewness
from prettytable import PrettyTable
from scipy import stats
# # def change(x):
# #     if x== 'Male':
# #         return 1
# #     else:
# #         return 2
#
# # df=sns.load_dataset('titanic')
# # #print(df.describe())
# # #hunt for missing values
# # print(df.isna().sum())
# # #drop
# # #df.dropna()
# #a1,b1=df
#
# url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/autos.clean.csv'
# df=pd.read_csv(url)
#
# feature = df.columns
# drive_wheel = df['drive-wheels']
# print(df.head())
# #=====
# #one-hot encoding
# #=====
# df1=pd.get_dummies(df, columns=['num-of-doors', 'drive-wheels','fuel-type'])
# #===
# #Label Encoding
# #===
# df3=df.copy()
# df3['body-style']=df3['body-style'].astype('category')
# df3['body-style-num']= df3['body-style'].cat.codes
# #===
# #Want to df with only two columns: body-style and body-style-num
# col_interest = ['body-style','body-style-num']
# df4=df3[col_interest]
# #=======
# #We want a df with a body style col and body style um is next to each ohter
# #=====
# df5= df.copy()
# df5.insert(7,'body-style-num', df3['body-style-num'])

#==
#data cleaning
import seaborn as sns
# pd.set_option('display.precision',2)
# df=sns.load_dataset('taxis')
#
# df['payment'].fillna(df['payment'].mode()[0], inplace=True)
#
# #Forward method
# # df1=pd.DataFrame(
# #     {'A':[np.nan,1,2,3, np.nan,np.nan],
# #      'B':[11,5,np.nan,np.nan,np.nan,8],
# #      'C':[np.nan,5,10,11,np.nan,8]}
# # )
# # #print(df1.head())
# #
# # df2=df1.copy()
# # df3=df1.copy()
# # df4=df1.copy()
# # df5=df1.copy()
# #
# # df2.fillna(axis='rows',method='bfill',inplace=True)
# #
# # df3.fillna(axis='columns', method='ffill', inplace=True)
#
# df.fillna(axis='rows', method='ffill', inplace=True)
# #print(df.isna().sum())
#
# #select columns, first 5 cols and last 1000 rows
# df10=df.iloc[-1000:, :5]
# # #print(df10.tail(5))
# #-====
# # #New data frame
# url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/stock%20prices.csv'
# df=pd.read_csv(url)
# #
#
# df2=df[df['symbol']=='GOOGL']
# df3=df2[df2['date']>='2015-01-01']
#
# date=pd.date_range(df2.iloc[0,1],df2.iloc[754,1],periods=len(df2))
# df2.index= date
# import matplotlib.pyplot as plt
#
# plt.figure()
# col=df2.columns
# df2[col[:-1]].plot()
# plt.grid()
# plt.tight_layout()
# plt.show()