import dash
from dash import dcc, html, callback, Input, Output
import plotly.graph_objs as go
import pandas as pd
from data import df_main

layout = html.Div([
    html.Div([
        html.H1("Sales Aggregation & Analysis", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '10px'
        }),
        html.P("Group and analyze sales data across multiple dimensions", style={
            'fontSize': '16px',
            'color': '#7f8c8d',
            'marginBottom': '30px'
        })
    ], style={'paddingBottom': '30px', 'borderBottom': '2px solid #ecf0f1'}),
    
    html.Div([
        html.Div([
            html.Label("Group By:", style={'fontWeight': 'bold', 'fontSize': '14px', 'marginBottom': '8px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='agg-group-dropdown',
                options=[
                    {'label': 'By Region', 'value': 'Region'},
                    {'label': 'By Month', 'value': 'Month_Name'},
                    {'label': 'By Day of Week', 'value': 'Day_of_Week'},
                    {'label': 'By Product', 'value': 'ProductKey'},
                    {'label': 'By Quarter', 'value': 'Quarter'},
                    {'label': 'By Country', 'value': 'Country'},
                    {'label': 'By Continent', 'value': 'Continent'}
                ],
                value='Region',
                style={'width': '100%'}
            )
        ], style={
            'width': '32%',
            'display': 'inline-block',
            'marginRight': '2%',
            'padding': '15px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        }),
        
        html.Div([
            html.Label("Metric:", style={'fontWeight': 'bold', 'fontSize': '14px', 'marginBottom': '8px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='agg-metric-dropdown',
                options=[
                    {'label': 'Total Sales Value', 'value': 'EstimatedSalesValue'},
                    {'label': 'Total Quantity', 'value': 'OrderQuantity'},
                    {'label': 'Order Count', 'value': 'OrderNumber'}
                ],
                value='EstimatedSalesValue',
                style={'width': '100%'}
            )
        ], style={
            'width': '32%',
            'display': 'inline-block',
            'marginRight': '2%',
            'padding': '15px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        }),
        
        html.Div([
            html.Label("Filter by Region (Optional):", style={'fontWeight': 'bold', 'fontSize': '14px', 'marginBottom': '8px', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='agg-region-filter',
                options=[{'label': 'All Regions', 'value': 'all'}] + 
                        [{'label': region, 'value': region} for region in sorted(df_main['Region'].unique())],
                value='all',
                style={'width': '100%'}
            )
        ], style={
            'width': '32%',
            'display': 'inline-block',
            'padding': '15px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '8px'
        })
    ], style={'marginBottom': '30px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='agg-bar-graph')
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
            dcc.Graph(id='agg-pie-graph')
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
            dcc.Graph(id='agg-line-graph')
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
            dcc.Graph(id='agg-table-graph')
        ], style={
            'width': '100%',
            'marginTop': '30px',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        })
    ])
], style={'padding': '40px', 'maxWidth': '1400px', 'margin': '0 auto'})

@callback(
    [Output('agg-bar-graph', 'figure'),
     Output('agg-pie-graph', 'figure'),
     Output('agg-line-graph', 'figure'),
     Output('agg-table-graph', 'figure')],
    [Input('agg-group-dropdown', 'value'),
     Input('agg-metric-dropdown', 'value'),
     Input('agg-region-filter', 'value')]
)
def update_aggregation_graphs(group_by, metric, region_filter):
    # Filter data based on region selection
    df_filtered = df_main.copy()
    if region_filter != 'all':
        df_filtered = df_filtered[df_filtered['Region'] == region_filter]
    
    # Handle metric aggregation
    if metric == 'OrderNumber':
        # Count unique order numbers
        agg_data = df_filtered.groupby(group_by).size().reset_index(name='value')
    else:
        agg_data = df_filtered.groupby(group_by)[metric].sum().reset_index()
        agg_data.columns = [group_by, 'value']
    
    agg_data = agg_data.sort_values('value', ascending=False)
    
    # Format metric name for display
    metric_display = {
        'EstimatedSalesValue': 'Sales Value',
        'OrderQuantity': 'Quantity',
        'OrderNumber': 'Order Count'
    }.get(metric, metric)
    
    # Bar chart
    fig_bar = go.Figure(data=[
        go.Bar(x=agg_data[group_by], y=agg_data['value'], 
               marker_color='#3498db',
               text=agg_data['value'].apply(lambda x: f'{x:,.0f}'),
               textposition='auto')
    ])
    fig_bar.update_layout(
        title=f'Total {metric_display} by {group_by}',
        xaxis_title=group_by,
        yaxis_title=f'Total {metric_display}',
        template='plotly_white',
        hovermode='x unified'
    )
    
    # Pie chart
    fig_pie = go.Figure(data=[
        go.Pie(labels=agg_data[group_by], values=agg_data['value'])
    ])
    fig_pie.update_layout(
        title=f'Distribution of {metric_display} by {group_by}',
        template='plotly_white'
    )
    
    # Line chart (by date or month)
    if group_by in ['Month_Name', 'Day_of_Week']:
        # Group by date for time series
        daily_agg = df_filtered.groupby('OrderDate')[metric if metric != 'OrderNumber' else 'OrderQuantity'].sum().reset_index()
        daily_agg = daily_agg.sort_values('OrderDate')
        
        fig_line = go.Figure(data=[
            go.Scatter(x=daily_agg['OrderDate'], 
                      y=daily_agg[daily_agg.columns[1]], 
                      mode='lines+markers',
                      name=metric_display, 
                      line=dict(color='#2ecc71', width=2),
                      marker=dict(size=4))
        ])
        fig_line.update_layout(
            title=f'Daily {metric_display} Trend',
            xaxis_title='Date',
            yaxis_title=f'{metric_display}',
            template='plotly_white',
            hovermode='x unified'
        )
    else:
        # Bar chart as line won't make sense for categorical
        fig_line = go.Figure(data=[
            go.Bar(x=agg_data[group_by], y=agg_data['value'], marker_color='#2ecc71')
        ])
        fig_line.update_layout(
            title=f'{metric_display} by {group_by} (Sorted)',
            xaxis_title=group_by,
            yaxis_title=f'{metric_display}',
            template='plotly_white'
        )
    
    # Summary table
    summary_table = agg_data.copy()
    summary_table['percentage'] = (summary_table['value'] / summary_table['value'].sum() * 100).round(2)
    summary_table.columns = [group_by, metric_display, 'Percentage (%)']
    
    fig_table = go.Figure(data=[
        go.Table(
            header=dict(
                values=['<b>' + col + '</b>' for col in summary_table.columns],
                fill_color='#3498db',
                align='left',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[summary_table[col] for col in summary_table.columns],
                fill_color='#ecf0f1',
                align='left',
                height=25
            )
        )
    ])
    fig_table.update_layout(
        title=f'Summary: {metric_display} by {group_by}',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    return fig_bar, fig_pie, fig_line, fig_table
