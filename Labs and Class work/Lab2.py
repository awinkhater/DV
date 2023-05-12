import numpy as np
import pandas as pd
import scipy.stats
from prettytable import PrettyTable
#1.
url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv'
df = pd.read_csv(url)
#This is my function from lab 1: it only uses numpy
def corr_coeff( x,y):
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


print ("The sample Pearson's Correlation between,Sales,and,AdBudget,is:", corr_coeff(df["Sales"], df["AdBudget"]))
#2
print ("The sample Pearson's Correlation between,AdBudget and,GDP,is:", corr_coeff(df["GDP"], df["AdBudget"]))
#3
print ("The sample Pearson's Correlation between,Sales,and,GDP,is:", corr_coeff(df["Sales"], df["GDP"]))
#4
def corr_t(D,a,b, alpha):
    '''
    :param D: a data frame
    :param a: an array of numbers or dataframe array
    :param b: an array of numbers or a dataframe column
    :return:
    '''
    n=len(D)
    r = corr_coeff(a,b)
    t_0= (r*((n-2)**0.5))/((1-(r**2))**0.5)
    p=scipy.stats.t.sf((t_0), n-3)
    if p < alpha:
        return("p=",p,"The correlation is significant, reject the null hypothesis")
    else:
        return("p=",p,"The correlation is not siginficant, fail to reject.")

print("AdBudget and Sales", corr_t(df, df['AdBudget'], df['Sales'], 0.05))
#This p-value is significant
print("GDP and Sales", corr_t(df, df['GDP'], df['Sales'],0.05))
#This p-value is significant
print("AdBudget and Sales", corr_t(df, df['AdBudget'], df['GDP'],0.05))
#This p-value is significant



#5
def parr_corr_t (D, h,g,w,alpha, t):
    '''

    :param D: A dataframe
    :param h: A column of dataframe
    :param g: A column of dataframe. A confounding variable to be excluded
    :param w: A column of dataframe
    :param alpha: the p-value threshold
    :return:
    '''

    r_hw = corr_coeff(h,w)
    r_gw = corr_coeff(g,w)
    r_gh = corr_coeff(g,h)

    r_hw_g= round((r_hw -r_gh * r_gw)/((1-r_gw**2)**(0.5)*(1-r_gh**2)**(0.5)),2)
    n= len(D)
    k = 1
    if t==1:
#t-test:
        t_0= r_hw_g*((n-2-k)/(1-r_hw_g**2))**0.5

        p = ((scipy.stats.t.sf(t_0, n - 3)))
        if abs(p) < alpha:
            return ("Parital Correlation=", r_hw_g, "p=", p, "The correlation is significant, reject the null hypothesis")
        else:
            return ("Parital Correlation=", r_hw_g, "p=", p, "The correlation is not siginficant, fail to reject.")
    else:
        return(r_hw_g)

print("Sales and AdBudget (without GDP):", parr_corr_t(df,df['Sales'], df['GDP'],df['AdBudget'], 0.05,1))

#6
print(("GDP and AdBudget (without Sales):",parr_corr_t(df,df['GDP'], df['Sales'],df['AdBudget'], 0.05, 1)))
#7
print(("Sales and GDP (without AdBudget):",parr_corr_t(df,df['Sales'], df['AdBudget'],df['GDP'], 0.05, 1)))
#8
def corr_table_prep(D, a,b,c):
    tdf = pd.DataFrame(columns=['Category','Sales and AdBudget', 'Sales and GDP', 'GDP and AdBudget'])
    list=["Correlation"]
    list.append(corr_coeff(a,b))
    list.append(corr_coeff(b,c))
    list.append(corr_coeff(a,c))
    tdf.loc[0] = list
    list2=["Partial Correlation (Excluding Non-Listed Column)"]
    list2.append(parr_corr_t(D,a,c,b,0.5,0))
    list2.append(parr_corr_t(D, b, a, c, 0.5,0))
    list2.append(parr_corr_t(D, a, b, c, 0.5,0))
    tdf.loc[1] = list2
    return (tdf)

def corr_PT1(D,a,b,c, title):
    df= corr_table_prep(D,a,b,c)
    x = PrettyTable()
    for i in range (df.shape[0]):
        x.add_row(df.iloc[i,:])
        x.title= title
        x.field_names = df.columns
        x.float_format='.2'
    print(x.get_string)

corr_PT1(df, df['AdBudget'], df['Sales'], df['GDP'], "Correlation Comparison Table")

#9
#Uhhh