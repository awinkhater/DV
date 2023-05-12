import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#'fivethirtyeight
#'ggplot
#Other styles exist
# plt.style.use('seaborn-dark')
# t= np.linspace(-np.pi, np.pi, 50)
# s,c= np.sin(t), np.cos(t)
# plt.figure(figsize=(5,5))
# plt. plot(t,s,c= 'g', linewidth=3, marker = 'v', ms=9, mec='r', mfc='r', label = 'sine')
# plt. plot(t,c,c= 'k', linewidth=3, linestyle='-.', label = 'cosine')
# plt.legend()
# plt.title('Sine and Cosine')
# plt.grid()
# plt.xlabel('time')
# plt.ylabel('magnitude')

# font1={'family':'serif', 'color': 'black', 'size': 20}
# font2={'family':'serif', 'color': 'darkgreen', 'size': 15}
# a,b= [1,2,2,1,1],[1,1,2,2,1]
# d,e=[1.5,2.5,1.5,.5, 1.5],[0.5,1.5,2.5, 1.5, 0.5]
# #Extra points are to comeback
# plt.figure(figsize=(5,5))
# plt. plot(a,b,c= 'r', linewidth=3, marker = 'v', ms=9, mec='r', mfc='r', label = 'Square')
# plt. plot(d,e,c= 'g', linewidth=3, marker = 'D', ms=9, mec='b', mfc='b', label = 'Diamond')
# plt.title('Square and Diamond', fontdict= font1, loc='left')
# plt.legend(loc='lower left')
# plt.grid(axis='y')
# plt.xlabel('Width', fontdict=font2)
# plt.ylabel('Height')
# #Below can help with hidden axis
# #plt.tight_layout()
# plt.axis('equal')

#names=sns.get_dataset_names()
#print (names)
#==========SUBPLOT
#df=sns.load_dataset('iris')
#print(df.describe())
# plt.figure(figsize= (10,8))
# plt.subplot(2,2,1)
# plt.plot(df.sepal_width, label= 'Sepal Width')
# plt.title('sepal width')
#
# plt.subplot(2,2,2)
# plt.hist(df.sepal_width, label= 'Sepal Width')
# plt.title('sepal width')
#
# plt.subplot(2,2,3)
# plt.plot(df.petal_width, label= 'Petal Width')
# plt.title('petal width')
#
# plt.subplot(2,2,4)
# plt.hist(df.petal_width, label= 'Petal Width')
# plt.title('petal width')
#
# plt.show()

# x= np.linspace(1,10)
# y= [10 ** el for el in x]
# z=[2* el for el in x]
#
# fig= plt.figure(figsize=(10,8))
# ax1 = fig.add_subplot(2,2,1)
# ax1.plot(x,y, color = 'blue')
# ax1.set_font = 20
# ax1.set_yscale('log')
# ax1.set_title(r'Logarithmic plot of ${10}^x$')
# ax1.set_ylabel(r'${y} = {10}^{x} $')
# plt.grid(visible=True, which= 'both', axis= 'both')
#
# ax2 = fig.add_subplot(2,2,2)
# ax2.plot(x,y, color = 'black')
# ax2.set_font = 20
# ax2.set_yscale('linear')
# ax2.set_title(r'Linear plot of ${10}^x$')
# ax2.set_ylabel(r'${y} = {10}^{x} $')
# plt.grid(visible=True, which= 'both', axis= 'both')
#
# ax3 = fig.add_subplot(2,2,3)
# ax3.plot(x,z, color = 'red')
# ax3.set_font = 20
# ax3.set_yscale('log')
# ax3.set_title(r'Logarithmic plot of ${2}^x$')
# ax3.set_ylabel(r'${y} = {2}^{x} $')
# plt.grid(visible=True, which= 'both', axis= 'both')
#
# ax4 = fig.add_subplot(2,2,4)
# ax4.plot(x,z, color = 'magenta')
# ax4.set_font = 20
# ax4.set_yscale('linear')
# ax4.set_title(r'Linear plot of ${2}^x$')
# ax4.set_ylabel(r'${y} = {2}^{x} $')
# plt.grid(visible=True, which= 'both', axis= 'both')
# plt.show()

#CODE FOR THIRD METHOD WILL BE ONLINE for plt.subplotsn