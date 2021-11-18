import dash
from plots.page_base import set_page_base
from dash.dependencies import Input, Output
from plots.control_set import output_set
import config

dash_app = dash.Dash(__name__)
server = dash_app.server
dash_app.layout = set_page_base()


@dash_app.callback(Output(component_id='my-output', component_property='children'),
            Input(component_id='my-input', component_property='value'))
def update_output_div(input_value):
    return output_set(input_value)


if __name__ == '__main__':
    dash_app.run_server(debug=config.debug)
