import dash
from dash import dcc, html, callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate random data for distribution
np.random.seed(42)
n_samples = 1000

# Create sample data
df_dist = pd.DataFrame({
    'sales': np.random.normal(loc=50000, scale=15000, size=n_samples),
    'customer_age': np.random.randint(18, 75, size=n_samples),
    'transaction_value': np.random.exponential(scale=500, size=n_samples),
})

layout = html.Div([
    html.Div([
        html.H1("Distribution Analysis", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '10px'
        }),
        html.P("Explore statistical distributions across different metrics", style={
            'fontSize': '16px',
            'color': '#7f8c8d',
            'marginBottom': '30px'
        })
    ], style={'paddingBottom': '30px', 'borderBottom': '2px solid #ecf0f1'}),
    
    html.Div([
        html.Div([
            html.Label("Select Metric:", style={'fontWeight': 'bold', 'fontSize': '16px', 'marginBottom': '10px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='dist-dropdown',
                options=[
                    {'label': 'Sales Distribution', 'value': 'sales'},
                    {'label': 'Customer Age Distribution', 'value': 'customer_age'},
                    {'label': 'Transaction Value Distribution', 'value': 'transaction_value'}
                ],
                value='sales',
                style={'width': '100%'}
            )
        ], style={
            'width': '35%',
            'display': 'inline-block',
            'marginRight': '2%',
            'padding': '20px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        })
    ], style={'marginBottom': '40px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='histogram-graph')
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'marginRight': '2%',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        }),
        
        html.Div([
            dcc.Graph(id='box-graph')
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        }),
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(id='kde-graph')
        ], style={
            'width': '100%',
            'marginTop': '30px',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        })
    ])
], style={'padding': '40px', 'maxWidth': '1200px', 'margin': '0 auto'})

@callback(
    [Output('histogram-graph', 'figure'),
     Output('box-graph', 'figure'),
     Output('kde-graph', 'figure')],
    Input('dist-dropdown', 'value')
)
def update_distribution_graphs(selected_metric):
    data = df_dist[selected_metric]
    
    # Histogram
    fig_hist = go.Figure(data=[
        go.Histogram(x=data, nbinsx=30, name=selected_metric, marker_color='#3498db')
    ])
    fig_hist.update_layout(
        title=f'Histogram of {selected_metric}',
        xaxis_title=selected_metric,
        yaxis_title='Frequency',
        template='plotly_white'
    )
    
    # Box plot
    fig_box = go.Figure(data=[
        go.Box(y=data, name=selected_metric, marker_color='#e74c3c')
    ])
    fig_box.update_layout(
        title=f'Box Plot of {selected_metric}',
        yaxis_title=selected_metric,
        template='plotly_white'
    )
    
    # KDE (using histogram with cumulative)
    fig_kde = go.Figure(data=[
        go.Histogram(x=data, nbinsx=50, name=selected_metric, 
                    marker_color='#2ecc71', opacity=0.7, 
                    histfunc='count', cumulative_enabled=False)
    ])
    fig_kde.update_layout(
        title=f'Distribution Density of {selected_metric}',
        xaxis_title=selected_metric,
        yaxis_title='Density',
        template='plotly_white',
        barmode='overlay'
    )
    
    return fig_hist, fig_box, fig_kde
