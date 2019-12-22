import dash 
import dash_html_components as html 
import dash_daq as daq

margin_style = {"margin": "10%"}

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.BooleanSwitch(on=True, style=margin_style),
    daq.ColorPicker(style=margin_style),
    daq.Gauge(value=7, style=margin_style),
    daq.GraduatedBar(value=7, style=margin_style),
    daq.Indicator(size=30, style=margin_style),
    daq.Joystick(style=margin_style),
    daq.Knob(value=7, style=margin_style),
    daq.LEDDisplay(value=2.19475, style=margin_style),
    daq.NumericInput(max=100, value=42, style=margin_style),
    daq.PowerButton(size=100, style=margin_style),
    daq.PrecisionInput(value=47563826347, style=margin_style),
    daq.StopButton(size=100, style=margin_style),
    daq.Tank(value=7, showCurrentValue=True, units="リットル", style=margin_style),
    daq.Thermometer(min=0, max=40, value=17, showCurrentValue=True, color="red", units="C", style=margin_style),
    daq.ToggleSwitch(size=100, color="red", style=margin_style),

])

if __name__ == "__main__":
    app.run_server(debug=True)
