import dash
import numpy as np
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
#1

url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/Metro_Interstate_Traffic_Volume.csv'
df=pd.read_csv(url)

print(df.describe())

#2
num=['temp', 'rain_1h', 'snow_1h', 'clouds_all', 'traffic_volume']
cat=['holiday', 'weather_main', 'weather_description']

for i in num:
    for j in df[i]:
        if j == None:
            j=df[i].mean()


#Wasn't able to get duplicate dates removed

a=df.isna().sum()/len(df)*100
#Percent of data that is missing
print(a)

#3
A=pd.DataFrame(df[['rain_1h','snow_1h','clouds_all' ,'temp' ]])

corr = A.corr()
fig = go.Figure(data=go.Heatmap(z=corr.values,
                                    x=A.columns,
                                    y=A.columns))
fig.update_layout(
        title="Heatmap",
        xaxis_title="Correlation",

        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        ))
fig.show()
#3b
scaler = preprocessing.StandardScaler().fit(A)
X_scaled= scaler.transform(A)

# #3c
from sklearn.decomposition import PCA
pca=PCA(n_components='mle', svd_solver='full')
pca.fit(X_scaled)
print(f"Explained Varaince ratio at {len(pca.explained_variance_ratio_)} Components: ",((pca.explained_variance_ratio_.sum())))
print("Even with losing one element, the explained variance is only .78, so pca is proving ineffective and we shouldnt remove any features")
pcx = pca.fit_transform(X_scaled)
#Reduced Data Set
df2 = pd.DataFrame(data = pcx)
#d
print(f'Original condition number is {round(np.linalg.cond(X_scaled),2)}')
print(f'Reduced condition number is {round(np.linalg.cond(df2), 2)}')

print("The reduced feature set has a condition number that is closer to 1, thus showing that the matrix is invertible and multicolinearity concerns are lower")

#4
#a
Q1=df['traffic_volume'].quantile(.25)
Q3=df['traffic_volume'].quantile(.75)

print("Q1:",Q1)
print("Q3:",Q3)

#b
IQR= Q3-Q1
print(f"IQR={IQR}")
print(f"Any Traffic Volume that is more than {Q3+1.5*IQR} or less than {Q1-1.5*IQR} is an outlier")

#c.

def remove_outliers(df, columns):
    for col in columns:

        Q3 = df[col].quantile(.75)
        Q1 = df[col].quantile(.25)
        IQR= Q3-Q1
        df = df[(df[col] <= Q3+(1.5 * IQR))]
        df = df[(df[col] >= Q1 - (1.5 * IQR))]
    return (df)

remove_outliers(df, ['traffic_volume'])

fig = px.box(df, y='traffic_volume')
fig.update_layout(
    title="Box Plot for Traffic",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple",

    )
)
fig.show()

#5
#a
Q1=df['temp'].quantile(.25)
Q3=df['temp'].quantile(.75)

print("Q1:",Q1)
print("Q3:",Q3)

#b
IQR= round(Q3-Q1,2)
print(f"IQR={IQR}")
print(f"Any Temp that is more than {round((Q3+1.5*IQR),2)} or less than {round((Q1-1.5*IQR),2)} is an outlier")

#c.

def remove_outliers(df, columns):
    for col in columns:

        Q3 = df[col].quantile(.75)
        Q1 = df[col].quantile(.25)
        IQR= Q3-Q1
        df = df[(df[col] <= Q3+(1.5 * IQR))]
        df = df[(df[col] >= Q1 - (1.5 * IQR))]
    return (df)

remove_outliers(df, ['temp'])

fig = px.box(df, y='temp')
fig.update_layout(
    title="Box Plot for Temp",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple",

    )
)
fig.show()

#6
sns.heatmap(df.corr(), annot=True)
plt.title('Feature Heat Map')
plt.tight_layout()
plt.show()
#7
fig1 = px.bar(df, x='weather_main', y='traffic_volume', color='weather_main')
fig1.update_layout(
        title="Borough Graph Bar Plot",
        xaxis_title="Weather Types",
        yaxis_title="Traffic Volume",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
fig1.show()

#8
sns.set_style('darkgrid')
sns.histplot(data=df, x='traffic_volume',hue='weather_main', element='poly')
plt.title('Weather Traffic Histogram')
plt.show()

#9
sns.set_style('darkgrid')
sns.histplot(data=df, x='traffic_volume',hue='weather_main', element='bars')
plt.title('Weather Traffic Histogram')
plt.show()

#10
sns.set_style('darkgrid')
sns.histplot(data=df, x='traffic_volume',hue='weather_main', element='step')
plt.title('Weather Traffic Histogram')
plt.show()

#11
sns.set_style('darkgrid')
sns.histplot(data=df, x='traffic_volume',hue='weather_main', multiple="stack")
plt.title('Weather Traffic Histogram')
plt.show()

#12
sns.set_style('darkgrid')
sns.displot(data=df, x="traffic_volume", hue='weather_main', kind='kde')
plt.title('Traffic_volume KDE Plot')
plt.tight_layout()
plt.show()
#13
df1= df.loc[0:99]

df1=df1[['temp', 'traffic_volume']]
scaler = preprocessing.StandardScaler().fit(df1)
X_scaled= scaler.transform(df1)
scd = pd.DataFrame(data = X_scaled, columns=['temp', 'traffic_volume'])

for i in range (1,5):
    plt.subplot(2,2,i)
    if i == 1:
        plt.plot(df1['temp'])
        plt.plot(df1['traffic_volume'])
        plt.xlabel='Index'
        pltylabel='Value'
        plt.title('Raw Data Plot')
    if i == 2:
        plt.hist(df1['temp'])
        plt.hist(df1['traffic_volume'])
        plt.xlabel='Value'
        plt.ylabel='Frequency'
        plt.title('Raw Data Hist')
    if i ==3:
        plt.plot(scd['temp'])
        plt.plot(scd['traffic_volume'])
        plt.xlabel = 'Index'
        pltylabel = 'Value'
        plt.title('Scaled Data Plot')
    if i==4:
        plt.hist(scd['temp'])
        plt.hist(scd['traffic_volume'])
        plt.xlabel='Value'
        plt.ylabel='Frequency'
        plt.title('Scaled Data Plot')
plt.tight_layout()
plt.show()

# #15
from scipy import stats

z=stats.kstest(df['traffic_volume'], "norm")
print(f"K-S test: statistic{z[0]} p-value={z[1]}")
print("Judging by the K-S Test, Traffic and the QQ plot, the traffic is not normal")
stats.probplot(df['traffic_volume'], dist="norm", plot=plt)
plt.title('Traffic QQ Plot')
plt.grid()
plt.xlabel=('Theoretical Quantities')
plt.ylabel=('Sample Quantities')
plt.show()

# #16
z=stats.kstest(df['temp'], "norm")
print(f"K-S test: statistic{z[0]} p-value={z[1]}")
print("Judging by the K-S Test, Temp and the QQ plot, the temp is not normal")
stats.probplot(df['temp'], dist="norm", plot=plt)
plt.title('Temp QQ Plot')
plt.grid()
plt.xlabel=('Theoretical Quantities')
plt.ylabel=('Sample Quantities')
plt.show()

#14 BONUS======================
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
from scipy.stats import shapiro
ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
#
ftp_app2.layout = html.Div(
    [

        html.P('Select a Column'),
        dcc.Dropdown(id='my-drop', options=[
                     {'label': 'temp', 'value': 'temp'},
                    {'label': 'rain_1h', 'value': 'rain_1h'},
                    {'label': 'snow_1h', 'value': 'snow_1h'},
                    {'label': 'clouds_all', 'value': 'clouds_all'},
                    {'label': 'traffic_volume', 'value': 'traffic_volume'},
                 ], clearable= True),
        html.Br(),
        html.P('Select a Normality Test Type'),
dcc.Dropdown(id='my-test', options=[
                      {'label': 'Shapiro', 'value': 'Shapiro'},
                     {'label': 'KS', 'value': 'KS'},
                   {'label': 'Dago', 'value': 'Dago'},

                 ], clearable= True),
        html.Br(),
        html.Div(id='my-out')
])

@ftp_app2.callback(
            Output(component_id='my-out', component_property='children'),
            [Input(component_id='my-drop', component_property='value'),
             Input(component_id='my-test', component_property='value')])

def update_Histo(B,C):
    if C== 'Shapiro':
        z = stats.shapiro(df[B])
        O=(f"Shapiro test: statistic{z[0]} p-value={z[1]}")
    if C== 'KS':
        z = stats.kstest(df[B], "norm")
        O=(f"K-S test: statistic{z[0]} p-value={z[1]}")
    if C=='Dago':
        x1, p1 = stats.normaltest(df['B'])

        O=(f"da_k_squared test: statistic{x1} p-value={p1}")
    return(O)
ftp_app2.server.run(debug=True)