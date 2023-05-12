import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1
df= sns.load_dataset('iris')

col=['sepal_length','sepal_width', 'pedal_length', 'pedal_width']
plt.figure(figsize=(16,12))
for i in range(0, 2):
    for j in range(0 ,len(col)):
        if i==0:
            plt.subplot(4,2,j+1)
            sns.lineplot(data=df,x=df.index, y='sepal_length', hue='species')
            plt.ylabel('cm')
            plt.xlabel('samples')
        if i==1:
            plt.subplot(2, 4, 5 + j )
            sns.histplot(data=df, x=df.index, hue='species', fill=True)
            plt.ylabel('cm')
            plt.xlabel('samples')
plt.grid()
plt.tight_layout()
plt.show()

#2:
for i in range (0,4):
    k= col[i]
    print(f"Setosa Mean {k}:",np.round((df.mean(['species']=='setosa'))[i]),2)
    print(f"Versicolor Mean {k}:",np.round(df.mean(['species']=='versicolor')[i]),2)
    print(f"Virginica Mean {k}:",np.round(df.mean(['species']=='virginica')[i]),2)

