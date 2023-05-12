import dash
import numpy as np
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app= dash.Dash('My app', external_stylesheets = external_stylesheets)
#Wont run without file
image='network.png'
encoded_image= base64.b64encode(open(imgae, 'rb').read()).decode('ascii')
my_app.layout = html.Div( html.Img(src='data:imag'))