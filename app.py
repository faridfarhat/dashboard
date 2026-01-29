import dash
from dash import dcc, html, callback, Input, Output
from pages import overview, aggregation, distribution

# Minimal Dash app exposing only overview, aggregation and distribution pages
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Analytics Dashboard"

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Overview', href='/', style={'marginRight': '20px'}),
        dcc.Link('Aggregation', href='/aggregation', style={'marginRight': '20px'}),
        dcc.Link('Distribution', href='/distribution')
    ], style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderBottom': '1px solid #ecf0f1'}),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/aggregation':
        return aggregation.layout
    elif pathname == '/distribution':
        return distribution.layout
    else:
        return overview.layout


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
