#Quiz
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#1
df=sns.load_dataset('taxis')

# print("there are", len(df),"observations inside the raw dataset")
# print("there are", 14 ,"observations inside the raw dataset")
#print(df.describe)
#2
null_drop_point= round(0.002* len(df),2)
print("Drop Columns that have more than", null_drop_point, "nulls")
print(df.isna().sum())
rlist=["payment", "pickup_zone", "dropoff_zone", "pickup_borough", "dropoff_borough"]
df2=df.drop('payment', axis=1)
df2=df2.drop('pickup_zone', axis=1)
df2=df2.drop('dropoff_zone', axis=1)
df2=df2.drop('pickup_borough', axis=1)
df2=df2.drop('dropoff_borough', axis=1)

print("The cleaned dataset has ", len(df2), "of observations")
print("the cleaned has", 9, "columns")

print("The list of removed columns are", rlist )

#4
print(df2.isna().sum())

m_tot=df2['total'].mean()
m_tip=df2['tip'].mean()
v_tot=df2['total'].var()
v_tip=df2['tip'].var()

#5
print("mean of total is", round(m_tot,2))
print("mean of total is", round(m_tip,2))
print("variance of total is", round(v_tot,2))
print("variance of total is", round(v_tip,2))

#6

df2['tip_percentage']= (df2['tip']/df2['total'])

x=df2['tip_percentage'].mean()

print("The majority of passnegers tipped",round(x,2),"% of the total")

#7
plt.figure()
plt.hist(df['tip_percentage'])
plt.hist()
#Unfinished