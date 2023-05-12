import numpy as np
import pandas as pd
import plotly.express as px
from plotly import graph_objects as go
#LOAD DATA
# df=px.data.iris()
# tips=px.data.tips()
#==========
#Boxplot
# fig=px.box(tips,
#            x= 'day',
#            y='total_bill')
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")
#===========
#Histogram
# fig = go.Figure(go.Histogram(y=df['sepal_width'], nbinsx=40))
#
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")


# feature = df.columns[:-2]
# fig= px.histogram(data_frame=tips,x='total_bill', color='day', marginal='box')
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")
#===========
#Scatter
# fig=px.scatter_matrix(data_frame=df, dimensions=feature, color='species', title='Scatter Matrix')
# fig.update_traces(diagonal_visible = False)
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")
#===========
#Bar Plot/ Font
# fig=px.bar(data_frame=df,
#            x='total_bill',
#            y='day',
#            color='sex',
#            barmode='group',
#            title="Tips Dataset Barplot")
# fig.update_layout(width=1200, height=800,
#                   autosize= False,
#                   template='plotly_dark',
#                   font_family= 'Courier New',
#                   font_color= 'green',
#                   title_font_family='Times New Roman',
#                   title_font_size=20,
#                   title_font_color='red',
#                   legend_title_font_size=20)
# fig.show(renderer="browser")
#============
#Line Plot
# col=stocks.columns
# fig=px.line(data_frame=stocks, x='date', y=['FB', 'AMZN', 'GOOG', 'AAPL', 'NFLX', 'FB', 'MSFT'])
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")
#==============
#Basic Math Plot
# x=np.linspace(-np.pi, np.pi, 1000)
# y1=np.sin(x)
# y2=np.cos(x)
# fig=px.line(x=x, y=[y1, y2])
# fig.update_layout(width=500, height=500, autosize= False)
# fig.show(renderer="browser")
#==========
#Double Plot
#B='Numfloors'
#fig1 = px.scatter(data_frame=df, y=B, x=df.index)
#     x = np.linspace(0, len(df), len(df))
#     Y = df[B].mean() + (3 * df[B].std())
#     y = [Y] * (len(df))
#     fig2 = px.line(y=y, x=x)
#     fig2.update_traces(line_color='#FF5733', line_width=5)
#     fig3 = go.Figure(data=fig1.data + fig2.data)
#     return (fig3)
#=============
#Scatter Plot With Regression Line
# df = px.data.tips()
# fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
# fig.show()
#==============
#Subplot
# col2=df_2.columns[:4]
#
# fig = make_subplots(rows=4, cols=1)
# for i in range(len(col2)):
#     C= 1
#     R= i+1
#     print (C, R)
#     fig.add_trace(go.Histogram(x=df_2[col2[i]],  nbinsx=50, name=col2[i]),
#                     row=R, col=C)
#     fig.update_layout(
#         title="Stock Post PCA Histogram Subplot",
#         legend_title="legend")
#
# fig.show()
#=========
#Scatter Matrix
# fig = px.scatter_matrix(stocks,
#     dimensions=col,
#     title="Original Feature Space",
#     labels={col:col.replace('_', ' ') for col in col}) # remove underscore
# fig.update_traces(diagonal_visible=False)
# fig.show()
#==========
#Pie Chart
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()
#============
#ANIMATION
# df=px.data.gapminder()
# df_2007 = df.query('year==2007')
# df_canada= df.query("country=='Canada'")
    # fig=px.scatter(data_frame=df,
    #                x= 'gdpPercap',
    #                y= 'lifeExp',
    #                color='continent',
    #                size='pop',
    #                hover_name='country',
    #                #log_x=True,
    #                size_max=60,
    #                animation_frame='year',
    #                animation_group='country',
    #                range_x= [25, 50000],
    #                range_y=[25,91]
    #                #,facet_col='continent',
    #                )
    # fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
    # fig.show(renderer="browser")

