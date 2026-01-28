import dash
from dash import dcc, html, callback, Input, Output
from pages import aggregation, distribution

# Minimal Dash app exposing only aggregation and distribution pages
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Analytics Dashboard"

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Aggregation', href='/aggregation', style={'marginRight': '20px'}),
        dcc.Link('Distribution', href='/distribution')
    ], style={'padding': '10px', 'backgroundColor': '#f8f9fa'}),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/distribution':
        return distribution.layout
    else:
        return aggregation.layout


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
