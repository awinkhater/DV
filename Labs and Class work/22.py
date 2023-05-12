import plotly.express as px
import numpy as np
from pandas_datareader import data
import yfinance as yf
yf.pdr_override()
import seaborn as sns
import plotly.graph_objects as go
#In built data set
#Need Violin Plot too (maybe see power point)
df=px.data.iris()
tips=px.data.tips()

fig=px.box(tips,
           x= 'day',
           y='total_bill')
fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
fig.show(renderer="browser")


#SEE HIS NOTES FOR THE PIE CHART

# fig = go.Figure(go.Histogram(y=df['sepal_width'], nbinsx=40))
#
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")


# feature = df.columns[:-2]
# fig= px.histogram(data_frame=tips,x='total_bill', color='day', marginal='box')
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")



# fig=px.scatter_matrix(data_frame=df, dimensions=feature, color='species', title='Scatter Matrix')
# fig.update_traces(diagonal_visible = False)
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")
# df= px.data.tips()
# fig=px.bar(data_frame=df,
# #            x='total_bill',
# #            y='day',
# #            color='sex',
# #            barmode='group',
# #            title="Tips Dataset Barplot")
# # fig.update_layout(width=1200, height=800,
# #                   autosize= False,
# #                   template='plotly_dark',
# #                   font_family= 'Courier New',
# #                   font_color= 'green',
# #                   title_font_family='Times New Roman',
# #                   title_font_size=20,
# #                   title_font_color='red',
# #                   legend_title_font_size=20)
# # fig.show(renderer="browser")

# df=px.data.iris()
# fig=px.bar(data_frame=df,
#            x='sepal_width',
#            y='sepal_length',
#            color='species',
#            barmode='stack',
#            labels={'sepal_length': 'Sepal Length (cm)',
#                    'sepal_width': 'Sepal Width (cm)',
#                    'species': 'Species for Iris'},
#            title="Iris Dataset Barplot")
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



# df=px.data.iris()
# fig=px.bar(data_frame=df, x='species', y=['sepal_length', 'sepal_width', ' petal_length', 'petal_width'])
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")


# df=sns.load_dataset('flights')
# fig=px.line(data_frame=df, x= 'year', y='passengers', color='month')
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")



# stocks=px.data.stocks()
# col=stocks.columns
# fig=px.line(data_frame=stocks, x='date', y=['FB', 'AMZN', 'GOOG', 'AAPL', 'NFLX', 'FB', 'MSFT'])
# fig.update_layout(width=1200, height=800, autosize= False, template='plotly_dark')
# fig.show(renderer="browser")


# start_date="2000-01-01"
# end_date="2023-03-22"
# stocks=['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
# df = data.get_data_yahoo(stocks[0], start=start_date, end=end_date)
#
# fig= px.line(data_frame=df,
#              x=df.index,
#              y=['Open', 'Close', 'High', 'Low', 'Adj Close'],
#              title="Apple Stock Price")
# fig.update_layout(width=1200, height=800, autosize= False)
# fig.show(renderer="browser")
#
#


#Graphing Sin and Cosine
# x=np.linspace(-np.pi, np.pi, 1000)
# y1=np.sin(x)
# y2=np.cos(x)
# fig=px.line(x=x, y=[y1, y2])
# fig.update_layout(width=500, height=500, autosize= False)
# fig.show(renderer="browser")