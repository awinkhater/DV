import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#1
mean_x = 0
std_x= 1
N_x=1000
np.random.seed(123)
x= np.random.normal(mean_x, std_x, N_x)
mean_y=5
std_y= np.sqrt(2)
y=np.random.normal(mean_y, std_y, N_x )
#2
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

#3
def info_get (x,y):
    '''

    :param x: An array of n numbers
    :param y: An array of n numbers
    :return: Various stats
    '''
    print("The sample mean of random variable x is:", np.mean(x))
    print("The sample mean of random variable y is:", np.mean(y))
    print("The sample variance of random variable x is :", np.var(x))
    print("The sample variance of random variable y is :", np.var(y))
    print("The sample Pearson's Correlation ", corr_coeff(x,y))

info_get(x,y)

#4
plt.figure()
plt.plot (x, label = 'x')
plt.plot(y, label = 'y')
plt.title ('x and y random variables')
plt.legend(['x', 'y'])
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()
plt.show()
#5
plt.figure()
plt.hist (x, label = 'x')
plt.hist(y, label = 'y')
plt.title ('x and y random variables')
plt.legend(['x', 'y'])
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()
plt.show()

#6.
url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv'
df = pd.read_csv(url)

#Cleaning the data
df['Sales'] = df['Sales'].to_numpy()
df['AdBudget']= df['AdBudget'].to_numpy()
df['GDP']=df['GDP'].to_numpy()
#7 and #8
print ("The Sample Pearson Correlation Coeffcient between Sales and AdBudget:", corr_coeff(df['Sales'], df['AdBudget']))
print ("The Sample Pearson Correlation Coeffcient between Sales and GDP:", corr_coeff(df['Sales'], df['GDP']))
print ("The Sample Pearson Correlation Coeffcient between AdBudget and GDP:", corr_coeff(df['AdBudget'], df['GDP']))
#9
date = pd.date_range(df['Date'][0], df['Date'][99], periods=len(df))
df.index = date
df[['Sales','AdBudget','GDP']].plot()
plt.title ('Sales, AdBudget, and GDP Line Plot')
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=90)
plt.legend(['GDP', 'Sales', 'AdBudget'])
plt.show()

#10
plt.figure()
plt.hist(df['Sales'])
plt.hist(df['AdBudget'])
plt.hist(df['GDP'])
plt.title ('Sales, AdBudget, and GDP Histogram')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.legend(['GDP', 'Sales', 'AdBudget'])
plt.show()

