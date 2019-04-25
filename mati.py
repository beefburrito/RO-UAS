import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd 
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression as LR
from sklearn.datasets import make_regression
from dash.dependencies import Input, Output


df = pd.read_csv('athlete_events.csv', engine='python')

indo = df["NOC"] == "INA"
yr1 = df["Year"] == 1956
yr2 = df["Year"] == 1960
yr3 = df["Year"] == 1964
yr4 = df["Year"] == 1968
yr5 = df["Year"] == 1972
yr6 = df["Year"] == 1976
yr7 = df["Year"] == 1980
yr8 = df["Year"] == 1984
yr9 = df["Year"] == 1988
yr10 = df["Year"] == 1992
yr11 = df["Year"] == 1996
yr12 = df["Year"] == 2000
yr13 = df["Year"] == 2004
yr14 = df["Year"] == 2008
yr15 = df["Year"] == 2012
yr16 = df["Year"] == 2016
gold = df["Medal"] == "Gold"
silver = df["Medal"] == "Silver"
bronze = df["Medal"] == "Bronze"
none = df["Medal"] == "NA"
swim = df["Sport"] == "Swimming"
badminton = df["Sport"] == "Badminton"

#Athletes
temp = df[indo & yr1]
a1 = temp.Year.count()
temp = df[indo & yr2]
a2 = temp.Year.count()
temp = df[indo & yr3]
a3 = temp.Year.count()
temp = df[indo & yr4]
a4 = temp.Year.count()
temp = df[indo & yr5]
a5 = temp.Year.count()
temp = df[indo & yr6]
a6 = temp.Year.count()
temp = df[indo & yr7]
a7 = temp.Year.count()
temp = df[indo & yr8]
a8 = temp.Year.count()
temp = df[indo & yr9]
a9 = temp.Year.count()
temp = df[indo & yr10]
a10 = temp.Year.count()
temp = df[indo & yr11]
a11 = temp.Year.count()
temp = df[indo & yr12]
a12 = temp.Year.count()
temp = df[indo & yr13]
a13 = temp.Year.count()
temp = df[indo & yr14]
a14 = temp.Year.count()
temp = df[indo & yr15]
a15 = temp.Year.count()
temp = df[indo & yr16]
a16 = temp.Year.count()

#Gold Medal

temp = df[indo & yr1 & gold]
g1 = temp.Year.count()
temp = df[indo & yr2 & gold]
g2 = temp.Year.count()
temp = df[indo & yr3 & gold]
g3 = temp.Year.count()
temp = df[indo & yr4 & gold]
g4 = temp.Year.count()
temp = df[indo & yr5 & gold]
g5 = temp.Year.count()
temp = df[indo & yr6 & gold]
g6 = temp.Year.count()
temp = df[indo & yr7 & gold]
g7 = temp.Year.count()
temp = df[indo & yr8 & gold]
g8 = temp.Year.count()
temp = df[indo & yr9 & gold]
g9 = temp.Year.count()
temp = df[indo & yr10 & gold]
g10 = temp.Year.count()
temp = df[indo & yr11 & gold]
g11 = temp.Year.count()
temp = df[indo & yr12 & gold]
g12 = temp.Year.count()
temp = df[indo & yr13 & gold]
g13 = temp.Year.count()
temp = df[indo & yr14 & gold]
g14 = temp.Year.count()
temp = df[indo & yr15 & gold]
g15 = temp.Year.count()
temp = df[indo & yr16 & gold]
g16 = temp.Year.count()

#Silver Medal
temp = df[indo & yr1 & silver]
s1 = temp.Year.count()
temp = df[indo & yr2 & silver]
s2 = temp.Year.count()
temp = df[indo & yr3 & silver]
s3 = temp.Year.count()
temp = df[indo & yr4 & silver]
s4 = temp.Year.count()
temp = df[indo & yr5 & silver]
s5 = temp.Year.count()
temp = df[indo & yr6 & silver]
s6 = temp.Year.count()
temp = df[indo & yr7 & silver]
s7 = temp.Year.count()
temp = df[indo & yr8 & silver]
s8 = temp.Year.count()
temp = df[indo & yr9 & silver]
s9 = temp.Year.count()
temp = df[indo & yr10 & silver]
s10 = temp.Year.count()
temp = df[indo & yr11 & silver]
s11 = temp.Year.count()
temp = df[indo & yr12 & silver]
s12 = temp.Year.count()
temp = df[indo & yr13 & silver]
s13 = temp.Year.count()
temp = df[indo & yr14 & silver]
s14 = temp.Year.count()
temp = df[indo & yr15 & silver]
s15 = temp.Year.count()
temp = df[indo & yr16 & silver]
s16 = temp.Year.count()

#Bronze Medal
temp = df[indo & yr1 & bronze]
b1 = temp.Year.count()
temp = df[indo & yr2 & bronze]
b2 = temp.Year.count()
temp = df[indo & yr3 & bronze]
b3 = temp.Year.count()
temp = df[indo & yr4 & bronze]
b4 = temp.Year.count()
temp = df[indo & yr5 & bronze]
b5 = temp.Year.count()
temp = df[indo & yr6 & bronze]
b6 = temp.Year.count()
temp = df[indo & yr7 & bronze]
b7 = temp.Year.count()
temp = df[indo & yr8 & bronze]
b8 = temp.Year.count()
temp = df[indo & yr9 & bronze]
b9 = temp.Year.count()
temp = df[indo & yr10 & bronze]
b10 = temp.Year.count()
temp = df[indo & yr11 & bronze]
b11 = temp.Year.count()
temp = df[indo & yr12 & bronze]
b12 = temp.Year.count()
temp = df[indo & yr13 & bronze]
b13 = temp.Year.count()
temp = df[indo & yr14 & bronze]
b14 = temp.Year.count()
temp = df[indo & yr15 & bronze]
b15 = temp.Year.count()
temp = df[indo & yr16 & bronze]
b16 = temp.Year.count()
sports = [df[gold & indo & badminton].NOC.count(),df[gold & indo & swim].NOC.count()]
YearSlide=[]
YSlide=[]
for i in range(1956,2100,4):
    YearSlide.append(i)
for i in range(0,144,4):
    YSlide.append(i*(1/30))
app = dash.Dash()

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'goldbar': '#FFDF00',
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='How many gold medals will Indonesia win?',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Data Analysis', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Number of Indonesian athletes throughout the years',
        figure={
            'data': [
                {'x': [1956, 1960, 1964, 1968,1972,1976,1980,1984,1988,1992,
1996,2000,2004,2008,2012,2016], 'y': [a1, a2, a3, a4, a5, a6, a7, a8, a9,a10,a11,a12,a13,a14,a15,a16],'type':'bar','name':'Participants'},
                  {'x': [1956, 1960, 1968,1972,1976,1984,1988,1992,
1996,2000,2004,2008,2012,2016], 'y': [g1, g2, g4, g5, g6, g8, g9,g10,g11,g12,g13,g14,g15,g16],'color':'yellow', 'type': 'bar','mode':'markers', 'name': 'Gold'},
            ],
            'layout': go.Layout(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Amount of athletes'},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                #hovermode='closest''
            )
        }
    ),
    dcc.Graph(
            id='graph',
            figure=go.Figure(
                data=[
                    go.Pie(labels = ['Badminton','Swimming'],
                        values = sports,
                        name = "Gold medals won in sports",
                        marker = {'colors':['rgb(150,123,255)','rgb(100,200,100)']}
                        )
                ],
                layout=go.Layout(
                    title = 'Gold medals won by Sports'
                )
            )
        ),
    html.Div(children='Linear Regression', style={
        'textAlign': 'center',
        'color': colors['text']
    }),    
   dcc.Graph(
        id='Medal Prediction',
        figure={
            'data': [
                {'x': [1956, 1960, 1968,1972,1976,1984,1988,1992,
1996,2000,2004,2008,2012,2016], 'y': [g1, g2, g4, g5, g6, g8, g9,g10,g11,g12,g13,g14,g15,g16],'color':'yellow', 'type': 'scatter','mode':'markers', 'name': 'Gold'},
                {'x': YearSlide,'y':YSlide,'mode':'line','name':'Predicted medal won'}
            ],
            'layout': {
                ''
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    html.Div(children='MAE = 0.604214', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

           
])


if __name__ == '__main__':
    app.run_server()