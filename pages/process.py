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

            ## Process

            The Data set was from the Kaggle on Videos Games Sales with Ratings.
            The data set has 16719 rows x 19 columns and it was looks good for me to work out but the problem on this data set was there's way too many null values on it

            Critic_Score       8582

            Critic_Count       8582

            User_Score         6704

            User_Count         9129

            Developer          6623

            Rating             6769

            This is how much null value this dataset has. It is more than 50% of the data has null value that it took a lot of time and effort to clear this data.
            However, at the end, I just drop the all null values to just focus on relationship between Global Sales, Genre and Platform
            Also, in the Platform column, some of the Platform was way too outdated or got few games that We decide to drop it
            For the future process, keep in mind drop the data set in this manner can cause huge leakage on my model which is not going to give good outcome.

            My model is RandomForestRegressor to predict.

            """
        ),

    ],
)

layout = dbc.Row([column1])
