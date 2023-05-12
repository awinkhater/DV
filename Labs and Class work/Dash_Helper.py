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
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app= dash.Dash('My app', external_stylesheets = external_stylesheets)
#=================FULL TABs
# my_app = dash.Dash('Homework #4', external_stylesheets=external_stylesheets)
# my_app.layout = html.Div([html.H1('Homework 4', style={'textAlign': 'center'}),
#                             html.Br(),
#                             dcc.Tabs(id='hw-questions',
#                                    children=[
#                                        dcc.Tab(label='Question 1', value='q1'),
#                                        dcc.Tab(label='Question 2', value='q2'),
#                                        dcc.Tab(label='Question 3', value='q3'),
#                                        dcc.Tab(label='Question 4', value='q4'),
#                                        dcc.Tab(label='Question 5', value='q5'),
#                                        dcc.Tab(label='Question 6', value='q6'),
#                                    ]),
#                             html.Div(id='layout')])
# #
# # Question 1
# question1_layout=html.Div(
#     [
#         dcc.Graph(id= 'my-graph1'),
#         html.P("Covid Data of Each Country"),
#         dcc.Dropdown(id= 'countries',
#                      options= [
#                          {'label':'US', 'value':'US'},
#                          {'label':'Brazil', 'value':'Brazil'},
#                          {'label':'UK_Sum', 'value':'UK_sum'},
#                          {'label':'China_Sum', 'value':'China_sum'},
#                          {'label':'India', 'value': 'India'},
#                          {'label':'Italy', 'value': 'Italy'},
#                          {'label':'Germany', 'value': 'Germany'}
#                      ], multi='True',
#                      value= 20,
#                      clearable= True)
# ])
#
# @my_app.callback(
#             Output(component_id='my-graph1', component_property='figure'),
#             [
#              Input(component_id='countries', component_property='value')
#              ]
#         )
#
# def update_covid_graph(a1):
#
#     fig = px.line(data_frame=df, y=a1, x=df.index)
#     return fig
#
#
# # # Question 2
# question2_layout = html.Div(
#     [
#     html.H1('Graph of a(x^2) + bx + c',),
#         dcc.Graph(id= 'my-graph2'),
#         html.P("a"),
#         dcc.Slider(id= 'a', min = -10, max= 10, value= 0.5,
#                    marks= { -10:'-10',
#                             -5:'-5',
#                             -1:'-1',
#                             0: '0',
#                             1:'1',
#                             5:'5',
#                             10:'10'}),
#         html.P("b"),
#         dcc.Slider(id= 'b', min = -10, max= 10, value= 0.5,
#                    marks= { -10:'-10',
#                             -5:'-5',
#                             -1:'-1',
#                             0: '0',
#                             1:'1',
#                             5:'5',
#                             10:'10'}),
#         html.P("c"),
#         dcc.Slider(id= 'c', min = -10, max= 10, value= 0.5,
#                    marks= { -10:'-10',
#                             -5:'-5',
#                             -1:'-1',
#                             0: '0',
#                             1:'1',
#                             5:'5',
#                             10:'10'})
#     ])
#
#
# @my_app.callback(
#             Output(component_id='my-graph2', component_property='figure'),
#             [
#              Input(component_id='a', component_property='value'),
#             Input(component_id='b', component_property='value'),
#             Input(component_id='c', component_property='value')
#              ])
#
# def update_function(a1, b1, c1):
#     x= np.linspace(-2, 2, 1000)
#     y= a1*(x**2) + b1*x+c1
#     fig=px.line(x=x, y=y)
#     return fig
#
# #Question 3
# question3_layout=html.Div(
#     [
#         html.H1('Calculator',),
#         html.P("a"),
#         dcc.Input(
#             id="input_a",
#             type="number",
#             placeholder="First Number"),
#         html.P("b"),
#         dcc.Input(
#             id="input_b",
#             type="number",
#             placeholder="Second Number"),
#         html.P("Operation"),
#         dcc.Dropdown(id= 'op',
#                      options= [
#                          {'label':'+', 'value':'+'},
#                          {'label':'-', 'value':'-'},
#                          {'label':'*', 'value':'*'},
#                          {'label':'/', 'value':'/'},
#                          {'label':'Square', 'value': 'Square'},
#                          {'label':'Sqrt', 'value': 'Sqrt'},
#                          {'label':'log', 'value': 'log'}
#                      ],
#                      clearable= True),
#                     html.Br(),html.Br(),
#                     html.Div(id='my-out3')
#
#     ])
#
#
# @my_app.callback(
#             Output(component_id='my-out3', component_property='children'),
#             [
#              Input(component_id='input_a', component_property='value'),
#             Input(component_id='input_b', component_property='value'),
#             Input(component_id='op', component_property='value')
#              ])
#
# def update_calculator(a1, b1, o):
#     X=a1
#     if o=='+':
#         X= a1+b1
#     elif o=='-':
#         X= a1-b1
#     elif o=='*':
#         X= a1* b1
#     elif o=='/':
#         X= a1/b1
#     elif o=='Square':
#         X= a1**b1
#     elif o== 'Sqrt':
#         if a1 > 0 and b1 > 0:
#             X=a1**(1/b1)
#         else:
#             X="Error"
#     elif o=='log':
#         X= math.log(a1,b1)
#
#     return(f"={X}")
#
# def update_layout(Q):
#     if Q == 'q1':
#         return question1_layout
#     elif Q == 'q2':
#         return question2_layout
#     elif Q == 'q3':
#         return question3_layout
#
#
#
# my_app.server.run(debug=True)



#============



#================Double Plot
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


print("HOOO BOy")

#============= Upload
# import base64
# import datetime
# import io
#
# import dash
# from dash.dependencies import Input, Output, State
# from dash import dcc, html, dash_table
#
# import pandas as pd
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div([
#     dcc.Upload(
#         id='upload-data',
#         children=html.Div([
#             'Drag and Drop or ',
#             html.A('Select Files')
#         ]),
#         style={
#             'width': '100%',
#             'height': '60px',
#             'lineHeight': '60px',
#             'borderWidth': '1px',
#             'borderStyle': 'dashed',
#             'borderRadius': '5px',
#             'textAlign': 'center',
#             'margin': '10px'
#         },
#         # Allow multiple files to be uploaded
#         multiple=True
#     ),
#     html.Div(id='output-data-upload'),
# ])
#
# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')
#
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             # Assume that the user uploaded a CSV file
#             df = pd.read_csv(
#                 io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             # Assume that the user uploaded an excel file
#             df = pd.read_excel(io.BytesIO(decoded))
#     except Exception as e:
#         print(e)
#         return html.Div([
#             'There was an error processing this file.'
#         ])
#
#     return html.Div([
#         html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),
#
#         dash_table.DataTable(
#             df.to_dict('records'),
#             [{'name': i, 'id': i} for i in df.columns]
#         ),
#
#         html.Hr(),  # horizontal line
#
#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
#     ])
#
# @app.callback(Output('output-data-upload', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children
#
# if __name__ == '__main__':
#     app.run_server(debug=True)


#===================== RADIO BUTTONS
# app = Dash(__name__)
#
# app.layout = dcc.RadioItems(['New York City', 'Montreal','San Francisco'], 'Montreal')
#
# if __name__ == "__main__":
#     app.run_server(debug=True)

#================ CHECK BOXES
# from dash import dcc
#
# dcc.Checklist(
#     ['New York City', 'Montréal', 'San Francisco'],
#     ['New York City', 'Montréal']

#====================== DATEPICKER
# dcc.DatePickerRange(
#         id='my-date-picker-range',
#         min_date_allowed=date(1995, 8, 5),
#         max_date_allowed=date(2017, 9, 19),
#         initial_visible_month=date(2017, 8, 5),
#         end_date=date(2017, 8, 25)
#     ),
#     html.Div(id='output-container-date-picker-range')
# ])
#=================Single Value
#    dcc.DatePickerSingle(
#         id='my-date-picker-single',
#         min_date_allowed=date(1995, 8, 5),
#         max_date_allowed=date(2017, 9, 19),
#         initial_visible_month=date(2017, 8, 5),
#         date=date(2017, 8, 25)
#     ),
#     html.Div(id='output-container-date-picker-single')
# ])

#-================================== TEXT AREA
# from dash.dependencies import Input, Output
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     dcc.Textarea(
#         id='textarea-example',
#         value='Textarea content initialized\nwith multiple lines of text',
#         style={'width': '100%', 'height': 300},
#     ),
#     html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
# ])
#
# @app.callback(
#     Output('textarea-example-output', 'children'),
#     Input('textarea-example', 'value')
# )
# def update_output(value):
#     return 'You have entered: \n{}'.format(value)
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
# #================ Stacked Barplotn  b
