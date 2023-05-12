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

#Prepping Dataset
url='https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/CONVENIENT_global_confirmed_cases.csv'
df=pd.read_csv('CONVENIENT_global_confirmed_cases.csv')
df=df.dropna()
#NEW COLUMNS
df['China_sum'] = df.iloc[0:,57:90].astype(float).sum(axis=1)
columns=df.columns
df['UK_sum'] = df.iloc[0:,249:260].astype(float).sum(axis=1)
df['Country/Region'] = pd.to_datetime(df['Country/Region'])
df=df.set_index('Country/Region')

from scipy.fft import fft
from numpy import random

import base64
def logsig(n):
 return (1/(1+(np.e**-n)))
image = 'network.png'
encoded_image = base64.b64encode(open(image, 'rb').read()).decode('ascii')

#REAL ONE
my_app = dash.Dash('Homework #4', external_stylesheets=external_stylesheets)
my_app.layout = html.Div([html.H1('Homework 4', style={'textAlign': 'center'}),
                            html.Br(),
                            dcc.Tabs(id='hw-questions',
                                   children=[
                                       dcc.Tab(label='Question 1', value='q1'),
                                       dcc.Tab(label='Question 2', value='q2'),
                                       dcc.Tab(label='Question 3', value='q3'),
                                       dcc.Tab(label='Question 4', value='q4'),
                                       dcc.Tab(label='Question 5', value='q5'),
                                       dcc.Tab(label='Question 6', value='q6'),
                                   ]),
                            html.Div(id='layout')])
#
# Question 1
question1_layout=html.Div(
    [
        dcc.Graph(id= 'my-graph1'),
        html.P("Covid Data of Each Country"),
        dcc.Dropdown(id= 'countries',
                     options= [
                         {'label':'US', 'value':'US'},
                         {'label':'Brazil', 'value':'Brazil'},
                         {'label':'UK_Sum', 'value':'UK_sum'},
                         {'label':'China_Sum', 'value':'China_sum'},
                         {'label':'India', 'value': 'India'},
                         {'label':'Italy', 'value': 'Italy'},
                         {'label':'Germany', 'value': 'Germany'}
                     ], multi='True',
                     value= 20,
                     clearable= True)
])

@my_app.callback(
            Output(component_id='my-graph1', component_property='figure'),
            [
             Input(component_id='countries', component_property='value')
             ]
        )

def update_covid_graph(a1):

    fig = px.line(data_frame=df, y=a1, x=df.index)
    return fig


# # Question 2
question2_layout = html.Div(
    [
    html.H1('Graph of a(x^2) + bx + c',),
        dcc.Graph(id= 'my-graph2'),
        html.P("a"),
        dcc.Slider(id= 'a', min = -10, max= 10, value= 0.5,
                   marks= { -10:'-10',
                            -5:'-5',
                            -1:'-1',
                            0: '0',
                            1:'1',
                            5:'5',
                            10:'10'}),
        html.P("b"),
        dcc.Slider(id= 'b', min = -10, max= 10, value= 0.5,
                   marks= { -10:'-10',
                            -5:'-5',
                            -1:'-1',
                            0: '0',
                            1:'1',
                            5:'5',
                            10:'10'}),
        html.P("c"),
        dcc.Slider(id= 'c', min = -10, max= 10, value= 0.5,
                   marks= { -10:'-10',
                            -5:'-5',
                            -1:'-1',
                            0: '0',
                            1:'1',
                            5:'5',
                            10:'10'})
    ])


@my_app.callback(
            Output(component_id='my-graph2', component_property='figure'),
            [
             Input(component_id='a', component_property='value'),
            Input(component_id='b', component_property='value'),
            Input(component_id='c', component_property='value')
             ])

def update_function(a1, b1, c1):
    x= np.linspace(-2, 2, 1000)
    y= a1*(x**2) + b1*x+c1
    fig=px.line(x=x, y=y)
    return fig

#Question 3
question3_layout=html.Div(
    [
        html.H1('Calculator',),
        html.P("a"),
        dcc.Input(
            id="input_a",
            type="number",
            placeholder="First Number"),
        html.P("b"),
        dcc.Input(
            id="input_b",
            type="number",
            placeholder="Second Number"),
        html.P("Operation"),
        dcc.Dropdown(id= 'op',
                     options= [
                         {'label':'+', 'value':'+'},
                         {'label':'-', 'value':'-'},
                         {'label':'*', 'value':'*'},
                         {'label':'/', 'value':'/'},
                         {'label':'Square', 'value': 'Square'},
                         {'label':'Sqrt', 'value': 'Sqrt'},
                         {'label':'log', 'value': 'log'}
                     ],
                     clearable= True),
                    html.Br(),html.Br(),
                    html.Div(id='my-out3')

    ])


@my_app.callback(
            Output(component_id='my-out3', component_property='children'),
            [
             Input(component_id='input_a', component_property='value'),
            Input(component_id='input_b', component_property='value'),
            Input(component_id='op', component_property='value')
             ])

def update_calculator(a1, b1, o):
    X=a1
    if o=='+':
        X= a1+b1
    elif o=='-':
        X= a1-b1
    elif o=='*':
        X= a1* b1
    elif o=='/':
        X= a1/b1
    elif o=='Square':
        X= a1**b1
    elif o== 'Sqrt':
        if a1 > 0 and b1 > 0:
            X=a1**(1/b1)
        else:
            X="Error"
    elif o=='log':
        X= math.log(a1,b1)

    return(f"={X}")

#Question 4
question4_layout= html.Div(
    [
        html.H1('Polynomial Grapher',),
        html.P("Polynomial Degree"),
        dcc.Input(
            id="degree",
            type="number",
            placeholder="Degree of Polynomial"),
            html.Br(),html.Br(),
            dcc.Graph(id= 'my-graph4')

    ])


@my_app.callback(
            Output(component_id='my-graph4', component_property='figure'),
            [
             Input(component_id='degree', component_property='value')])

def update_poly(a1):
    x= np.linspace(-2,2, 1000)
    y=x**a1
    fig=px.line(x=x, y=y)
    return(fig)


#Q5
question5_layout=html.Div(
    [
        html.H1('Sine Grapher',),
        html.P("Please Enter Sine Wave Frequency"),
        dcc.Input(
            id="freq",
            type="number",
            placeholder="Frequency of Sin Wave"),
            html.P("Please Enter Mean of White Noise"),
            dcc.Input(
                id="wnm",
                type="number",
                placeholder="White Noise Mean"),
            html.P("Please Enter SD of White Noise"),
                    dcc.Input(
                        id="wnsd",
                        type="number",
                        placeholder="White Noise SD"),
            html.P("Please Enter Number of Samples"),
                    dcc.Input(
                        id="samp",
                        type="number",
                        placeholder="Samples"),
            html.Br(),html.Br(),
            dcc.Graph(id= 'my-graph5')

    ])


@my_app.callback(
            Output(component_id='my-graph5', component_property='figure'),
            [
             Input(component_id='freq', component_property='value'),
            Input(component_id='wnm', component_property='value'),
            Input(component_id='wnsd', component_property='value'),
            Input(component_id='samp', component_property='value')])

def update_sin(a1, b1, c1, d1):
   w = random.normal(loc=b1, scale=c1, size=(1, d1))[0]
   x = np.linspace(-np.pi, np.pi, d1)
   y = (np.sin(a1*x)) + w
   yft = fft(y)
   yft = [c.real for c in yft]
   fig = make_subplots(rows=2, cols=1,
                       column_widths=[0.5], subplot_titles=('Sin with Noise', 'Fast Fourier Transformation of Above Function'))
   for i in range(0, 2):
      C = 1
      R = i + 1
      if i == 0:
         fig.add_trace(go.Scatter(x=x, y=y),
                       row=R, col=C)
         fig.update_layout(
            title="Sine Wave with White Noise",
            legend_title="legend")
      elif i == 1:
         fig.add_trace(go.Scatter(x=x, y=yft),
                       row=R, col=C)
         fig.update_layout(
            title="Sine Wave with White Noise",
            legend_title="legend")
   return(fig)

#Q6
question6_layout= html.Div([
    html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                                        style={'height':'40%','width':'40%'})])
                 ,
        html.H1('Interactive Neural Network Ouput Graph',),
        dcc.Graph(id = 'my-graph6'),
        html.P('b1_1'),
        dcc.Slider(id= 'b1_1', min = -10, max= 10, value= 1,
                   marks= {  -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'}),
        html.P('b1_2'),
        dcc.Slider(id= 'b1_2', min = -10, max= 10, value= 1,
                   marks= {  -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'}),

        html.P('W1_1'),
        dcc.Slider(id= 'W1_1', min = -10, max= 10, value= 1,
                   marks= {  -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'
                            }),

        html.P('W1_2'),
        dcc.Slider(id= 'W1_2', min = -10, max= 10, value= 1,
                   marks= {  -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'}),
        html.P('W2_1'),
        dcc.Slider(id= 'W2_1', min = -10, max= 10, value= 1,
                   marks= {  -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'}),
        html.P('W2_2'),
        dcc.Slider(id='W2_2', min=-10, max=10, value=1,
                marks={ -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'}),

        html.P('b2_1'),
        dcc.Slider(id='b2_1', min=-10, max=10, value=1,
               marks={ -10:'-10', -9: '-9', -8 : '-8', -7:'-7', -6: '-6',
                            -5:'-5', -4:'-4', -3:'-3', -2:'-2', -1:'-1',
                            0: '0',
                            1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
                            6:'6', 7:'7', 8:'8', 9:'9',10:'10'})
])
@my_app.callback(
            Output(component_id='my-graph6', component_property='figure'),
            [
            Input(component_id='b1_1', component_property='value'),
            Input(component_id='b1_2', component_property='value'),
            Input(component_id='W1_1', component_property='value'),
            Input(component_id='W1_2', component_property='value'),
            Input(component_id='W2_1', component_property='value'),
            Input(component_id='W2_2', component_property='value'),
            Input(component_id='b2_1', component_property='value')
            ])


def update_NN(b11, b12, w11, w12, w21, w22, b21):
    p=np.linspace(-5,5,1000)
    a1_1= logsig(w11*p + b11)
    a1_2=logsig(w12*p +b12)
    a2=w21*a1_1 + w22*a1_2+b21
    fig=px.line(x=p, y=a2)
    return fig

@my_app.callback(Output(component_id='layout', component_property='children'),
                 [Input(component_id='hw-questions', component_property='value')])

def update_layout(Q):
    if Q == 'q1':
        return question1_layout
    elif Q == 'q2':
        return question2_layout
    elif Q == 'q3':
        return question3_layout
    elif Q == 'q4':
        return question4_layout
    elif Q == 'q5':
        return question5_layout
    elif Q == 'q6':
        return question6_layout

my_app.server.run(debug=True)