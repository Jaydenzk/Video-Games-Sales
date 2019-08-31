import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from app import app
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Jaydenzk/Video-Games-Sales/master/Video_Games_Sales_as_at_22_Dec_2016.csv')
df = df[(df['Platform'] == 'X360') | (df['Platform'] == 'PS3')]

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.

There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smaller size screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Will it be the 'HIT'???

            Now days gaming is at the heart of the entertainment business and console is the most popular machines.
            The Global game markets are growing every year and lot of developers and publisher put their efforts for better perform on Sales
            So, They probabily want to know the game will the hit on each platform.
            Here, it predicts the Global Sales of Genre on each Platform which most of company wants to know about it


            """
        ),


        dcc.Link(dbc.Button('Jump on', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/global.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])
