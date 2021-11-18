import dash_core_components as dcc
import dash_html_components as html


def set_control():
    input_controls = html.Div([html.H6("Change the value in the text box to see callbacks in action!"),
                        html.Div(["Input: ",
                        dcc.Input(id='my-input', value='initial value', type='text')]),
                        html.Br(),
                        html.Div(id='my-output'),])

    return input_controls


def output_set(input_value):
    return 'Output: {}'.format(input_value)