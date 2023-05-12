#Quiz 1 Solutions
import matplotlib as plt
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import yfinance as yf
import numpy as np
yf.pdr_override()



#used for bar and pie


label = [ 'C', 'C++', 'Java', 'Python', 'Rust']
data= [23, 17, 35, 29, 12]
#Sorted Bar Plot ==============================================
DF1= pd.DataFrame(np.array(data).reshape(1,5), columns=label)
DF1.loc['score']=data
DF1_sorted=DF1.T.sort_values('score')

plt.figure()
plt.bar(DF1_sorted.index,DF1_sorted['score'])
plt.ylabel('Score')
plt.xlabel('Lang Name')
plt.title('Simple Plot')
plt.show()
#See notes


# explode = (0.03, 0.03, 0.3, 0.03, 0.03)
# fig, ax = plt.subplots(1,1)
# ax.pie(data, labels = label, explode= explode, autopct= '%1.2f%%', shadow= False )
# ax.set_title('Grade % in each subject')
# ax.axis=('square')
# ax.legend(loc = (.95, .8))
# plt.show()



#=====================
# url= 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/mnist_test.csv'
# df=pd.read_csv(url)
#
# #print(df.shape)
# df_x= df.iloc[:,1:]
# plt.imshow(df_x.iloc[0,:].values.reshape(28,28))
# #plt.show()
#
#
#
# df_4= df[df['label']==4]
# #df_4= df_4.iloc[:,1:]
# for i in range (1,5):
#     plt.subplot(2,2,i)
#     plt.imshow(df_4.iloc[0,1:].values.reshape(28,28))
# plt.show()

# df_5 = df[df['label']==5]
# plt.figure(figsize=(16,16))
# for i in range (1,101):
#     plt.subplot(10,10,i)
#     plt.imshow(df_5.iloc[i,1:].values.reshape(28,28))
# plt.tight_layout()
# plt.show()
# stocks=['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
#
# start_date='2000-01-01'
# end_date='2023-02-22'
# df = data.get_data_yahoo(stocks, start=start_date, end=end_date)
#
# #Turn into a general function ?
# k=0
# plt.figure(figsize= (16,8))
# for i in stocks:
#     k+=1
#     df=data.get_data_yahoo(i,start=start_date, end=end_date)
#     plt.subplot (3,2,k)
#     plt.plot(df['Close'])
#     plt.grid()
#     plt.title(f'closing price {i}')
# plt.tight_layout()
# plt.show()


