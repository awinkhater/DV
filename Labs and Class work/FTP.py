#Final Term Project Workspace
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy.stats
from plotly.subplots import make_subplots
from scipy import stats

# Imports

import numpy as np
import pandas as pd
import scipy
#Dash
import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df= pd.read_csv('FTPDataset.csv')

#print(df.columns)
#Separating out the useful features for modeling
features = ['LotArea', 'BldgArea', 'NumBldgs',
                 'NumFloors', 'UnitsRes', 'UnitsTotal',
                 'LotFront', 'LotDepth', 'BldgFront',
                 'BldgDepth','LotType', 'BsmtCode', 'AssessLand', 'AssessTot']


dfF=df.loc[:, features]
dfF=pd.DataFrame(dfF)
# print(dfF['LotType'].values.tolist())
#Encodeing Catgorical Variable
# dfF['Borough']= dfF['Borough'].astype('category')
# dfF['Borough']= dfF['Borough'].cat.codes
#
# #============ NORMALITY CHECKS FOR EACH VARIABLE
#
# ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
# #
# ftp_app2.layout = html.Div(
#     [
#
#         html.P('Normalization Column'),
#         dcc.Dropdown(id='my-drop', options=[
#                      {'label': 'LotArea', 'value': 'LotArea'},
#                      {'label': 'BldgArea', 'value': 'BldgArea'},
#                      {'label': 'NumBldgs', 'value': 'NumBldgs'},
#                      {'label': 'NumFloors', 'value': 'NumFloors'},
#                     {'label': 'UnitsRes', 'value': 'UnitsRes'},
#                      {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#                      {'label': 'LotFront', 'value': 'LotFront'},
#                      {'label': 'LotDepth', 'value': 'LotDepth'},
#                     {'label': 'BldgFront', 'value': 'BldgFront'},
#                      {'label': 'BldgDepth', 'value': 'BldgDepth'},
#                       {'label': 'BsmtCode', 'value': 'BsmtCode'},
#                      {'label': 'AssessLand', 'value': 'AssessLand'},
#                    {'label': 'AssessTot', 'value': 'AssessTot'},
#
#                  ], clearable= True),
#         html.Br(),
#         dcc.Graph(id= 'my-graph'),
#         html.Br(),
#         html.Div([
#                    dcc.Graph(id='my-graph2'),
#                    html.Br(),
#         html.Br(),
#         html.Div(id='my-out'),
#             html.Br()
#
#         ])
# ])
#
# @ftp_app2.callback(
#             Output(component_id='my-graph', component_property='figure'),
#             [Input(component_id='my-drop', component_property='value')])
#
# def update_Norm(B):
#     fig1 = px.histogram(df, x=B)
#     fig1.update_layout(
#         title="Normality Graph",
#         xaxis_title="Column Values",
#         yaxis_title="Frequency",
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         )
#     )
#     return(fig1)
#
# @ftp_app2.callback(
#             Output(component_id='my-graph2', component_property='figure'),
#             [Input(component_id='my-drop', component_property='value')])
#
# def update_QQ(a1):
#     qq = stats.probplot(df[a1], dist='lognorm', sparams=(1))
#     x = np.array([qq[0][0][0], qq[0][0][-1]])
#
#     fig = go.Figure()
#     fig.add_scatter(x=qq[0][0], y=qq[0][1], mode='markers')
#     fig.add_scatter(x=x, y=qq[1][1] + qq[1][0] * x, mode='lines')
#     fig.update_layout(
#         title="QQ Plot",
#         xaxis_title="Theoretical Quantities",
#         yaxis_title="Standard Residuals",
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         )
#     )
#     fig.layout.update(showlegend=False)
#     return(fig)
#
# @ftp_app2.callback(
#             Output(component_id='my-out', component_property='children'),
#             Input(component_id='my-drop', component_property='value'))
# def update_test(C):
#     k, p = stats.normaltest(df[C])
#     if p <= 0.05:
#         return("Per the D'Agostino test, this column is not normally distributed")
#     else:
#         return ("Per the D'Agostino test, this column is normally distributed")
#
#
# ftp_app2.server.run(debug=True)



#PCA
# x=dfF.values
# y = df.loc[:,['Borough']].values
# scaler = preprocessing.StandardScaler().fit(x)
# X_scaled = scaler.transform(x)
#
# pca=PCA(n_components='mle', svd_solver='full')
# pca.fit(X_scaled)
#
# pcx = pca.fit_transform(X_scaled)
# #Reduced Data Set
# df_pca = pd.DataFrame(data = pcx)
# # ==============================#Comparative PCA Map
# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
#
# ftp_app3.layout = html.Div(
#     [
#         dcc.Graph(id= 'my-graph'),
#         html.P('Number of Principal Components'),
#         dcc.Slider(id='pca-slider', min=1, max=10, value=1,
#                    marks={1: 1,2:2,4: 4,6:6, 8:8, 10:10})
#         ])
#
#
# @ftp_app3.callback(
#             Output(component_id='my-graph', component_property='figure'),
#             [Input(component_id='pca-slider', component_property='value')])
#
# def update_pca(B):
#     pca = PCA(n_components=B, svd_solver='full')
#     pca.fit(X_scaled)
#     fig=px.line(np.cumsum(pca.explained_variance_ratio_) * 100)
#     return(fig)
# ftp_app3.server.run(debug=True)
#=============== Correlation Plot

# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
# #
# ftp_app3.layout = html.Div(
#     [   html.H1('Heatmap and Correlation Matrix'),
#         html.P('Desired Columns For Heatmap and Correlation'),
#         dcc.Checklist(id='mycheck', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ]),
#
#     html.Div([dcc.Graph(id='mygraph')
#     ])
#
# ])
# @ftp_app3.callback(
#             Output(component_id='mygraph', component_property='figure'),
#             [Input(component_id='mycheck', component_property='value')])
#
# def update_Stats(a1):
#     DFtemp = []
#     DFtemp = pd.DataFrame(DFtemp)
#     DFtemp[a1] = df[a1]
#     corr = DFtemp.corr()
#     fig = go.Figure(data=go.Heatmap(z=corr.values,
#                                     x=DFtemp.columns,
#                                     y=DFtemp.columns))
#     fig.update_layout(
#         title="Heatmap",
#         xaxis_title="Correlation",
#
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         ))
#     return fig
#
#
# ftp_app3.server.run(debug=True)


#Correlation Thing (MAYBE DONT NEED/ Should be merged into heat map)


# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
#
# ftp_app3.layout = html.Div(
#     [
#         html.P('Column A'),
#         dcc.Dropdown(id='my-drop1', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea '},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'Borough', 'value': 'Borough'},
#             {'label': 'Lot', 'value': 'Lot'},
#             {'label': 'SchoolDist', 'value': 'SchoolDist'},
#             {'label': 'Council', 'value': 'Council'},
#             {'label': 'ZipCode', 'value': 'ZipCode'},
#             {'label': 'FireComp', 'value': 'FireComp'},
#             {'label': 'PolicePrct', 'value': 'PolicePrct'},
#             {'label': 'Health Area', 'value': 'HealthArea'},
#             {'label': 'SanitBoro', 'value': 'SanitBoro'},
#             {'label': 'Address', 'value': 'Address'},
#             {'label': 'BldgClass', 'value': 'BldgClass'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ], value=20,
#                      clearable=True),
#         html.P('Column B'),
#         dcc.Dropdown(id='my-drop2', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea '},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'Borough', 'value': 'Borough'},
#             {'label': 'Lot', 'value': 'Lot'},
#             {'label': 'SchoolDist', 'value': 'SchoolDist'},
#             {'label': 'Council', 'value': 'Council'},
#             {'label': 'ZipCode', 'value': 'ZipCode'},
#             {'label': 'FireComp', 'value': 'FireComp'},
#             {'label': 'PolicePrct', 'value': 'PolicePrct'},
#             {'label': 'Health Area', 'value': 'HealthArea'},
#             {'label': 'SanitBoro', 'value': 'SanitBoro'},
#             {'label': 'Address', 'value': 'Address'},
#             {'label': 'BldgClass', 'value': 'BldgClass'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ], value=20,
#                      clearable=True), html.Div(id='my-out')
#
#     ])
#
#
# @ftp_app3.callback(
#             Output(component_id='my-out', component_property='children'),
#             [Input(component_id='my-drop1', component_property='value'),
#              Input(component_id='my-drop2', component_property='value')])
#
# def update_coor(a1, b1):
#     A = df[a1].values.tolist()
#     B = df[b1].values.tolist()
#     P = corr_t(df, A, B, 0.05)
#     if P < 0.05:
#         return (f"{a1} and {b1} are significantly correlated")
#     else:
#         return (f"{a1} and {b1} aren't significantly correlated")
#
#
# ftp_app3.server.run(debug=True)

##======================= Describer
# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
#
# ftp_app3.layout = html.Div(
#     [   html.H1('Basic Statistics of Each Column of the Dataset'),
#         html.P('Desired Column'),
#         dcc.Dropdown(id='my-drop1', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea '},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'Borough', 'value': 'Borough'},
#             {'label': 'Lot', 'value': 'Lot'},
#             {'label': 'SchoolDist', 'value': 'SchoolDist'},
#             {'label': 'Council', 'value': 'Council'},
#             {'label': 'ZipCode', 'value': 'ZipCode'},
#             {'label': 'FireComp', 'value': 'FireComp'},
#             {'label': 'PolicePrct', 'value': 'PolicePrct'},
#             {'label': 'Health Area', 'value': 'HealthArea'},
#             {'label': 'SanitBoro', 'value': 'SanitBoro'},
#             {'label': 'Address', 'value': 'Address'},
#             {'label': 'BldgClass', 'value': 'BldgClass'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ], value=20,
#                      clearable=True),
#         html.Div(id='my-out'),
#
#     html.Div([dcc.Graph(id='box-graph')
#     ])
#
# ])
# @ftp_app3.callback(
#             Output(component_id='my-out', component_property='children'),
#             [Input(component_id='my-drop1', component_property='value')])
#
# def update_Stats(a1):
#     A = df[a1]
#     L = A.describe()
#     return("Count: ", L[0],
#                 " Mean: ", L[1],
#                    " Standard Deviation: ", L[2],
#                    " Minimum: ", L[3],
#                    " Median: ", L[5],
#                    " Maximum: ", L[7])
#
# @ftp_app3.callback(
#             Output(component_id='box-graph', component_property='figure'),
#             [Input(component_id='my-drop1', component_property='value')])
#
#
#
# def update_box(a1):
#     fig = px.box(df, y=a1)
#     return(fig)
#
# ftp_app3.server.run(debug=True)


#NEXT UP: GRAPHS

#Histogram/ Distplot/Violin Plot/ Multi-Variate Box

# ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
# #
# ftp_app2.layout = html.Div(
#     [
#
#         html.P('Select a Column'),
#         dcc.Dropdown(id='my-drop', options=[
#                      {'label': 'LotArea', 'value': 'LotArea'},
#                      {'label': 'BldgArea', 'value': 'BldgArea'},
#                      {'label': 'NumBldgs', 'value': 'NumBldgs'},
#                      {'label': 'NumFloors', 'value': 'NumFloors'},
#                     {'label': 'UnitsRes', 'value': 'UnitsRes'},
#                      {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#                      {'label': 'LotFront', 'value': 'LotFront'},
#                      {'label': 'LotDepth', 'value': 'LotDepth'},
#                     {'label': 'BldgFront', 'value': 'BldgFront'},
#                      {'label': 'BldgDepth', 'value': 'BldgDepth'},
#                       {'label': 'BsmtCode', 'value': 'BsmtCode'},
#                      {'label': 'AssessLand', 'value': 'AssessLand'},
#                    {'label': 'AssessTot', 'value': 'AssessTot'},
#
#                  ], clearable= True),
#         html.Br(),
#         html.P('Select a Margin Plot Type'),
# dcc.Dropdown(id='my-marginal', options=[
#                       {'label': 'Box', 'value': 'box'},
#                      {'label': 'Violin', 'value': 'violin'},
#                    {'label': 'Rug', 'value': 'rug'},
#
#                  ], clearable= True),
#         html.Br(),
#         dcc.Graph(id= 'my-graph'),
#         html.Br(),
#         html.Div([
#
#         ])
# ])
#
# @ftp_app2.callback(
#             Output(component_id='my-graph', component_property='figure'),
#             [Input(component_id='my-drop', component_property='value'),
#              Input(component_id='my-marginal', component_property='value')])
#
# def update_Histo(B,C):
#     fig1 = px.histogram(df, x=B, color=df['Borough'], marginal=C)
#     fig1.update_layout(
#         title="Borough Distribution Graph",
#         xaxis_title="Column Values",
#         yaxis_title="Frequency",
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         )
#     )
#     return(fig1)
#
#
# ftp_app2.server.run(debug=True)
# ============= BAR PLOTS/ COUNT PLOT/ CAT PLOT
# ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
# #
# ftp_app2.layout = html.Div(
#     [
#
#         html.P('Select a Column'),
#         dcc.Dropdown(id='my-drop', options=[
#                      {'label': 'LotArea', 'value': 'LotArea'},
#                      {'label': 'BldgArea', 'value': 'BldgArea'},
#                      {'label': 'NumBldgs', 'value': 'NumBldgs'},
#                      {'label': 'NumFloors', 'value': 'NumFloors'},
#                     {'label': 'UnitsRes', 'value': 'UnitsRes'},
#                      {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#                      {'label': 'LotFront', 'value': 'LotFront'},
#                      {'label': 'LotDepth', 'value': 'LotDepth'},
#                     {'label': 'BldgFront', 'value': 'BldgFront'},
#                      {'label': 'BldgDepth', 'value': 'BldgDepth'},
#                       {'label': 'BsmtCode', 'value': 'BsmtCode'},
#                      {'label': 'AssessLand', 'value': 'AssessLand'},
#                    {'label': 'AssessTot', 'value': 'AssessTot'},
#
#                  ], clearable= True),
#         html.Br(),
#
#         dcc.Dropdown(id='my-drop2', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#
#         ], clearable=True),
#         html.Br(),
#         dcc.Graph(id= 'my-graph'),
#         html.Br(),
#         html.Div([
#
#         ])
# ])
#
# @ftp_app2.callback(
#             Output(component_id='my-graph', component_property='figure'),
#             [Input(component_id='my-drop', component_property='value'),
#             Input(component_id='my-drop2', component_property='value')
#              ])
#
# def update_Bar(B, C):
#     fig1 = px.bar(df, x=B, y=C, color=df['Borough'])
#     fig1.update_layout(
#         title="Borough Graph Bar Plot",
#         xaxis_title="Column A Values",
#         yaxis_title="Column B Values",
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         )
#     )
#     return(fig1)

# ftp_app2.server.run(debug=True)

#=======================PIE CHART
# ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
# #
# ftp_app2.layout = html.Div(
#     [
#
#         html.P('Select a Column'),
#         dcc.Dropdown(id='my-drop', options=[
#                      {'label': 'SchoolDist', 'value': 'SchoolDist'},
#                     {'label': 'FireComp', 'value': 'FireComp'},
#                     {'label': 'PolicePrct', 'value': 'PolicePrct'},
#                     {'label': 'HealthArea', 'value': 'HealthArea'},
#                      {'label': 'SanitBoro', 'value': 'SanitBoro'},
#                      {'label': 'NumBldgs', 'value': 'NumBldgs'},
#                      {'label': 'NumFloors', 'value': 'NumFloors'},
#                       {'label': 'BsmtCode', 'value': 'BsmtCode'},
#
#
#                  ], clearable= True),
#         html.Br(),
#
#         html.Br(),
#         dcc.Graph(id= 'my-graph'),
#         html.Br(),
#         html.Div([
#
#         ])
# ])
#
# @ftp_app2.callback(
#             Output(component_id='my-graph', component_property='figure'),
#             [Input(component_id='my-drop', component_property='value')
#              ])
#
# def update_Bar(B):
#     fig1  = px.pie(df, values=B, names='Borough' ,title='Pie Chart by Borough')
#
#     fig1.update_layout(
#         title="Borough Pie Chart",
#         font=dict(
#             family="Courier New, monospace",
#             size=18,
#             color="RebeccaPurple"
#         )
#     )
#     return(fig1)
#
# ftp_app2.server.run(debug=True)

#=================== SCATTER WITH OLS LINE
# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
# #
# ftp_app3.layout = html.Div(
#     [   html.H1('OLS Trend Scatter Plot'),
#         html.P('Desired Predictor For Scatter Plot'),
#         dcc.RadioItems(id='myRad', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ], inline=True),
#         html.Br(),
# html.P('Desired Target For Scatter Plot'),
#     dcc.RadioItems(id='myRad2', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
#         ], inline=True),
#
#     html.Div([dcc.Graph(id='mygraph')
#     ])
#
# ])
# @ftp_app3.callback(
#             Output(component_id='mygraph', component_property='figure'),
#             [Input(component_id='myRad', component_property='value'),
#              Input(component_id='myRad2', component_property='value')])
#
# def update_OLS(a1, b1):
#     fig = px.scatter(df, x=a1, y=b1, color='Borough', trendline="ols",
#                      trendline_scope="overall")
#     return fig

# ftp_app3.server.run(debug=True)

#KDE
# import plotly.figure_factory as ff
# ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
# #
# ftp_app2.layout = html.Div(
#     [
#
#         html.P('Select a Column'),
# dcc.Dropdown(id='my-drop', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
# #
#         ], clearable=True)
#         ,
#         html.Br(),
#         html.Div([dcc.Graph(id='mygraph')
#
# ])
#     ])
#
# @ftp_app2.callback(
#             Output(component_id='mygraph', component_property='figure'),
#             Input(component_id='my-drop', component_property='value'),
#              )
#
# def update_Histo(B):
#     dfQN=df[df['Borough']=='QN']
#     dfMN = df[df['Borough'] == 'MN']
#     dfBK = df[df['Borough'] == 'BK']
#     dfBX = df[df['Borough'] == 'BX']
#     dfSI = df[df['Borough'] == 'SI']
#     GL=['QN','MN','BK','BX','SI']
#     data=[dfQN[B],dfMN[B],dfBK[B],dfBX[B],dfSI[B],]
#
#     fig1 = ff.create_distplot(data, GL)
#     fig1.update_layout(
#             title="Borough Histogram KDE Plot",
#             font=dict(
#                 family="Courier New, monospace",
#                 size=18,
#                 color="RebeccaPurple",
#
#             )
#         )
#     return(fig1)

# ftp_app2.server.run(debug=True)

#============== SUBPLOTS

# ftp_app3= dash.Dash('ftp_app3', external_stylesheets = external_stylesheets)
# #
# ftp_app3.layout = html.Div(
#     [   html.H1('Numerical-Categorical Subplots'),
#         html.P('Desired Numerical Column'),
#         dcc.Dropdown(id='mydrop1', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
# #
#         ], clearable=True),
# dcc.Dropdown(id='mydrop2', options=[
#             {'label': 'LotArea', 'value': 'LotArea'},
#             {'label': 'BldgArea', 'value': 'BldgArea'},
#             {'label': 'NumBldgs', 'value': 'NumBldgs'},
#             {'label': 'NumFloors', 'value': 'NumFloors'},
#             {'label': 'UnitsRes', 'value': 'UnitsRes'},
#             {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#             {'label': 'LotFront', 'value': 'LotFront'},
#             {'label': 'LotDepth', 'value': 'LotDepth'},
#             {'label': 'BldgFront', 'value': 'BldgFront'},
#             {'label': 'BldgDepth', 'value': 'BldgDepth'},
#             {'label': 'BsmtCode', 'value': 'BsmtCode'},
#             {'label': 'AssessLand', 'value': 'AssessLand'},
#             {'label': 'AssessTot', 'value': 'AssessTot'},
# #
#         ], clearable=True),
#
#         html.P('SubSample Size'),
#         dcc.Input(
#             id="Sample Size",
#             type="number",
#             placeholder="Samples"),
#         html.P('SubSample Seed'),
#         dcc.Input(
#             id="Seed",
#             type="number",
#             placeholder="Seed"),
#
#         html.Div([dcc.Graph(id='mygraph')
#     ])
#
# ])
# @ftp_app3.callback(
#             Output(component_id='mygraph', component_property='figure'),
#             [Input(component_id='mydrop1', component_property='value'),
#             Input(component_id='mydrop2', component_property='value'),
#              Input(component_id='Sample Size', component_property='value'),
#              Input(component_id='Seed', component_property='value')])
#
#
# def update_Subplot(a1, b1, c, d):
#     DF=df.sample(n=c, random_state=d)
#     x=df[a1].values
#     y=df[b1].values
#     fig = make_subplots(rows=1, cols=3,
#                         column_widths=[0.4, 0.4, 0.4],
#                         subplot_titles=(f'Scatter of Columns {a1} and {b1}',
#                                         f'Selected Column: {a1}',
#                                         f'Selected Column: {b1}'))
#     for i in range(0, 3):
#         R=0
#         C=0
#         if i == 0:
#             R = 1
#             C = 1
#             fig.add_trace(go.Scatter(x=x, y=y),
#                           row=R, col=C)
#             fig.update_layout(
#                 title="Subplot of 2 Numerical Columns",
#                 legend_title="legend")
#         elif i == 1:
#             R = 1
#             C = 2
#             fig.add_trace(go.Histogram(x=x, nbinsx=50),
#                           row=R, col=C)
#             fig.update_layout(
#                 legend_title="legend")
#         elif i == 2:
#             R = 1
#             C = 3
#             fig.add_trace(go.Histogram(x=y, nbinsx=50),
#                           row=R, col=C)
#             fig.update_layout(
#                 legend_title="legend")
#     return (fig)
#
# ftp_app3.server.run(debug=True)
#
