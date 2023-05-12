import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot  as plt
import seaborn as sns

#1
stocks=px.data.stocks()
#2
col=stocks.columns[1:]
fig=px.line(data_frame=stocks, x='date', y=['FB', 'AMZN', 'GOOG', 'AAPL', 'NFLX', 'FB', 'MSFT'])
fig.update_layout(width=1200, height=800, autosize= False,
                  font_family='Courier New',
                  font_color= 'red',
                  title_font_family='Times New Roman',
                  legend_title_font_color='green')
fig.show(renderer="browser")

#3
from plotly.subplots import make_subplots
import plotly.graph_objects as go


fig = make_subplots(rows=3, cols=2)
for i in range(len(col)):
    C= i%2 +1
    R= i%3 + 1
    print (C, R)
    fig.add_trace(go.Histogram(x=stocks[col[i]],  nbinsx=50, name=col[i]),
                    row=R, col=C)
    fig.update_layout(
        title="Stock Histogram Subplot",
        legend_title="legend")

fig.show()
#4
stocks_num=stocks.drop(['date'], axis=1)
#a.
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
scaler = preprocessing.StandardScaler().fit(stocks_num)
X_scaled= scaler.transform(stocks_num)


#b.
_,s,_= np.linalg.svd(X_scaled)
print(f'svd values : {s}')
print(f'condition number is {np.linalg.cond(X_scaled)}')
#c
sns.heatmap(stocks.corr(), annot=True)
plt.show()
#d
from sklearn.decomposition import PCA
pca=PCA(n_components='mle', svd_solver='full')
pca.fit(X_scaled)
print(f"Explained Varaince ratio at {len(pca.explained_variance_ratio_)} Components: ",(pca.explained_variance_ratio_.sum()))

print("We should be using 4 Principal Components")
pcx = pca.fit_transform(X_scaled)
#Reduced Data Set
df_2 = pd.DataFrame(data = pcx)
#5
#b
x1 = [3,3,3,3,3,3]
y1 = [0,20,40,60,80,100]

x2= [0,1,2,3,4,5]
y2=[95,95,95,95,95,95]
pca=PCA(n_components=6, svd_solver='full')
pca.fit(X_scaled)
plt.plot(np.cumsum(pca.explained_variance_ratio_)*100, color='r')
plt.plot(x1,y1, color='r', linestyle='dashed')
plt.plot(x2,y2, color='k', linestyle='dashed')
plt.title('Explained Variance Ratio')
plt.ylabel('Percent of Explained Variance')
plt.xlabel('# of Principal Components')
plt.grid()
plt.show()

#c
scaler2 = preprocessing.StandardScaler().fit(df_2)
X_scaled2= scaler2.transform(df_2)
_,s2,_= np.linalg.svd(X_scaled2)
print(f'svd values : {s2}')
print(f'condition number is {np.linalg.cond(X_scaled2)}')
print("This makes sense because since this dataset is post PCA, The condition number will be closer to 1 showing that matrix is invertible")
#d
sns.heatmap(df_2.corr(), annot=True)
plt.show()
print("The Values have very low correlations due to the reduced potential multicolinearity")
#e
df_2 = pd.DataFrame(data = pcx)
df_2.rename(columns={0:'Principal Col 1', 1:'Principal Col 2',
                     2:'Principal Col 3', 3:'Principal Col 4'},
            inplace=True)


# #f
#
d=stocks['date'].values.tolist()
df_2['Date']=d
print(df_2.shape)
fig=px.line(data_frame=df_2, x='Date', y=[ 'Principal Col 1','Principal Col 2',
                                          'Principal Col 3','Principal Col 4'])
fig.update_layout(width=1200, height=800, autosize= False,
                  font_family='Courier New',
                  font_color= 'red',
                  title_font_family='Times New Roman',
                  legend_title_font_color='green')
fig.show(renderer="browser")

#g
col2=df_2.columns[:4]

fig = make_subplots(rows=4, cols=1)
for i in range(len(col2)):
    C= 1
    R= i+1
    print (C, R)
    fig.add_trace(go.Histogram(x=df_2[col2[i]],  nbinsx=50, name=col2[i]),
                    row=R, col=C)
    fig.update_layout(
        title="Stock Post PCA Histogram Subplot",
        legend_title="legend")

fig.show()

#h
#ORIGINAL FEATURE SPACE
fig = px.scatter_matrix(stocks,
    dimensions=col,
    title="Original Feature Space",
    labels={col:col.replace('_', ' ') for col in col}) # remove underscore
fig.update_traces(diagonal_visible=False)
fig.show()

#REDUCED FEATURE SPACE
fig = px.scatter_matrix(df_2,
    dimensions=col2,
    title="Reduced Feature Space",
    labels={col:col.replace('_', ' ') for col in col2}) # remove underscore
fig.update_traces(diagonal_visible=False)
fig.show()

