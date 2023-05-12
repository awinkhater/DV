import numpy as np
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

#1
url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/mnist_test.csv'
df=pd.read_csv(url)
df = pd.read_csv(url)

plt.figure(figsize=(12,12))
for i in range(0,100):
    plt.subplot(10,10,i+1)
    plt.imshow(df.iloc[i,1:].values.reshape(28,28))
plt.tight_layout()
plt.show()
#1B

plt.figure(figsize=(12,12))
k=0
for j in range (1, 101):

    if j <=10: df1 = df[df['label'] == 0]
    elif j <=20: df1 = df[df['label'] == 1]
    elif j <= 30:df1 = df[df['label'] == 2]
    elif j <= 40:df1 = df[df['label'] == 3]
    elif j <= 50:df1 = df[df['label'] == 4]
    elif j <= 60:df1 = df[df['label'] == 5]
    elif j <= 70:df1 = df[df['label'] == 6]
    elif j <= 80:df1 = df[df['label'] == 7]
    elif j <= 90:df1 = df[df['label'] == 8]
    else:df1 = df[df['label'] == 9]
    plt.subplot(10,10,j)
    plt.imshow(df1.iloc[j,1:].values.reshape(28,28))
plt.tight_layout()
plt.show()

#2
df= sns.load_dataset('diamonds')
print(df.isna().sum())
df= df.dropna()
#3
from prettytable import PrettyTable
def PT1(df, title):
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = ['Cut','Index']
        x.float_format='.2'
    print(x.get_string)
cuts=df.cut.values.tolist()
C=[]

k=0
for i in cuts:
    if i not in C:
        k+=1
        C.append(i)

C=pd.DataFrame(C)
C['Index']=[1,2,3,4,5]

PT1(C, "Diamond Datse__Various Cuts")
4
def PT2(df, title):
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = ['Color Name','Index']
        x.float_format='.2'
    print(x.get_string)
cols=df.color.values.tolist()
C=[]

for i in cols:
    if i not in C:
        C.append(i)

C=pd.DataFrame(C)
C['Index']=[1,2,3,4,5,6,7]
PT2(C, "Diamond Dataset_ Various Colors")

#5
def PT3(df, title):
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = ['Clarity Name','Index']
        x.float_format='.2'
    print(x.get_string)
cols=df.clarity.values.tolist()
C=[]

for i in cols:
    if i not in C:
        C.append(i)

C=pd.DataFrame(C)
I=[]
for i in range (0, len(C)):
    I.append(i)
C['Index']=I
PT3(C, "Diamond Dataset_ Various Clarities")

#6
cols=df.cut.values.tolist()
C=[]

for i in cols:
    if i not in C:
        C.append(i)

CL=[]
for j in C:
    df1= df[df['cut']==j]
    print(df1)
    CL.append(len(df1))

print(CL)



plt.figure(figsize=(10,6))
plt.barh(C, CL)
plt.title('Horizontal Bar plot of Cuts')
plt.xlabel('Sales')
plt.ylabel('Cut')
plt.show()
print ("The diamond with the Ideal cut has a maximum sales per count")
print ("The diamond with the Fair cut has a minimum sales per count")

# #7
cols=df.color.values.tolist()
C=[]

for i in cols:
    if i not in C:
        C.append(i)

CL=[]
for j in C:
    df1= df[df['color']==j]
    CL.append(len(df1))

print(CL)



plt.figure(figsize=(10,6))
plt.barh(C, CL)
plt.title('Horizontal Bar plot of Colors')
plt.xlabel('Sales')
plt.ylabel('Color')
plt.show()
print ("The diamond with the G color has a maximum sales per count")
print ("The diamond with the J color has a minimum sales per count")
#8
cols=df.clarity.values.tolist()
C=[]

for i in cols:
    if i not in C:
        C.append(i)

CL=[]
for j in C:
    df1= df[df['clarity']==j]
    CL.append(len(df1))

print(CL)



plt.figure(figsize=(10,6))
plt.barh(C, CL)
plt.title('Horizontal Bar plot of Clarity')
plt.xlabel('Sales')
plt.ylabel('Clarity')
plt.show()
print ("The diamond with the Sl1 clarity has a maximum sales per count")
print ("The diamond with the Il clarity has a minimum sales per count")
#9
df2=df.groupby('cut').size()
myexplode = [0.03, 0.03, 0.03, 0.03, 0.03]
def absolute_value(val):
    a = np.round(100 * ((val / 100 * df2.sum()) / df2.sum()), 2)
    return f'{a} %'
plt.pie(df2, labels=C, autopct=absolute_value, explode=myexplode)
plt.title("Pie Chart of Diamond Cut Sales by %")
plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
plt.show()

print("The Diamond with Ideal Cut has the most Sales with 39.95% sales count")
print("The Diamond with Fair Cut has the most least with 2.98 % sales count")
# #10
df2=df.groupby('color').size()
myexplode = [0.03, 0.03, 0.03, 0.03, 0.03]
C=[]
cols = df.color.values.tolist()
for i in cols:
    if i not in C:
        C.append(i)
myexplode = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
def absolute_value(val):
    a  = np.round(100*((val/100*df2.sum())/df2.sum()),2)
    return f'{a} %'
plt.pie(df2, labels=C, autopct=absolute_value, explode=myexplode)
plt.title("Sales Count per Color ")
plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
plt.show()

print("The Diamond with H Color has the most Sales with 20.93 % sales count")
print("The Diamond with D Color has the most least with 5.21 % sales count")

#11

df2=df.groupby('clarity').size()
myexplode = [0.03, 0.03, 0.03, 0.03, 0.03]
C=[]
cols = df.clarity.values.tolist()
for i in cols:
    if i not in C:
        C.append(i)
myexplode = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
def absolute_value(val):
    a  = np.round(100*((val/100*df2.sum())/df2.sum()),2)
    return f'{a} %'
plt.pie(df2, labels=C, autopct=absolute_value, explode=myexplode)
plt.title("Sales Count per clarity ")
plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.figure()
plt.show()

print("The Diamond with WS1 Clarity has the most Sales with 24.22 % sales count")
print("The Diamond with IF Clarity has the most least with 1.37 % sales count")