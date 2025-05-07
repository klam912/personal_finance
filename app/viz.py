import supabase
from app.supabase_client import supabase
from flask import current_app
import pandas as pd
import plotly.graph_objects as go
import plotly
import json

def monthly_summary():
    """Query the data and create a side-by-side barplot showing income and spending per month"""
    response = supabase.table("monthly_summary").select("*").execute()

    # Create a Pandas df
    monthly_summary_json = response.data[0]
    monthly_summary_df = pd.DataFrame(data=[monthly_summary_json])
    
    print(monthly_summary_df)

    # Change the month name
    monthy_num_to_name = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    monthly_summary_df['month'] = monthly_summary_df['month'].astype(str).map(monthy_num_to_name)


    # Create a side-by-side barplot with income/spending per month
    fig = go.Figure(data=[
        go.Bar(name='Income',x=monthly_summary_df['month'],y=monthly_summary_df['total_income'],
               hovertemplate='Month: %{x}<br>Income: $%{y}<br><extra></extra>'
               ),
        go.Bar(name='Spending',x=monthly_summary_df['month'],y=monthly_summary_df['total_spending'],
                hovertemplate='Month: %{x}<br>Spending: $%{y}<br><extra></extra>'
)
    ])

    # Fix the figure's layout
    fig.update_layout(
        barmode='group',
        # title='Monthly Income vs. Spending',
        xaxis_title='Month',
        yaxis_title='$'
        # xaxis_tickangle=45
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON