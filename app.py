import dash
from dash import dcc, html, callback, Input, Output
from pages import distribution, aggregation, home

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Analytics Dashboard"

server = app.server  # Expose the server variable for deployments

# Define the app layout
app.layout = html.Div([
    # Navigation Bar
    html.Nav([
        html.Div([
            # Logo/Home
            dcc.Link('📊 Analytics Dashboard', href='/', style={
                'fontSize': '24px',
                'fontWeight': 'bold',
                'color': '#ffffff',
                'textDecoration': 'none',
                'marginRight': 'auto'
            }),
            
            # Navigation Links
            html.Div([
                dcc.Link('Home', href='/', style={
                    'color': '#ecf0f1',
                    'marginRight': '30px',
                    'textDecoration': 'none',
                    'fontSize': '16px',
                    'transition': 'color 0.3s ease'
                }),
                dcc.Link('Distribution', href='/distribution', style={
                    'color': '#ecf0f1',
                    'marginRight': '30px',
                    'textDecoration': 'none',
                    'fontSize': '16px',
                    'transition': 'color 0.3s ease'
                }),
                dcc.Link('Aggregation', href='/aggregation', style={
                    'color': '#ecf0f1',
                    'textDecoration': 'none',
                    'fontSize': '16px',
                    'transition': 'color 0.3s ease'
                }),
            ], style={'display': 'flex', 'alignItems': 'center'})
        ], style={
            'display': 'flex',
            'alignItems': 'center',
            'maxWidth': '1200px',
            'margin': '0 auto',
            'padding': '0 20px'
        })
    ], style={
        'backgroundColor': '#2c3e50',
        'padding': '15px 0',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
        'position': 'sticky',
        'top': '0',
        'zIndex': '1000'
    }),
    
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 'backgroundColor': '#ffffff', 'minHeight': '100vh'})

@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/distribution':
        return distribution.layout
    elif pathname == '/aggregation':
        return aggregation.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
