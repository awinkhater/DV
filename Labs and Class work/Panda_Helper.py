#Quiz 1 Solutions
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import yfinance as yf
yf.pdr_override()
#======= Seaborn Load
df= sns.load_dataset('taxis')
#======   Yahoo Data Read
stocks=['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
start_date='2000-01-01'
end_date='2023-02-15'
df = data.get_data_yahoo(stocks[0], start=start_date, end=end_date)
#=====  Raw Dataset Read
url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/CONVENIENT_global_confirmed_cases.csv'
df=pd.read_csv(url)
df=df.dropna()
#==== rows and columns
obs, features= df.shape

print(f"There are {obs} observations, and {features} features")

#==== iloc example
#call row and column
df.iloc[0,1]
#First Column
df.iloc[:,0]
#First 5 Rows
df.iloc[0:5]
#First 2 columns and 2 rows
df.iloc[0:2, 0:2]
# 1st, 4th, 7th, 25th row + 1st 6th 7th columns
df.iloc[[0,3,6,24], [0,5,6]]
#========== loc examples
df.loc['Row Index Value'] # Out puts All column data
#Specfic Columns
df.loc[['Row Index Value'],['Desired Column 1', 'Desired Column B']]

#=== Null Count
print(df.isna().sum())
#add an extra .sum() for total missing values

#===== Null Percent
df1=df.copy()
column= df1.columns
a=df1.isna().sum()/len(df1)*100
#Percent of data that is missing
print(a)
#===== Drop Null
df1.dropna(inplace=True)
#========drop Columns with a null quantity greater than a percent
variable= []
for i in range (0, len(column)):
    if a[i]>=.20:
        variable.append(column[i])
df1.drop(variable, axis=1, inplace=True)
m1,n1=df1.shape

print(f"the new data set has {m1} rows and {n1} columns")

#================== Forward Fill
df.ffill(axis = 0)
#=============== Backward Fill
df.bfill(axis ='rows')

#==== Print Total Null Values
z=df1.isna().sum().sum()

print(f"there is {z} missing values")
#===== Mean of a column
a= round(df.total.mean(),2)
print(a)

#=========================== Reorder Columns
# shift column 'Name' to first position
first_column = df.pop('Name')

# insert column using insert(position,column_name,
# first_column) function
df.insert(0, 'Name', first_column)

#================ new column based on old column
df1['tip_percentage']=(df1.tip/df1.total)*100
#=========== Printing Groups of Dataframe
tip_zero=df1[df1['tip_percentage'].values==0]
tip_10_15 = df1[(df1['tip_percetange'].values>=10) & (df1['tip_percetange'].values<15)]
tip_15_20 = df1[(df1['tip_percetange'].values>=15) & (df1['tip_percetange'].values<20)]
tip_20 = df1[(df1['tip_percetange'].values>=20) ]
print(f'{100*(len(tip_zero)/len(df1)):.2f} % of passengers did not tip at all')
print(f'{100*(len(tip_10_15)/len(df1)):.2f} % of passengers tipped 10-15% of total')
print(f'{100*(len(tip_15_20)/len(df1)):.2f} % of passengers tipped 15-20% of total')
print(f'{100*(len(tip_20)/len(df1)):.2f} % of passengers tipped more than 20% of total')
print(f'Majority of passengers tipped  15-20% of total')

#========= Making a correlation plot of select columns
df2 = df1[['distance', 'fare','tip']]
corr = df2.corr()
print(corr)
print('*'*50)
print('*'*50)
print(f'The correlation coefficient between the tip & distance is {corr.iloc[0,2]:.2f} ')
print(f'The correlation coefficient between the tip & fare is {corr.iloc[1,2]:.2f} ')
print(f'The fare amount has the highest correlation coefficient with distance r = {corr.iloc[0,1]:.2f} ')

#====== Plotting a histogram of two variables
plt.figure()
df1['total'].hist(bins=50, label = 'total')
df1['tip'].hist(bins=50, label = 'tip')
plt.xlabel('USD($)')
plt.ylabel('Frequency')
plt.title('Histogram plot of Tip and Total')
plt.legend()
plt.grid()
plt.show()

#======== Mode of a dataframe
df.mode(numeric_only=True)

#==== median of a dataframe
df['grade'].median()

#=====variance of a dataframe
df.var()
#== standard deviation of a dataframe
df.std()
#==== skewness
scipy.stats.skew(a, axis=0, bias=True, nan_policy='propagate', *, keepdims=False)
#====== covariance matrix
df.cov()
#==== creating a df column with if the logic
df[’bucket’] = np.where(df[’total bill’]<10, ’Low’, ’High’)
#==== just drop a column
df.drop([’new bill’], axis = 1, inplace=True)
#======== adding a column to a specific location
df.insert(7,’ID ’, ’Tips Dataset’)
#==============Unique values
df.column.unique()
#==== drop a row
index = np.arange(0,11)
df6 = df.drop(index)
#===== Replacing nulls with mean of the column
df9[’total bill 2’].fillna(value=df[’total bill 2’].mean(), inplace= True)
#============= Replacing null with median of column
df9[’tip’].fillna(value=df[’tip’].median(), inplace= True)
t_stat, p_value = ttest_1samp(sample, popmean=155)
#====== t-test
import researchpy as rp
import scipy.stats as stats
rp.ttest(group1= df['bp_after'][df['sex'] == 'Male'], group1_name= "Male",
         group2= df['bp_after'][df['sex'] == 'Female'], group2_name= "Female")
#