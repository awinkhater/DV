import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#1
url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/CONVENIENT_global_confirmed_cases.csv'
df=pd.read_csv(url)
df=df.dropna()
#2
df['China_sum'] = df.iloc[0:,57:90].astype(float).sum(axis=1)
#I have verified that the numbers are correct

#3
columns=df.columns
print(df.iloc[0:,249:260])
df['UK_sum'] = df.iloc[0:,249:260].astype(float).sum(axis=1)

#4
df['Country/Region'] = pd.to_datetime(df['Country/Region'])
df=df.set_index('Country/Region')

def covid_plot(Country):
    plt.figure()
    df.plot(y=['US'], legend=None)
    plt.xlabel('Date')
    plt.ylabel('Confirmed COVID19 Cases')
    plt.title(f'{Country} Confirmed COVID19 cases')
    plt.grid()
    plt.tight_layout()
    plt.show()

covid_plot('US')
#5
#print(df.columns.values)
df2=df[['Italy','UK_sum','China_sum','India','Brazil']]
df2.plot()
plt.xlabel('Date')
plt.ylabel('Confirmed COVID19 Cases')
plt.title(f'Global Confirmed COVID19 cases')
plt.grid()
plt.tight_layout()
plt.show()
#6

plt.figure()
df.hist(column='US')
plt.xlabel('Date')
plt.ylabel('Confirmed COVID19 Cases')
plt.title(f'US Confirmed COVID19 cases')
plt.grid()
plt.show()

#7
k=0
countries= ['China_sum','UK_sum','Italy','Brazil','India']
plt.figure(figsize=(10,8))
for i in range (len(countries)):
    plt.subplot(3, 2, i+1)
    plt.hist(df[countries[i]])
    plt.xlabel('Date')
    plt.ylabel('COVID19 Cases')
    plt.title(f'{countries[i]} COVID19 cases')
    plt.tight_layout()
    plt.grid()
plt.show()
#8
t_mean=None
tm=None
t_var=None
tv=None
t_med=None
tmd=None
for i in countries:
    if t_mean== None or t_mean < df[i].mean():
        t_mean=round(df[i].mean(),2)
        tm=i
    if t_med == None or t_med < df[i].median():
        t_med = round(df[i].median(),2)
        tmd = i
    if t_var == None or t_var < df[i].var():
        t_var = round(df[i].median(),2)
        tv = i
print(f"Top Mean:{tm}:{t_mean}", f"Top Median:{tmd}:{t_med}", f"Top Variance:{tv}:{t_var}")

print ("**********************")
#********* PART 2

#1
import seaborn as sns
TD = sns.load_dataset('titanic')
TD= TD.dropna()

print(TD.head(5))
#2

def pc1():
    sex2=TD.groupby('sex').size()
    myexplode = [0.02, 0.02]
    def absolute_value(val):
        a  = round(val/100.*sex2.sum())
        return a
    plt.pie(sex2, labels=['Female', 'Male'], autopct=absolute_value, explode=myexplode)
    plt.title("Pie Chart of Total People on the Titanic")
    plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc1()
plt.show()
#3
def pc2():
    sex2=TD.groupby('sex').size()
    def absolute_value(val):
        a  = np.round((val/100*sex2.sum())/sex2.sum(), 3)
        return (f"{100* a}%")
    myexplode = [0.02, 0.02]
    plt.pie(sex2, labels=['Female', 'Male'], autopct=absolute_value, explode= myexplode)
    plt.title("Pie Chart of Total People on the Titanic in %")
    plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc2()
plt.show()
#4
def pc3():
    TDM = TD[TD["sex"] =='male']
    surv2=TDM.groupby('survived').size()
    def absolute_value(val):
        a = np.round(100*(val/100*surv2.sum())/surv2.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02]
    plt.pie(surv2, labels=['Male Not Survived', 'Male Survived'], autopct=absolute_value, explode= myexplode)
    plt.title("Pie Chart of Survival Percentages of Male Passengers")
    plt.legend(bbox_to_anchor=(0.8, 0.9), loc='upper left', borderaxespad=0)
plt.figure()
pc3()
plt.show()
#5
def pc4():
    TDF = TD[TD["sex"] =='female']
    surv2=TDF.groupby('survived').size()
    def absolute_value(val):
        a = np.round(100*(val/100*surv2.sum())/surv2.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02]
    plt.pie(surv2, labels=['Female Not Survived', 'Female Survived'], autopct=absolute_value, explode= myexplode)
    plt.title("Pie Chart of Survival Percentages of Female Passengers")
    plt.legend(bbox_to_anchor=(0.8, 0.1), loc='lower left', borderaxespad=0)
plt.figure()
pc4()
plt.show()
#6

def pc5():
    pc2=TD.groupby('pclass').size()
    def absolute_value(val):
        a = np.round(100*(val/100*pc2.sum())/pc2.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02, 0.02]
    plt.pie(pc2, labels=['Class 1', 'Class 2', 'Class 3'], autopct=absolute_value, explode= myexplode)
    plt.title("Pie Chart of Passengers Percentage by Level")
    plt.legend(bbox_to_anchor=(1.00, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc5()
plt.show()
#7

def pc6():
    TDS = TD[TD["survived"] ==1]
    pc3=TDS.groupby('pclass').size()
    def absolute_value(val):
        a = np.round(100 * (val / 100 * pc3.sum()) / pc3.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02, 0.02]
    plt.pie(pc3, labels=['Class 1', 'Class 2', 'Class 3'], autopct=absolute_value, explode= myexplode)
    plt.title("Pie Chart of Surviving Passengers Percentage by Level")
    plt.legend(bbox_to_anchor=(1.00, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc6()
plt.show()

#8
def pc7():
    TPC1 = TD[TD["pclass"] ==1]
    TDS3=TPC1.groupby('survived').size()
    def absolute_value(val):
        a = np.round(100 * (val / 100 * TDS3.sum()) / TDS3.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02]
    plt.pie(TDS3, labels=['Death Rate', 'Survival'], autopct=absolute_value, explode= myexplode)
    plt.title("Survival & Death Rate: Class 1")
    plt.legend(bbox_to_anchor=(.9, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc7()
plt.show()
#9
def pc8():
    TPC2 = TD[TD["pclass"] ==2]
    TDS4=TPC2.groupby('survived').size()
    def absolute_value(val):
        a = np.round(100 * (val / 100 * TDS4.sum()) / TDS4.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02]
    plt.pie(TDS4, labels=['Death Rate', 'Survival'], autopct=absolute_value, explode= myexplode)
    plt.title("Survival & Death Rate: Class 2")
    plt.legend(bbox_to_anchor=(.9, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc8()
plt.show()

#10
def pc9():
    TPC2 = TD[TD["pclass"] ==3]
    TDS4=TPC2.groupby('survived').size()
    def absolute_value(val):
        a = np.round(100 * (val / 100 * TDS4.sum()) / TDS4.sum(), 1)
        return (f"{a}%")
    myexplode = [0.02, 0.02]
    plt.pie(TDS4, labels=['Death Rate', 'Survival'], autopct=absolute_value, explode= myexplode)
    plt.title("Survival & Death Rate: Class 3")
    plt.legend(bbox_to_anchor=(.9, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
pc9()
plt.show()
#11

plt.figure(figsize=(16,8))
plt.subplot(3,3,1)
pc1()
plt.subplot(3,3,2)
pc2()
plt.subplot(3,3,3)
pc3()
plt.subplot(3,3,4)
pc4()
plt.subplot(3,3,5)
pc5()
plt.subplot(3,3,6)
pc6()
plt.subplot(3,3,7)
pc7()
plt.subplot(3,3,8)
pc8()
plt.subplot(3,3,9)
pc9()
plt.tight_layout()
plt.show()

