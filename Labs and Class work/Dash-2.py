import numpy as np
import dash as dash
#import dash_core_components as dcc
from dash import dcc
from dash import html
#import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
#See his code for tabs
#Also Double Check why your histogram shows no data
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app= dash.Dash('My app', external_stylesheets = external_stylesheets)

my_app.layout = html.Div(
    [
        dcc.Graph(id= 'my-graph'),
        html.P('Mean'),
        dcc.Slider(id= 'mean', min= -3, max=3, value= 0,
                marks={-3:'-3',-2:'-2', -1: '1', 0: '0', 1:'1',2: '2', 3: '3'}),
        html.Br(),
        html.P('Standard Deviation'),
        dcc.Slider(id= 'std', min= 1, max=3, value= 1,
                   marks={ 1: '1',3: '3'}),
        html.Br(),
        html.P('Number of Samples'),
        dcc.Slider(id= 'size', min = 1, max= 10000, value= 100,
                   marks= { 100:'100', 500:'500',1000:'1000', 5000: '5000', 10000:'10000'}),
        html.Br(),
        html.P("Number of bins"),
        dcc.Dropdown(id= 'bins',
                     options= [
                         {'label':20, 'value':20},
                         {'label':40, 'value':40},
                         {'label':60, 'value':60},
                         {'label':80, 'value':80},
                         {'label':100, 'value':100},
                     ],
                     value= 20,
                     clearable= False)
])

@my_app.callback(
            Output(component_id='my-graph', component_property='figure'),
            [Input(component_id='mean', component_property='value'),
             Input(component_id='std', component_property='value'),
             Input(component_id='size', component_property='value'),
             Input(component_id='bins', component_property='value')
             ]
        )

def update_Ale(a1,a2,a3,a4):
    x= np.random.normal(a1,a2,a3)
    fig= px.histogram(x=x,nbins= a4,range_x= [-5,5], width= 500, height= 500)
    return fig

my_app.server.run(debug=True)
# my_app.run_server(
#     port= 8055,
#     host='0.0.0.0')

# my_app.run_server(debug=True,
#                   port=8040,
#                   host="0.0.0.0")
##=======================================
# my_app.layout = html.Div([
#     html.H1('Complex DV',),
#     dcc.Dropdown(id='my-drop', options=[
#         {'label': 'Intro', 'value': 'Introduction'},
#         {'label': 'Pandas', 'value': 'Pandas '},
#         {'label': 'Seaborn', 'value': 'SNS'},
#         {'label': 'MatPlotLib', 'value': 'MPL'}
#     ],multi='True'),html.Div(id='my-out')
# ])
# my_app.layout= html.Div(
#     [html.H3('Temperature Slider'),dcc.Slider(
#         id='my-slider',
#         min=0, max=100, step=1,
#         value=10)
#         ,html.H1('Heres Output'),
#         html.Br(),html.Br(),
#         html.Div(id='my-out')
#     ])
#
# @my_app.callback(
#     Output(component_id='my-out', component_property='children'),
#     [Input(component_id='my-slider', component_property='value')]
# )
# def update_Alex(input):
#     return(f"The selected Temperature of {input} Farenheit, in Celsius is {(input-32)/1.8} degrees")
# my_app.server.run(debug=True)

##=========================================
# my_app=dash.Dash('My App')
# # my_app.layout = html.Div([
# #     html.H1('Complex DV',),
# #     dcc.Dropdown(id='my-drop', options=[
# #         {'label': 'Intro', 'value': 'Introduction'},
# #         {'label': 'Pandas', 'value': 'Pandas '},
# #         {'label': 'Seaborn', 'value': 'SNS'},
# #         {'label': 'MatPlotLib', 'value': 'MPL'}
# #     ],multi='True'),html.Div(id='my-out')
# # ])
# my_app.layout= html.Div(
#     [html.H3('Temperature Slider'),dcc.Slider(
#         id='my-slider',
#         min=0, max=100, step=1,
#         value=10)
#         ,html.H1('Heres Output'),
#         html.Br(),html.Br(),
#         html.Div(id='my-out')
#     ])
#
# @my_app.callback(
#     Output(component_id='my-out', component_property='children'),
#     [Input(component_id='my-slider', component_property='value')]
# )
# def update_Alex(input):
#     return(f"The selected Temperature of {input} Farenheit, in Celsius is {(input-32)/1.8} degrees")
# my_app.server.run(debug=True)

