import dash
from dash import dcc, html, callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate random data for aggregation
np.random.seed(42)
n_samples = 365

# Create sample data with dates and categories
dates = pd.date_range(start='2023-01-01', periods=n_samples, freq='D')
categories = np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], size=n_samples)

df_agg = pd.DataFrame({
    'date': dates,
    'category': categories,
    'sales': np.random.uniform(1000, 10000, size=n_samples),
    'quantity': np.random.randint(10, 100, size=n_samples),
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=n_samples)
})

# Add month and day of week columns
df_agg['month'] = df_agg['date'].dt.month
df_agg['day_of_week'] = df_agg['date'].dt.day_name()

layout = html.Div([
    html.Div([
        html.H1("Aggregation & Trends Analysis", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '10px'
        }),
        html.P("Group data and analyze trends across different dimensions", style={
            'fontSize': '16px',
            'color': '#7f8c8d',
            'marginBottom': '30px'
        })
    ], style={'paddingBottom': '30px', 'borderBottom': '2px solid #ecf0f1'}),
    
    html.Div([
        html.Div([
            html.Label("Group By:", style={'fontWeight': 'bold', 'fontSize': '16px', 'marginBottom': '10px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='agg-dropdown',
                options=[
                    {'label': 'By Category', 'value': 'category'},
                    {'label': 'By Region', 'value': 'region'},
                    {'label': 'By Month', 'value': 'month'},
                    {'label': 'By Day of Week', 'value': 'day_of_week'}
                ],
                value='category',
                style={'width': '100%'}
            )
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'marginRight': '2%',
            'padding': '20px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        }),
        
        html.Div([
            html.Label("Metric:", style={'fontWeight': 'bold', 'fontSize': '16px', 'marginBottom': '10px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Total Sales', 'value': 'sales'},
                    {'label': 'Total Quantity', 'value': 'quantity'}
                ],
                value='sales',
                style={'width': '100%'}
            )
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'padding': '20px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        })
    ], style={'marginBottom': '40px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='bar-graph')
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
            dcc.Graph(id='pie-graph')
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
            dcc.Graph(id='line-graph')
        ], style={
            'width': '100%',
            'marginTop': '30px',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        })
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(id='table-graph')
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
    [Output('bar-graph', 'figure'),
     Output('pie-graph', 'figure'),
     Output('line-graph', 'figure'),
     Output('table-graph', 'figure')],
    [Input('agg-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_aggregation_graphs(group_by, metric):
    # Aggregate data
    agg_data = df_agg.groupby(group_by)[metric].sum().reset_index()
    agg_data.columns = [group_by, 'value']
    
    # Bar chart
    fig_bar = go.Figure(data=[
        go.Bar(x=agg_data[group_by], y=agg_data['value'], marker_color='#3498db')
    ])
    fig_bar.update_layout(
        title=f'Total {metric} by {group_by}',
        xaxis_title=group_by,
        yaxis_title=f'Total {metric}',
        template='plotly_white'
    )
    
    # Pie chart
    fig_pie = go.Figure(data=[
        go.Pie(labels=agg_data[group_by], values=agg_data['value'])
    ])
    fig_pie.update_layout(
        title=f'Distribution of {metric} by {group_by}',
        template='plotly_white'
    )
    
    # Time series line chart
    daily_agg = df_agg.groupby('date')[metric].sum().reset_index()
    fig_line = go.Figure(data=[
        go.Scatter(x=daily_agg['date'], y=daily_agg[metric], mode='lines', 
                  name=metric, line=dict(color='#2ecc71', width=2))
    ])
    fig_line.update_layout(
        title=f'Daily {metric} Trend',
        xaxis_title='Date',
        yaxis_title=f'{metric}',
        template='plotly_white'
    )
    
    # Summary table
    summary_table = agg_data.copy()
    summary_table['percentage'] = (summary_table['value'] / summary_table['value'].sum() * 100).round(2)
    
    fig_table = go.Figure(data=[
        go.Table(
            header=dict(
                values=[group_by, f'Total {metric}', 'Percentage (%)'],
                fill_color='#3498db',
                align='left',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[summary_table[group_by], summary_table['value'].round(2), summary_table['percentage']],
                fill_color='#ecf0f1',
                align='left'
            )
        )
    ])
    fig_table.update_layout(
        title=f'Summary Table: {metric} by {group_by}',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    return fig_bar, fig_pie, fig_line, fig_table
