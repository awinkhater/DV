import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy import stats
#Dash
import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

#
# # PART 1.1 Initial Dataset merge
# csv_files=['BK.csv','BX.csv','MN.csv','QN.csv','SI.csv']
# l = []
# for f in csv_files:
#     l.append(pd.read_csv(f))
# # #
# df_raw = pd.concat(l, ignore_index=True)
# df_raw
# #
# # print(len(df_raw))
# # df_raw.to_csv('NY_PLUTO.csv')
# #
# # PART 1.2 Initial Dataset read
#
df_raw=pd.read_csv('NY_PLUTO.csv')
df_raw.set_index(df_raw.columns[0])
# #TAKING ONLY THE MOST USEFUL COLUMNS
df_raw= df_raw[['Borough', 'Lot', 'SchoolDist',
                'Council','ZipCode','FireComp',
                'PolicePrct','HealthArea','SanitBoro',
                'Address', 'BldgClass',
                'LotArea', 'BldgArea', 'NumBldgs',
                'NumFloors', 'UnitsRes', 'UnitsTotal',
                'LotFront', 'LotDepth', 'BldgFront',
                'BldgDepth', 'LotType', 'BsmtCode', 'AssessLand', 'AssessTot']]
#
# print(df_raw.isna().sum())
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# ftp_app1= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)
#
# ftp_app1.layout = html.Div(
#     [
#         html.P('Null Counts'),
#         dcc.Dropdown(id='my-drop', options=[
#                      {'label': 'LotArea', 'value': 'LotArea'},
#                      {'label': 'BldgArea', 'value': 'BldgArea '},
#                      {'label': 'NumBldgs', 'value': 'NumBldgs'},
#                      {'label': 'NumFloors', 'value': 'NumFloors'},
#                     {'label': 'UnitsRes', 'value': 'UnitsRes'},
#                      {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
#                      {'label': 'LotFront', 'value': 'LotFront'},
#                      {'label': 'LotDepth', 'value': 'LotDepth'},
#                     {'label': 'BldgFront', 'value': 'BldgFront'},
#                      {'label': 'BldgDepth', 'value': 'BldgDepth'},
#                     {'label': 'Borough', 'value': 'Borough'},
#                     {'label': 'Lot', 'value': 'Lot'},
#                     {'label': 'SchoolDist', 'value': 'SchoolDist'},
#                     {'label': 'Council', 'value': 'Council'},
#                     {'label': 'ZipCode', 'value': 'ZipCode'},
#                     {'label': 'FireComp', 'value': 'FireComp'},
#                     {'label': 'PolicePrct', 'value': 'PolicePrct'},
#                     {'label': 'Health Area', 'value': 'HealthArea'},
#                     {'label': 'SanitBoro', 'value': 'SanitBoro'},
#                     {'label': 'Address', 'value': 'Address'},
#                     {'label': 'BldgClass', 'value': 'BldgClass'},
#                       {'label': 'BsmtCode', 'value': 'BsmtCode'},
#                      {'label': 'AssessLand', 'value': 'AssessLand'},
#                    {'label': 'AssessTot', 'value': 'AssessTot'},
#                  ], value= 20,
#                      clearable= True), html.Div(id='my-out') ])
# #
# #
# @ftp_app1.callback(
#             Output(component_id='my-out', component_property='children'),
#             [Input(component_id='my-drop', component_property='value')])
#
# def update_nulls(B):
#     N=df_raw[B].isna().sum()
#     return (f"There are {N} Null Values in the {B} column of the raw dataset")
#
# ftp_app1.server.run(debug=True)
#
#
# #We can afford to drop the null values dataset

predf=df_raw.dropna()
# # #Take a Manageable subset





# # 1.3
# # Outliers
#
# #Using IQR
def remove_outliers(df, columns):
    for col in columns:

        Q3 = df[col].quantile(.75)
        Q1 = df[col].quantile(.25)
        IQR= Q3-Q1
        df = df[(df[col] <= Q3+(1.5 * IQR))]
        df = df[(df[col] >= Q1 - (1.5 * IQR))]
    return (df)
#
# #
# #
#
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
ftp_app2= dash.Dash('ftp_app1', external_stylesheets = external_stylesheets)

ftp_app2.layout = html.Div(
    [
        dcc.Graph(id= 'my-graph'),
        html.P('Outlier Distribution'),
        dcc.Dropdown(id='my-drop', options=[
                     {'label': 'LotArea', 'value': 'LotArea'},
                     {'label': 'BldgArea', 'value': 'BldgArea'},
                     {'label': 'NumBldgs', 'value': 'NumBldgs'},
                     {'label': 'NumFloors', 'value': 'NumFloors'},
                    {'label': 'UnitsRes', 'value': 'UnitsRes'},
                     {'label': 'UnitsTotal', 'value': 'UnitsTotal'},
                     {'label': 'LotFront', 'value': 'LotFront'},
                     {'label': 'LotDepth', 'value': 'LotDepth'},
                    {'label': 'BldgFront', 'value': 'BldgFront'},
                     {'label': 'BldgDepth', 'value': 'BldgDepth'},
                      {'label': 'BsmtCode', 'value': 'BsmtCode'},
                     {'label': 'AssessLand', 'value': 'AssessLand'},
                   {'label': 'AssessTot', 'value': 'AssessTot'},

                 ], value= 20,
                     clearable= True)])
#
#
@ftp_app2.callback(
            Output(component_id='my-graph', component_property='figure'),
            [Input(component_id='my-drop', component_property='value')])

def update_outliers(B):
    fig1 = px.scatter(data_frame=predf, y=B, x=predf.index)
    x = np.linspace(0, len(predf), len(predf))
    IQR = predf[B].quantile(.75) - predf[B].quantile(.25)
    Y = predf[B].quantile(.75) + (1.5 * IQR)
    y = [Y] * len(x)
    fig2 = px.line(y=y, x=x)
    fig2.update_traces(line_color='#FF5733', line_width=1)

    Z = predf[B].quantile(.25) - (1.5 * IQR)
    z = [Z] * len(x)
    fig3 = px.line(y=z, x=x)
    fig3.update_traces(line_color='#FFA500', line_width=1)

    fig4 = go.Figure(data=fig1.data + fig2.data + fig3.data)
    fig4.update_layout(
        title="Variable IQR Visualizer: Red and Orange Lines are IQR Bounds",
        xaxis_title="Index Values",
        yaxis_title="Column Values",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    return(fig4)
ftp_app2.server.run(debug=True)
#
#




# predf=remove_outliers(predf, ['LotArea', 'BldgArea', 'NumBldgs',
#                 'NumFloors', 'UnitsRes', 'UnitsTotal',
#                 'LotFront', 'LotDepth', 'BldgFront',
#                 'BldgDepth','BsmtCode', 'AssessLand', 'AssessTot'])
# predf = predf.sample(n=60000, random_state=10)
#
# # # #SAVING THE CLEAN DATASET
# predf.to_csv('FTPDataset.csv')
