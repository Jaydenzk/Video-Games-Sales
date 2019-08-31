import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Insights


            """
        ),

        html.Br(),

        dcc.Markdown(
            """
            ## __How it works?__

            """
        ),

        html.Br(),

        dcc.Markdown(
            """
            Let's begin with model's permutaion importance. This chart shows which features weight the most in the model's Platform
            """
        ),

        html.Img(src='assets/permu.png', className='img-fluid'),

        dcc.Markdown(
            """
            The permutation importance shows JP and Other weight the most while Global and EU weight much less than Publisher.
            It looks little bit odds to me because Global Sales is what add up NA EU JP and Other so, we will keep in mind this for later.
            """
        ),

        html.Img(src='assets/pdp1.png', className='img-fluid'),


        dcc.Markdown(
            """
            The pdpbox looks very interesting here. At the permutation importance, the feature heavily weight on JP and Other but pdpbox shows different way.
            The global shows positive trend lines which means Global will have positive impact on predict the model for sure.
            """
        )
    ],
    md=4,
)

layout = dbc.Row([column1])
