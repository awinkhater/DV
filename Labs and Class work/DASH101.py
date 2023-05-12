import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#NEED
#Yeah the 'as dash' is necessary
import dash as dash
import dash_core_components as dcc
import dash_html_components as html

# my_app= dash.Dash('My App')
# #H1 is Title (largest font)
# my_app.layout = html.Div([html.H1('hello world! with h1.html', style= {'textAlign': 'center'}),
#                         html.Div(html.H2('hello world! with h2.html',style= {'textAlign': 'center'})),
#                         html.Div(html.H3('hello world! with h3.html',style= {'textAlign': 'center'})),
#                         html.Div(html.H4('hello world! with h4.html',style= {'textAlign': 'center'})),
#
# ]
# )
# my_app.server.run(debug=True)
#==============
my_app= dash.Dash('My App')
my_app.layout= html.Div([html.H1('Assignment 1'),
                         html.Button('Submit Assignment 1', id= 'Assignment1'), html.H2('Assignment 2'),
                         html.Button('Submit Assignment 2', id= 'Assignment2')])


my_app.server.run(debug=True)