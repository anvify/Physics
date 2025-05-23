import dash
from dash import html, dcc, Input, Output
import plotly.graph_objs as go
import numpy as np

# Pendulum physics function
def calculate_pendulum(length, mass, angle_deg, time_span=10, dt=0.05):
    g = 9.81
    angle_rad = np.radians(angle_deg)
    t = np.arange(0, time_span, dt)
    theta = angle_rad * np.cos(np.sqrt(g / length) * t)
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    return t, x, y, theta

# Create Dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Interactive Pendulum Simulation"),
    html.Div([
        html.Label('Pendulum Length (m):'),
        dcc.Slider(id='length-slider', min=0.1, max=5, step=0.1, value=1,
                   marks={i: f'{i}' for i in range(1, 6)}),
        html.Label('Pendulum Mass (kg):'),
        dcc.Slider(id='mass-slider', min=0.1, max=10, step=0.1, value=1,
                   marks={i: f'{i}' for i in range(1, 11)}),
        html.Label('Initial Angle (degrees):'),
        dcc.Slider(id='angle-slider', min=1, max=90, step=1, value=30,
                   marks={i: f'{i}°' for i in range(0, 91, 15)}),
    ], style={'width': '50%', 'padding': '20px'}),
    dcc.Graph(id='pendulum-graph')
])

@app.callback(
    Output('pendulum-graph', 'figure'),
    Input('length-slider', 'value'),
    Input('mass-slider', 'value'),
    Input('angle-slider', 'value')
)
def update_graph(length, mass, angle_deg):
    t, x, y, theta = calculate_pendulum(length, mass, angle_deg)
    trace = go.Scatter(x=x, y=y, mode='lines+markers', line=dict(color='blue'), name='Pendulum Path')
    layout = go.Layout(
        title='Pendulum Motion',
        xaxis=dict(title='X Position (m)', scaleanchor='y', scaleratio=1),
        yaxis=dict(title='Y Position (m)'),
        showlegend=False,
        height=600
    )
    return go.Figure(data=[trace], layout=layout)

app.run_server(debug=False)

