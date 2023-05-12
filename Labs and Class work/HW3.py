import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#1
dfraw= sns.load_dataset('penguins')
print(dfraw.describe())
#2
print(dfraw.isna().sum())
df=dfraw.copy()
df.dropna(inplace=True)
print(50*"*")
print("clean dataset null count:")
print(df.isna().sum())

#3
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm')
plt.title('Flipper Length Histogram 1')
plt.show()

print("The distribution seems to be bimodal near 190 and 215.")

#4
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm', binwidth=3)
plt.title('Flipper Length Histogram 2')
plt.show()

print("The distribution now seems to be more right skewed with a mean around 195")

#5
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm', binwidth=30)
plt.title('Flipper Length Histogram 3')
plt.show()

print("This graph basically shows the right skew, but is nearly useless")

#6
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species')
plt.title('Flipper Length Displot 1')
plt.tight_layout()
plt.show()

print("Gentoo have a big advantage in flipper length and Adelie seem to have the smallest flippers")
#7
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species', element='step')
plt.title('Flipper Length Displot 2')
plt.tight_layout()
plt.show()
print("We can see even clearer that the chinstrap penguins sit in the middle but have more overlap in flipper length with the Adelie")
#8
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm', hue='species', multiple="stack")
plt.title('Flipper Length Stacked Histogram')
plt.tight_layout()
plt.show()
print("IT appears that Gentoo have the longest flippers by a signifcant margin")
#9
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='sex', multiple='dodge')
plt.title('Flipper Length Displot 3')
plt.tight_layout()
plt.show()
print("It appears that Female Penguins have the longer flippers")

#10
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", col="sex")
plt.title('Flipper Length Displot 4')
plt.tight_layout()
plt.show()
print("The most frequent range for males is 190-195, for females its also 190-195 ")

#11
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm', hue='species', multiple="stack", stat='density')
plt.title('Flipper Length Stacked Normalized Histogram')
plt.tight_layout()
plt.show()
print("The Gentoo has the largest flipper length, their range is from 200-230mm")
#12
sns.set_style('darkgrid')
sns.histplot(data=df, x='flipper_length_mm', hue='sex', multiple="stack", stat='density')
plt.title('Flipper Length Normalized Histogram by Sex')
plt.tight_layout()
plt.show()
print("Males have a a larger flipper length and the range is from 180-230 mm")
#13
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species',stat='probability')
plt.title('Flipper Length Displot 5')
plt.tight_layout()
plt.show()
print("The most probable flipper length and species is an Adelie with a flipper length between 190-195 mm")
#14
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species', kind='kde')
plt.title('Flipper Length KDE Plot')
plt.tight_layout()
plt.show()
#15
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='sex', kind='kde')
plt.title('Flipper Length KDE Plot (by sex)')
plt.tight_layout()
plt.show()
#16
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species', kind='kde', multiple='stack')
plt.title('Stacked Flipper Length KDE Plot')
plt.tight_layout()
plt.show()
#17
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='sex', kind='kde', multiple='stack')
plt.title('Stacked Flipper Length KDE Plot (by sex)')
plt.tight_layout()
plt.show()
#18
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='species', kind='kde', fill=True)
plt.title('Filled Flipper Length KDE Plot')
plt.tight_layout()
plt.show()
print("This fill style makes it easier to see the relative densities of all the species in relation to eachother")
#19
sns.set_style('darkgrid')
sns.displot(data=df, x="flipper_length_mm", hue='sex', kind='kde', fill=True)
plt.title('Stacked Flipper Length KDE Plot (by sex)')
plt.tight_layout()
plt.show()
print("The fill option makes seeing the overlap in kde plots alot clearer")
#20
sns.set_style('darkgrid')
sns.regplot(x="bill_length_mm",
            y="bill_depth_mm",
            data=df)
plt.title('Bill Length vs Bill Depth Regression Plot')
plt.tight_layout()
plt.show()
print("It appears bill depth is negatively correlated with bill length due to the slop of the regression line")
#21
sns.set_style('darkgrid')
sns.countplot(x='island', hue='species', data=df)
plt.title('Island Population by species')
plt.tight_layout()
plt.show()
print("While Adelie penguins are present on each island, Gentoo penguins are present on only Biscoe, and Chinstrap are only present on Dream")
#22
sns.set_style('darkgrid')
sns.countplot(x='sex', hue='species', data=df)
plt.title('Sex Count by species')
plt.tight_layout()
plt.show()
print("It appears that both species have nearly identical even sex distributions")
#23
sns.set_style('darkgrid')
sns.displot(df, x="bill_length_mm", y="bill_depth_mm", hue='sex', kind="kde", fill=True )
plt.title('Bill Length-Depth Distribution Colored by Sex')
plt.tight_layout()
plt.show()
#24
sns.set_style('darkgrid')
sns.displot(df, x="bill_length_mm", y="flipper_length_mm", hue='sex', kind="kde", fill=True )
plt.title('Bill Length- Flipper Length Distribution Colored by Sex')
plt.tight_layout()
plt.show()
#25
sns.set_style('darkgrid')
sns.displot(df, x="flipper_length_mm", y="bill_depth_mm", hue='sex', kind="kde", fill=True )
plt.title('Flipper Length/ Bill Depth Distribution Colored by Sex')
plt.tight_layout()
plt.show()
#26
plt.figure(figsize=(8,16))
sns.set_style('darkgrid')
fig, axes = plt.subplots(3, 1)

sns.kdeplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue='sex', fill=True, ax=axes[0])
sns.kdeplot(data=df, x="bill_length_mm", y="flipper_length_mm", hue='sex',fill=True, ax=axes[1])
sns.kdeplot(data=df, x='flipper_length_mm', y='bill_depth_mm', hue='sex', fill=True, ax=axes[2])
plt.tight_layout()
plt.show()

#27
sns.set_style('darkgrid')
sns.displot(df, x="bill_length_mm", y="bill_depth_mm", hue='sex')
plt.title('Bill Length vs Depth Displot 2')
plt.tight_layout()
plt.show()

#28
sns.set_style('darkgrid')
sns.displot(df, x="flipper_length_mm", y="bill_depth_mm", hue='sex')
plt.title('Bill Length vs Depth Displot 3')
plt.tight_layout()
plt.show()

#29
sns.set_style('darkgrid')
sns.displot(df, x="flipper_length_mm", y="bill_length_mm", hue='sex')
plt.title('Bill Length vs Depth Displot 4')
plt.tight_layout()
plt.show()