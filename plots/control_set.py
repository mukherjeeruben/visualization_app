import dash_core_components as dcc
import dash_html_components as html
import config


def set_control():
    input_controls = html.Div([html.Div(children='''Select Count of Data Set'''),
                               dcc.Dropdown(id="dropdown2",
                                            options=[{"label": x['chunk'], "value": x['chunk']} for x in config.chunk_set],
                                            value=None,
                                            clearable=False),
                               html.Div(children='''Select Year'''),
                               dcc.Dropdown(id="dropdown1",
                                             options=[{"label": x['year'], "value": x['year']} for x in config.query_year],
                                             value=None,
                                             clearable=False)
                               ])
    return input_controls

