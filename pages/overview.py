import dash
from dash import dcc, html, callback, Input, Output, dash_table
import plotly.graph_objs as go
import pandas as pd
from data import df_main, get_summary_stats, get_first_rows

layout = html.Div([
    html.Div([
        html.H1("Dashboard Overview", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '10px'
        }),
        html.P("Dataset Summary & Key Metrics", style={
            'fontSize': '16px',
            'color': '#7f8c8d',
            'marginBottom': '30px'
        })
    ], style={'paddingBottom': '30px', 'borderBottom': '2px solid #ecf0f1'}),
    
    # Summary Statistics Cards
    html.Div(id='summary-cards-container', style={'marginBottom': '40px'}),
    
    # Data Sample
    html.Div([
        html.H2("First 5 Rows of Data", style={
            'fontSize': '20px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '15px'
        }),
            html.Div(id='data-sample-table-container', style={
                'backgroundColor': '#ffffff',
                'borderRadius': '8px',
                'padding': '10px'
            })
    ], style={'marginBottom': '40px'}),
    
    # Key Visualizations
    html.Div([
        html.H2("Top Regions by Sales", style={
            'fontSize': '20px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '15px'
        }),
        html.Div([
            html.Div([
                dcc.Graph(id='overview-region-bar')
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
                dcc.Graph(id='overview-region-pie')
            ], style={
                'width': '48%',
                'display': 'inline-block',
                'backgroundColor': '#ffffff',
                'borderRadius': '8px',
                'padding': '15px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
            })
        ])
    ], style={'marginBottom': '40px'}),
    
    # Monthly Trend
    html.Div([
        html.H2("Sales Trend Over Time", style={
            'fontSize': '20px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '15px'
        }),
        html.Div([
            dcc.Graph(id='overview-monthly-trend')
        ], style={
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        })
    ], style={'marginBottom': '40px'}),
    
    # Customer and Product Insights
    html.Div([
        html.Div([
            html.H2("Top 10 Products by Orders", style={
                'fontSize': '20px',
                'fontWeight': 'bold',
                'color': '#2c3e50',
                'marginBottom': '15px'
            }),
            dcc.Graph(id='overview-top-products')
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
            html.H2("Order Distribution by Day", style={
                'fontSize': '20px',
                'fontWeight': 'bold',
                'color': '#2c3e50',
                'marginBottom': '15px'
            }),
            dcc.Graph(id='overview-day-distribution')
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px',
            'padding': '15px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
        })
    ])
], style={'padding': '40px', 'maxWidth': '1400px', 'margin': '0 auto'})

@callback(
    [Output('summary-cards-container', 'children'),
     Output('data-sample-table-container', 'children'),
     Output('overview-region-bar', 'figure'),
     Output('overview-region-pie', 'figure'),
     Output('overview-monthly-trend', 'figure'),
     Output('overview-top-products', 'figure'),
     Output('overview-day-distribution', 'figure')],
    [Input('summary-cards-container', 'id')]
)
def update_overview(container_id):
    # Get summary stats
    stats = get_summary_stats()
    
    # Create summary cards
    cards = html.Div([
        html.Div([
            html.Div([
                html.H3(f"{stats['total_orders']:,}", style={'color': '#3498db', 'margin': '0'}),
                html.P("Total Orders", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center'})
        ], style={'width': '19%', 'display': 'inline-block', 'marginRight': '1%', 'padding': '20px', 
                  'backgroundColor': '#ecf0f1', 'borderRadius': '8px', 'textAlign': 'center'}),
        
        html.Div([
            html.Div([
                html.H3(f"{stats['total_quantity']:,}", style={'color': '#2ecc71', 'margin': '0'}),
                html.P("Total Items Ordered", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center'})
        ], style={'width': '19%', 'display': 'inline-block', 'marginRight': '1%', 'padding': '20px', 
                  'backgroundColor': '#ecf0f1', 'borderRadius': '8px', 'textAlign': 'center'}),
        
        html.Div([
            html.Div([
                html.H3(stats['total_sales_value'], style={'color': '#e74c3c', 'margin': '0', 'fontSize': '18px'}),
                html.P("Total Sales Value", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center'})
        ], style={'width': '19%', 'display': 'inline-block', 'marginRight': '1%', 'padding': '20px', 
                  'backgroundColor': '#ecf0f1', 'borderRadius': '8px', 'textAlign': 'center'}),
        
        html.Div([
            html.Div([
                html.H3(f"{stats['unique_customers']:,}", style={'color': '#f39c12', 'margin': '0'}),
                html.P("Unique Customers", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center'})
        ], style={'width': '19%', 'display': 'inline-block', 'marginRight': '1%', 'padding': '20px', 
                  'backgroundColor': '#ecf0f1', 'borderRadius': '8px', 'textAlign': 'center'}),
        
        html.Div([
            html.Div([
                html.H3(f"{stats['unique_territories']}", style={'color': '#9b59b6', 'margin': '0'}),
                html.P("Regions", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center'})
        ], style={'width': '19%', 'display': 'inline-block', 'padding': '20px', 
                  'backgroundColor': '#ecf0f1', 'borderRadius': '8px', 'textAlign': 'center'})
    ], style={'marginBottom': '20px'})
    
    # Create data sample DataTable showing all columns with horizontal scroll
    first_rows = get_first_rows(5)
    data_table = dash_table.DataTable(
        id='data-sample-table',
        columns=[{'name': col, 'id': col} for col in first_rows.columns],
        data=first_rows.to_dict('records'),
        page_size=5,
        style_table={'overflowX': 'auto', 'maxWidth': '100%'},
        style_cell={'textAlign': 'left', 'minWidth': '120px', 'whiteSpace': 'normal'},
        style_header={'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'},
        style_data={'backgroundColor': '#ecf0f1'}
    )
    
    # Regional analysis
    regional_data = df_main.groupby('Region').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique'
    }).reset_index().sort_values('EstimatedSalesValue', ascending=False)
    
    fig_region_bar = go.Figure(data=[
        go.Bar(x=regional_data['Region'], y=regional_data['EstimatedSalesValue'], 
               marker_color='#3498db', text=regional_data['EstimatedSalesValue'].apply(lambda x: f'${x:,.0f}'),
               textposition='auto')
    ])
    fig_region_bar.update_layout(
        title='Total Sales by Region',
        xaxis_title='Region',
        yaxis_title='Sales Value',
        template='plotly_white'
    )
    
    fig_region_pie = go.Figure(data=[
        go.Pie(labels=regional_data['Region'], values=regional_data['EstimatedSalesValue'])
    ])
    fig_region_pie.update_layout(
        title='Sales Distribution by Region',
        template='plotly_white'
    )
    
    # Monthly trend
    monthly_data = df_main.groupby('Month_Name').agg({
        'EstimatedSalesValue': 'sum',
        'OrderNumber': 'nunique'
    }).reset_index()
    
    # Order months correctly
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    monthly_data['Month_Name'] = pd.Categorical(monthly_data['Month_Name'], categories=month_order, ordered=True)
    monthly_data = monthly_data.sort_values('Month_Name')
    
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Scatter(
        x=monthly_data['Month_Name'], 
        y=monthly_data['EstimatedSalesValue'],
        mode='lines+markers',
        name='Sales Value',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8)
    ))
    fig_monthly.add_trace(go.Scatter(
        x=monthly_data['Month_Name'],
        y=monthly_data['OrderNumber'],
        mode='lines+markers',
        name='Order Count',
        yaxis='y2',
        line=dict(color='#e74c3c', width=3),
        marker=dict(size=8)
    ))
    fig_monthly.update_layout(
        title='Monthly Sales and Order Trend',
        xaxis_title='Month',
        yaxis_title='Sales Value',
        yaxis2=dict(title='Order Count', overlaying='y', side='right'),
        template='plotly_white',
        hovermode='x unified'
    )
    
    # Top products
    product_data = df_main.groupby('ProductKey').agg({
        'OrderNumber': 'nunique'
    }).reset_index().sort_values('OrderNumber', ascending=False).head(10)
    
    fig_products = go.Figure(data=[
        go.Bar(x=product_data['OrderNumber'], y=product_data['ProductKey'].astype(str), 
               orientation='h', marker_color='#2ecc71',
               text=product_data['OrderNumber'], textposition='auto')
    ])
    fig_products.update_layout(
        title='Top 10 Products by Order Count',
        xaxis_title='Number of Orders',
        yaxis_title='Product Key',
        template='plotly_white',
        showlegend=False
    )
    
    # Day of week distribution
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_data = df_main.groupby('Day_of_Week').agg({
        'OrderNumber': 'nunique'
    }).reset_index()
    day_data['Day_of_Week'] = pd.Categorical(day_data['Day_of_Week'], categories=day_order, ordered=True)
    day_data = day_data.sort_values('Day_of_Week')
    
    fig_day = go.Figure(data=[
        go.Bar(x=day_data['Day_of_Week'], y=day_data['OrderNumber'], 
               marker_color='#f39c12')
    ])
    fig_day.update_layout(
        title='Order Distribution by Day of Week',
        xaxis_title='Day of Week',
        yaxis_title='Number of Orders',
        template='plotly_white'
    )
    
    return cards, data_table, fig_region_bar, fig_region_pie, fig_monthly, fig_products, fig_day
