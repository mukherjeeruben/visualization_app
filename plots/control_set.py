import dash_core_components as dcc
import dash_html_components as html
import config


def set_control_a():
    input_controls = html.Div(children=[dcc.Dropdown(id="dropdown4",
                                                     options=[{"label": x['VendorName'], "value": x['VendorID']} for x in config.Vendors_dataset],
                                                     value=None,
                                                     clearable=False,
                                                     searchable=False,
                                                     placeholder="Select Cab Vendor",
                                                     style={'background-color': '#f9f9f9',
                                                            'color': '#189AB4',
                                                            'min-width': '200px',
                                                            'font-size': '12px',
                                                            'font-family': 'Arial',
                                                            'cursor': 'pointer'
                                                            }
                                                     ),
                                dcc.Dropdown(id="dropdown3",
                                             options=[{"label": x['chunk'], "value": x['chunk']} for x in config.city_count],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Top City Count",
                                             style={'background-color': '#f9f9f9',
                                                    'color': '#189AB4',
                                                    'min-width': '120px',
                                                    'font-size': '12px',
                                                    'font-family': 'Arial',
                                                    'cursor': 'pointer'
                                                    }
                                             ),
                    dcc.Dropdown(id="dropdown2",
                                 options=[{"label": x['month'], "value": x['month']} for x in config.date_rangeset],
                                 value=None,
                                 clearable=False,
                                 searchable=False,
                                 placeholder="Select Month",
                                 style={'background-color': '#f9f9f9',
                                        'color': '#189AB4',
                                        'min-width': '110px',
                                        'font-size': '12px',
                                        'font-family': 'Arial',
                                        'cursor': 'pointer'
                                        }
                                 ),

                               dcc.Dropdown(id="dropdown1",
                                             options=[{"label": x['year'], "value": x['year']} for x in config.query_year],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Select Year",
                                            style={'background-color': '#f9f9f9',
                                                   'color': '#189AB4',
                                                   'min-width': '100px',
                                                   'font-size': '12px',
                                                   'font-family': 'Arial',
                                                   'cursor': 'pointer',
                                                  }
                                            )],
                                            style={'display': 'flex',
                                                   'justify-content': 'space-evenly',
                                                   'max-width':'680px'
                                                   })

    return input_controls


def set_control_b():
    input_controls = html.Div(children=[
                                dcc.Dropdown(id="dropdown12",
                                             options=[{"label": x['month'], "value": x['month']} for x in config.date_rangeset],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Select Month",
                                             style={'background-color': '#f9f9f9',
                                                    'color': '#189AB4',
                                                    'min-width': '110px',
                                                    'font-size': '12px',
                                                    'font-family': 'Arial',
                                                    'cursor': 'pointer'}
                                             ),
                               dcc.Dropdown(id="dropdown13",
                                             options=[{"label": x['year'], "value": x['year']} for x in config.query_year],
                                             value=None,
                                             clearable=False,
                                             searchable=False,
                                             placeholder="Select Year",
                                            style={'background-color': '#f9f9f9',
                                                   'color': '#189AB4',
                                                   'min-width': '100px',
                                                   'font-size': '12px',
                                                   'font-family': 'Arial',
                                                   'cursor': 'pointer'}
                                            )],
                                            style={'display': 'flex',
                                                   'justify-content': 'space-evenly',
                                                   'max-width': '300px'
                                                   })

    return input_controls


def set_control_c():
    input_controls = html.Div(children=[dcc.Dropdown(id="dropdown21",
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
                                        dcc.Dropdown(id="dropdown20",
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

