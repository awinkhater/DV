#Class Day 7

#lab 3:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme(style='ticks')
#================= Seaborn Zone
#names= sns.get_dataset_names()
#print(names)

flights=sns.load_dataset('flights')
tips=sns.load_dataset('tips')
D=sns.load_dataset('diamonds')
Peng=sns.load_dataset('penguins')
fmri=sns.load_dataset('fmri')
#===
#Line Plot with sns
# plt.figure(figsize=(10,10))
# sns.lineplot(data=flights,
#               x='year',
#               y='passengers',
#              ci=None,
#              hue= 'month',
#              palette='Paired')
# plt.grid()
# plt.show()

#print(D['color'].unique())
# sns.lineplot(data=D,
#               x='clarity',
#               y='price',
#              hue='cut',
#              ci=None)
# plt.legend(loc='lower right')
# plt.grid()
# plt.show()
#==== Count Plot
# df_male= tips[tips['sex']=='Male']
# df_female = tips[tips['sex'] == 'Female']
# sns.countplot(data=tips,
#               x='smoker',
#               hue='sex')
# plt.show()
#
# sns.displot(data=tips, x='total_bill', col='time', row='sex', kind='kde')
# plt.show()

#==== Pairplot
# sns.pairplot(data = Peng, hue='species')
# plt.show()

#==== Lmplot

# sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
# plt.show()

#======= Joinplot

# sns.jointplot(data=tips, x='total_bill', y='tip')
# plt.show()

#======= Boxplot
#
# sns.boxplot(data=fmri, x='timepoint', y='signal', hue='region')
# plt.show()
# # ===== Swarmplot
# sns.swarmplot(data=fmri, x='timepoint', y='signal', hue='region')
# plt.show()

#CATPLOT=============================
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()
#============== Lab Help
# #1
# url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/CONVENIENT_global_confirmed_cases.csv'
# df=pd.read_csv(url)
# df=df.dropna()
#
#
# df['Country/Region'] = pd.to_datetime(df['Country/Region'])
# df=df.set_index('Country/Region')
#
#
# plt.figure()
# df.plot(y=['Italy'], legend=None)
# plt.xlabel('Date')
# plt.ylabel('Confirmed COVID19 Cases')
# plt.title('Global Confirmed COVID19 cases')
# plt.grid()
# plt.tight_layout()
# plt.show()