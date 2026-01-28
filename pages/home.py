import dash
from dash import dcc, html

layout = html.Div([
    # Hero Section
    html.Div([
        html.Div([
            html.H1("Analytics Dashboard", style={
                'fontSize': '48px',
                'fontWeight': 'bold',
                'color': '#ffffff',
                'marginBottom': '20px'
            }),
            html.P("Explore data insights with interactive visualizations", style={
                'fontSize': '20px',
                'color': '#ecf0f1',
                'marginBottom': '30px'
            }),
            html.Div([
                dcc.Link('View Distribution Analysis', href='/distribution', style={
                    'display': 'inline-block',
                    'backgroundColor': '#3498db',
                    'color': '#ffffff',
                    'padding': '12px 30px',
                    'borderRadius': '5px',
                    'marginRight': '15px',
                    'textDecoration': 'none',
                    'fontSize': '16px',
                    'fontWeight': 'bold',
                    'transition': 'all 0.3s ease'
                }),
                dcc.Link('View Aggregation Analysis', href='/aggregation', style={
                    'display': 'inline-block',
                    'backgroundColor': '#2ecc71',
                    'color': '#ffffff',
                    'padding': '12px 30px',
                    'borderRadius': '5px',
                    'textDecoration': 'none',
                    'fontSize': '16px',
                    'fontWeight': 'bold',
                    'transition': 'all 0.3s ease'
                }),
            ], style={'display': 'flex', 'gap': '15px'})
        ], style={
            'textAlign': 'center',
            'maxWidth': '800px',
            'margin': '0 auto'
        })
    ], style={
        'backgroundColor': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'backgroundImage': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'padding': '100px 20px',
        'textAlign': 'center'
    }),
    
    # Features Section
    html.Div([
        html.H2("Features", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'textAlign': 'center',
            'marginBottom': '50px'
        }),
        
        html.Div([
            # Feature 1
            html.Div([
                html.Div('📊', style={'fontSize': '48px', 'marginBottom': '15px'}),
                html.H3("Distribution Analysis", style={
                    'fontSize': '22px',
                    'fontWeight': 'bold',
                    'color': '#2c3e50',
                    'marginBottom': '10px'
                }),
                html.P("Analyze data distributions with histograms, box plots, and density visualizations. Understand the spread and patterns in your data.", style={
                    'color': '#7f8c8d',
                    'lineHeight': '1.6'
                })
            ], style={
                'width': '30%',
                'display': 'inline-block',
                'textAlign': 'center',
                'padding': '20px',
                'marginRight': '3%'
            }),
            
            # Feature 2
            html.Div([
                html.Div('📈', style={'fontSize': '48px', 'marginBottom': '15px'}),
                html.H3("Aggregation & Trends", style={
                    'fontSize': '22px',
                    'fontWeight': 'bold',
                    'color': '#2c3e50',
                    'marginBottom': '10px'
                }),
                html.P("Group data by multiple dimensions and track trends over time. Create bar charts, pie charts, and time series visualizations.", style={
                    'color': '#7f8c8d',
                    'lineHeight': '1.6'
                })
            ], style={
                'width': '30%',
                'display': 'inline-block',
                'textAlign': 'center',
                'padding': '20px',
                'marginRight': '3%'
            }),
            
            # Feature 3
            html.Div([
                html.Div('🎨', style={'fontSize': '48px', 'marginBottom': '15px'}),
                html.H3("Interactive Visualizations", style={
                    'fontSize': '22px',
                    'fontWeight': 'bold',
                    'color': '#2c3e50',
                    'marginBottom': '10px'
                }),
                html.P("Hover, zoom, and interact with charts. Filter data using dropdowns to customize your analysis in real-time.", style={
                    'color': '#7f8c8d',
                    'lineHeight': '1.6'
                })
            ], style={
                'width': '30%',
                'display': 'inline-block',
                'textAlign': 'center',
                'padding': '20px'
            }),
        ], style={'marginBottom': '40px'})
    ], style={
        'padding': '80px 40px',
        'backgroundColor': '#f8f9fa'
    }),
    
    # About Section
    html.Div([
        html.H2("About This Dashboard", style={
            'fontSize': '36px',
            'fontWeight': 'bold',
            'color': '#2c3e50',
            'marginBottom': '30px'
        }),
        html.Div([
            html.P("This interactive dashboard is built with Python Dash and provides powerful data analysis capabilities.", style={
                'fontSize': '16px',
                'color': '#555555',
                'lineHeight': '1.8',
                'marginBottom': '15px'
            }),
            html.P("Whether you're analyzing sales data, customer behavior, or market trends, this tool helps you extract meaningful insights with beautiful, interactive visualizations.", style={
                'fontSize': '16px',
                'color': '#555555',
                'lineHeight': '1.8',
                'marginBottom': '15px'
            }),
            html.Ul([
                html.Li("Built with Dash, Plotly, Pandas, and NumPy", style={'marginBottom': '10px'}),
                html.Li("Interactive charts with hover, zoom, and filter capabilities", style={'marginBottom': '10px'}),
                html.Li("Multiple analysis pages for different use cases", style={'marginBottom': '10px'}),
                html.Li("Random sample data for demonstration purposes", style={'marginBottom': '10px'}),
            ], style={'color': '#555555', 'lineHeight': '1.8'})
        ], style={'maxWidth': '600px'})
    ], style={
        'padding': '80px 40px',
        'maxWidth': '900px',
        'margin': '0 auto'
    }),
    
    # CTA Section
    html.Div([
        html.H2("Get Started", style={
            'fontSize': '32px',
            'fontWeight': 'bold',
            'color': '#ffffff',
            'textAlign': 'center',
            'marginBottom': '30px'
        }),
        html.P("Choose an analysis to explore the data:", style={
            'fontSize': '18px',
            'color': '#ecf0f1',
            'textAlign': 'center',
            'marginBottom': '40px'
        }),
        html.Div([
            dcc.Link('Distribution Analysis', href='/distribution', style={
                'display': 'inline-block',
                'backgroundColor': '#3498db',
                'color': '#ffffff',
                'padding': '15px 40px',
                'borderRadius': '5px',
                'marginRight': '20px',
                'textDecoration': 'none',
                'fontSize': '16px',
                'fontWeight': 'bold'
            }),
            dcc.Link('Aggregation Analysis', href='/aggregation', style={
                'display': 'inline-block',
                'backgroundColor': '#2ecc71',
                'color': '#ffffff',
                'padding': '15px 40px',
                'borderRadius': '5px',
                'textDecoration': 'none',
                'fontSize': '16px',
                'fontWeight': 'bold'
            }),
        ], style={'textAlign': 'center'})
    ], style={
        'backgroundColor': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'backgroundImage': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'padding': '80px 40px',
        'textAlign': 'center'
    }),
    
    # Footer
    html.Footer([
        html.Div([
            html.P("© 2024 Analytics Dashboard. Built with Dash & Plotly.", style={
                'color': '#7f8c8d',
                'textAlign': 'center',
                'marginBottom': '0'
            })
        ], style={'paddingTop': '20px', 'borderTop': '1px solid #ecf0f1'})
    ], style={
        'padding': '40px',
        'backgroundColor': '#f8f9fa',
        'textAlign': 'center'
    })
], style={'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'})
