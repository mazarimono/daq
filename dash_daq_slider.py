import dash  
import dash_daq as daq 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Slider(value=7)
], style={"margin":"2%"})

app.run_server(debug=True)