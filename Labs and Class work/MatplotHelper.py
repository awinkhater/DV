import matplotlib.pylot as plt
import numpy as np

#====Plotting math
plt.style.use('seaborn-dark')
t= np.linspace(-np.pi, np.pi, 50)
s,c= np.sin(t), np.cos(t)
plt.figure(figsize=(5,5))
plt. plot(t,s,c= 'g', linewidth=3, marker = 'v', ms=9, mec='r', mfc='r', label = 'sine')
plt. plot(t,c,c= 'k', linewidth=3, linestyle='-.', label = 'cosine')
plt.legend()
plt.title('Sine and Cosine')
plt.grid()
plt.xlabel('time')
plt.ylabel('magnitude')

#======= Setting Fonts and Graphing Shapes

font1={'family':'serif', 'color': 'black', 'size': 20}
font2={'family':'serif', 'color': 'darkgreen', 'size': 15}
a,b= [1,2,2,1,1],[1,1,2,2,1]
d,e=[1.5,2.5,1.5,.5, 1.5],[0.5,1.5,2.5, 1.5, 0.5]
#Extra points are to comeback
plt.figure(figsize=(5,5))
plt. plot(a,b,c= 'r', linewidth=3, marker = 'v', ms=9, mec='r', mfc='r', label = 'Square')
plt. plot(d,e,c= 'g', linewidth=3, marker = 'D', ms=9, mec='b', mfc='b', label = 'Diamond')
plt.title('Square and Diamond', fontdict= font1, loc='left')
plt.legend(loc='lower left')
plt.grid(axis='y')
plt.xlabel('Width', fontdict=font2)
plt.ylabel('Height')
#Below can help with hidden axis
#plt.tight_layout()
plt.axis('equal')

#============ Histogram Subplot
def stock_hist(col, C):
    k = 0
    plt.figure(figsize= (16,8))
    for i in stocks:
        if col== 'Volume':
            k +=1
            df=data.get_data_yahoo(i,start=start_date, end=end_date)
            plt.subplot (3,2,k)
            plt.hist(df[col], bins=50, color=C, label=f'{col}')
            plt.ylabel(f"{col} Shares")
            plt.xlabel('Date')
            plt.grid()
            plt.title(f'{col} {i}')
        else:
            k += 1
            df = data.get_data_yahoo(i, start=start_date, end=end_date)
            plt.subplot(3, 2, k)
            plt.hist(df[col], bins=50, color=C, label=f'{col}')
            plt.ylabel(f"{col} USD ($)")
            plt.xlabel('Date')
            plt.grid()
            plt.title(f'{col} {i}')
    plt.tight_layout()

    plt.show()

#============== Line plot subplot
def stock_plot(col, C):
    k = 0
    plt.figure(figsize= (16,8))
    for i in stocks:
        if col== 'Volume':
            k +=1
            df=data.get_data_yahoo(i,start=start_date, end=end_date)
            plt.subplot (3,2,k)
            plt.plot(df[col], color= C, label=f'{col}')
            #This hides the scientific notation
            plt.ticklabel_format(style='plain', axis='y')
            plt.ylabel(f"{col} Shares")
            plt.xlabel('Date')
            plt.legend()
            plt.grid()
            plt.title(f'{col} {i}')
        else:
            k += 1
            df = data.get_data_yahoo(i, start=start_date, end=end_date)
            plt.subplot(3, 2, k)
            plt.plot(df[col], color=C, label=f'{col}')
            plt.ylabel(f"{col} USD ($)")
            plt.xlabel('Date')
            plt.legend()
            plt.grid()
            plt.title(f'{col} {i}')
    plt.tight_layout()

    plt.show()

stock_plot('High', 'b')
#================= Pie Chart

plt.figure()
sex2=TD.groupby('sex').size()
def absolute_value(val):
    a  = np.round((val/100*sex2.sum())/sex2.sum(), 3)
    return (f"{100* a}%")
myexplode = [0.02, 0.02]
plt.pie(sex2, labels=['Female', 'Male'], autopct=absolute_value, explode= myexplode)
plt.title("Pie Chart of Total People on the Titanic")
plt.legend()
plt.show()

 #============ DF Plot
# #6
#
# plt.figure()
# df.hist(column='US')
# plt.xlabel('Date')
# plt.ylabel('Confirmed COVID19 Cases')
# plt.title(f'US Confirmed COVID19 cases')
# plt.grid()
# plt.show()
#
# #7
# k=0
# countries= ['China_sum','UK_sum','Italy','Brazil','India']
# plt.figure()
# for i in range (len(countries)):
#     plt.subplot(3, 2, i+1)
#     plt.hist(df[countries[i]])
#     plt.xlabel('Date')
#     plt.ylabel('COVID19 Cases')
#     plt.title(f'US Confirmed COVID19 cases')
#     plt.tight_layout()
# plt.grid()
# plt.show()
#=========================
#Math graphing stuff

# x = np.linspace(-10,10,100)
# x = np.array(x, dtype=np.complex)
# y1 = x ** 2
# y2 = x ** (1/2)
# y3 = x ** 3
# y4 = x **(1/3)
#
# fig, ax = plt.subplots(2,2)
# ax[0,0].plot(x,y1, label='$f(x) = x^2$')
# ax[0,0].legend()
# ax[0,0].set_title('$f(x) = x^2$')
# ax[0,0].set_xlabel('Samples')
# ax[0,0].set_ylabel('Mag.')
# ax[0,0].grid()
#
# ax[1,0].plot(x,y2,label='$f(x) = \sqrt{x}$')
# ax[1,0].legend()
# ax[1,0].set_title('$f(x) = \sqrt{x}$')
# ax[1,0].set_xlabel('Samples')
# ax[1,0].set_ylabel('Maginitude')
# ax[1,0].grid()
#
# ax[0,1].plot(x,y3,label='$f(x) = x^3$')
# ax[0,1].legend()
# ax[0,1].set_title('$f(x) = x^3$')
# ax[0,1].set_xlabel('Samples')
# ax[0,1].set_ylabel('Maginitude')
# ax[0,1].grid()
#
# ax[1,1].plot(x,y4,label='$f(x) = \sqrt[3]{x}$')
# ax[1,1].legend()
# ax[1,1].set_title('$f(x) = \sqrt[3]{x}$')
# ax[1,1].set_xlabel('Samples')
# ax[1,1].set_ylabel('Maginitude')
# ax[1,1].grid()
# fig.tight_layout()
#
# plt.show()
#

# x = np.linspace(1,10)
# y = [10 ** el  for el in x]
# z = [2 * el  for el in x]
#
# fig = plt.figure(figsize=(10,8))
# ax1 = fig.add_subplot(2,2,1)
# ax1.plot(x,y,color = 'blue')
# ax1.set_font = 20
# ax1.set_yscale('log')
# ax1.set_title(r'Logarithmic plot of ${10}^x$')
# ax1.set_ylabel(r'$ {y} = {10}^{x} $')
# plt.grid(visible=True,which='both',axis='both')
#
#
# ax2 = fig.add_subplot(2,2,2)
# ax2.plot(x,y,color = 'red')
# ax2.set_yscale('linear')
# ax2.set_title(r'Linear plot of ${10}^x$')
# ax2.set_ylabel(r'$ {y} = {10}^{x} $')
# plt.grid(b=True,which='both',axis='both')
#
# ax3 = fig.add_subplot(2,2,3)
# ax3.plot(x,z,color = 'green')
# ax3.set_yscale('log')
# ax3.set_title(r'Logarithmic plot of ${2}^{x}$')
# ax3.set_ylabel(r'$ {y} = {2}^{x} $')
# plt.grid(b=True,which='both',axis='both')
#
# ax4 = fig.add_subplot(2,2,4)
# ax4.plot(x,z,color = 'magenta')
# ax4.set_yscale('linear')
# ax4.set_title(r'Linear plot of ${2}*{x}$')
# ax4.set_ylabel(r'$ {y} = {2}^{x} $')
# plt.grid(b=True,which='both',axis='both')
# plt.show()



# names = sns.get_dataset_names()
# print(names)
# df = sns.load_dataset('iris')
#
# # print(df.describe())
#
# plt.figure(figsize=(10,8))
#
# plt.subplot(2,2,1)
# plt.plot(df.sepal_width, label = 'sepal width')
# plt.title('sepal width')
#
# plt.subplot(2,2,2)
# plt.hist(df.sepal_width, label = 'septal width')
# plt.title('septal width')
#
# plt.subplot(2,2,3)
# plt.plot(df.petal_width, label = 'petal width')
# plt.title('petal width')
#
# plt.subplot(2,2,4)
# plt.hist(df.petal_width, label = 'petal width')
# plt.title('petal width')
#
# plt.show()
# font1 = {'family':'serif', 'color':'blue', 'size' :20}
# font2 = {'family':'serif', 'color':'darkred', 'size' :15}
#
# plt.plot([1,2,2,1,1],[1,1,2,2,1], lw = 3, c = 'red', label = 'square')
# plt.plot([1.5,2.5,1.5,.5,1.5],[0.5,1.5,2.5,1.5,0.5], lw = 3, c = 'k', label = 'diamond')
# plt.title('simple rectangle', fontdict = font1, loc='center')
# plt.ylabel('height', fontdict=font2)
# plt.xlabel('width', fontdict=font2)
# plt.tight_layout()
# plt.axis('equal')
# plt.legend(loc = 'lower left')
# plt.grid(axis='x')
# plt.show()
#
# t = np.linspace(-np.pi, np.pi, 50)
# s, c = np.sin(t), np.cos(t)
#
# plt.figure(figsize=(10,8))
# plt.plot(t,s, c = 'r', linewidth = 3, marker ='D' ,ms = 8,mec = 'k', mfc = 'white', label = 'sine')
# plt.plot(t,c, c = 'b', linewidth = 3, marker ='v',ms = 8,mec = 'r', mfc = 'red',label = 'cos')
# plt.legend()
# plt.title('sine and cosine')
# plt.grid()
# plt.xlabel('time')
# plt.ylabel('Mag.')
# plt.show()
