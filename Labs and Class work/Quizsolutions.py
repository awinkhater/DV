#Quiz 1 Solutions
#Also availible on 2/22 lecture notes (class 6)
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 #1
df= sns.load_dataset('taxis')
#2
obs, features= df.shape

print(f"There are {obs} observations, and {features} features")

#3
print(df.isna().sum())
#add an extra .sum() for total missing values

df1=df.copy()
column= df1.columns
a=df1.isna().sum()/len(df1)*100
#Percent of data that is missing
print(a)

#dropping stuff
variable= []
for i in range (0, len(column)):
    if a[i]>=.20:
        variable.append(column[i])
df1.drop(variable, axis=1, inplace=True)
m1,n1=df1.shape
#4

print(f"the new data set has {m1} rows and {n1} columns")


z=df1.isna().sum().sum()

print(f"there is {z} missing values")
#5
a= round(df.total.mean(),2)
print(a)

print (f"The mean of total is {np.round(df1['total'].mean(),2)} $")
print (f"the variance of total is {np.round(df1['total'].var(),2)}$ ")

#6.
#new column, Wow you did it right
df1['tip_percentage']=(df1.tip/df1.total)*100
tip_zero=df1[df1['tip_percentage'].values==0]
tip_zero=df1[df1['tip_percentage'].values>= 10]
#continue onwards,See his code

print(f'{100*(len(tip_zero)/len(df1)):2f} & of passengers did not tip at all')
#7

#His code:
df = sns.load_dataset('taxis')
obser, feature = df.shape
print(f'There are {obser} observations inside the raw dataset')
print(f'There are {feature} features[columns] inside the raw dataset')

print(df.isna().sum())
print(f'The total number of missing observations are {df.isna().sum().sum()}')

df1 = df.copy()
col = df.columns
a = df.isna().sum()/len(df)*100
print(a)

variable = []
for i in range(0,len(col)):
    if a[i]>=.20:
        variable.append(col[i])

df1.drop(variable, axis=1, inplace=True)
m1,n1 = df1.shape
print(f'There are {obser} observations and {feature} # of features inside the raw dataset' )
print(f'There are {m1} observations and {n1} # of features inside the cleaned dataset' )
print(f'The list of removed columns are {variable}' )

z = df1.isna().sum().sum()
if z==0:
    print(f'The dataset has {z} # of missing values')
else:
    print(f'The dataset has {z} # of missing values')

print(f'The mean of the total is  {df1.total.mean():.2f} $' )
print(f'The mean of the tip is  {df1.tip.mean():.2f} $' )
print(f'The variance of the total is  {df1.total.var():.2f} $' )
print(f'The variance of the tip is  {df1.tip.var():.2f} $' )

df1['tip_percetange'] = (df1.tip/df.total)*100
tip_zero = df1[df1['tip_percetange'].values==0]
tip_10_15 = df1[(df1['tip_percetange'].values>=10) & (df1['tip_percetange'].values<15)]
tip_15_20 = df1[(df1['tip_percetange'].values>=15) & (df1['tip_percetange'].values<20)]
tip_20 = df1[(df1['tip_percetange'].values>=20) ]

print('*'*50)
print('*'*50)

print(f'{100*(len(tip_zero)/len(df1)):.2f} % of passengers did not tip at all')
print(f'{100*(len(tip_10_15)/len(df1)):.2f} % of passengers tipped 10-15% of total')
print(f'{100*(len(tip_15_20)/len(df1)):.2f} % of passengers tipped 15-20% of total')
print(f'{100*(len(tip_20)/len(df1)):.2f} % of passengers tipped more than 20% of total')
print(f'Majority of passengers tipped  15-20% of total')

df2 = df1[['distance', 'fare','tip']]
corr = df2.corr()
print(corr)
print('*'*50)
print('*'*50)
print(f'The correlation coefficient between the tip & distance is {corr.iloc[0,2]:.2f} ')
print(f'The correlation coefficient between the tip & fare is {corr.iloc[1,2]:.2f} ')
print(f'The fare amount has the highest correlation coefficient with distance r = {corr.iloc[0,1]:.2f} ')


plt.figure()
df1['total'].hist(bins=50, label = 'total')
df1['tip'].hist(bins=50, label = 'tip')
plt.xlabel('USD($)')
plt.ylabel('Frequency')
plt.title('Histogram plot of Tip and Total')
plt.legend()
plt.grid()
plt.show()