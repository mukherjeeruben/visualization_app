import dash_core_components as dcc
import dash_html_components as html
import config


def set_control():
    input_controls = html.Div(children=[
                               dcc.Dropdown(id="dropdown2",
                                            options=[{"label": x['chunk'], "value": x['chunk']} for x in config.chunk_set],
                                            value=None,
                                            clearable=False,
                                            searchable=False,
                                            placeholder="Select Chunk Count",
                                            style={'background-color': '#f9f9f9',
                                                   'color': '#189AB4',
                                                   'min-width': '200px',
                                                   'font-size': '14px',
                                                   'font-family': 'sans-serif',
                                                   'cursor': 'pointer',
                                                   'padding': '5px'}),
                                dcc.Dropdown(id="dropdown3",
                                             options=[{"label": x['chunk'], "value": x['chunk']} for x in config.city_count],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Top City Count",
                                             style={'background-color': '#f9f9f9',
                                                    'color': '#189AB4',
                                                    'min-width': '140px',
                                                    'font-size': '14px',
                                                    'font-family': 'sans-serif',
                                                    'cursor': 'pointer',
                                                    'padding': '5px'}
                                             ),
                                dcc.Dropdown(id="dropdown4",
                                             options=[{"label": x['VendorName'], "value": x['VendorID']} for x in config.Vendors_dataset],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Select Cab Vendor",
                                             style={'background-color': '#f9f9f9',
                                                    'color': '#189AB4',
                                                    'min-width': '180px',
                                                    'font-size': '14px',
                                                    'font-family': 'sans-serif',
                                                    'cursor': 'pointer',
                                                    'padding': '5px'}
                                             ),
                               dcc.Dropdown(id="dropdown1",
                                             options=[{"label": x['year'], "value": x['year']} for x in config.query_year],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Select Year",
                                            style={'background-color': '#f9f9f9',
                                                   'color': '#189AB4',
                                                   'min-width': '140px',
                                                   'font-size': '14px',
                                                   'font-family': 'sans-serif',
                                                   'cursor': 'pointer',
                                                   'padding': '5px'}
                                            )],
                                            style={'display': 'flex',
                                                   'min-width': '600px',
                                                   })

    return input_controls

