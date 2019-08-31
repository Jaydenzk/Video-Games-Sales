import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from joblib import load
pipeline = load('assets/pipeline.joblib')
model = pipeline

from app import app


column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions
            """
            ),

        html.Br(),

        dcc.Markdown('#### Platform'),
        dcc.Dropdown(
            id='Platform',
            options=[
                {'label': 'PS2', 'value': 'PS2'},
                {'label': 'DS', 'value': 'DS'},
                {'label': 'PS3', 'value': 'PS3'},
                {'label': 'Wii', 'value': 'Wii'},
                {'label': 'X360', 'value': 'X360'},
                {'label': 'PSP', 'value': 'PSP'},
                {'label': 'PS', 'value': 'PS'},
                {'label': 'PC', 'value': 'PC'},
                {'label': 'XB', 'value': 'XB'},
                {'label': 'GBA', 'value': 'GBA'},
                {'label': 'GC', 'value': 'GC'},
                {'label': '3DS', 'value': '3DS'},
                {'label': 'PSV', 'value': 'PSV'},
                {'label': 'PS4', 'value': 'PS4'},
                {'label': 'N64', 'value': 'N64'},
                {'label': 'XOne', 'value': 'XOne'},
                {'label': 'SNES', 'value': 'SNES'},
                {'label': 'SAT', 'value': 'SAT'},
                {'label': 'WiiU', 'value': 'WiiU'},
                {'label': '2600', 'value': '2600'},
                {'label': 'GB', 'value': 'GB'},
                {'label': 'NES', 'value': 'NES'},
                {'label': 'DC', 'value': 'DC'},
                {'label': 'GEN', 'value': 'GEN'},
                {'label': 'NG', 'value': 'NG'},
            ],
            value=''
        ),

        html.Br(),

        dcc.Markdown('#### Genre'),
        dcc.Dropdown(
            id='Genre',
            options=[
                {'label': 'Action', 'value': 'Action'},
                {'label': 'Sports', 'value': 'Sports'},
                {'label': 'Misc', 'value': 'Misc'},
                {'label': 'Role-Playing', 'value': 'Role-Playing'},
                {'label': 'Shooter', 'value': 'Shooter'},
                {'label': 'Adventure', 'value': 'Adventure'},
                {'label': 'Racing', 'value': 'Racing'},
                {'label': 'Platform', 'value': 'Platform'},
                {'label': 'Simulation', 'value': 'Simulation'},
                {'label': 'Fighting', 'value': 'Fighting'},
                {'label': 'Strategy', 'value': 'Strategy'},
                {'label': 'Puzzle', 'value': 'Puzzle'},
            ],
            value=''
        ),

      ],
      md=4,
)

column2 = dbc.Col(
    [
        html.H2('Video Games Sales Prediction', className='mb-5'),

        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Platform', 'value'),
     Input('Genre', 'value'),
     ]
)

def predict(Platform, Genre):

    row = pd.DataFrame(
        columns=['Platform', 'Genre'],
        data=[[Platform, Genre]]
    )

    y_pred = round(model.predict(row)[0] * 100, 2)

    label = f'Sales prediction chances are likely {y_pred}%'

    output = daq.Gauge(
             id='Prediction-Sales',
             label=label,
             color="3346FF",
             showCurrentValue=True,
             value=y_pred,
             min=0,
             max=200,
             units="%")

    print(f'{label}')


    return output
