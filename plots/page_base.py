from dash import html, dcc
from plots.control_set import set_control_a, set_control_b, set_control_c


def set_page_base():
    page_base = html.Div(children=[
        html.H1(children='CA682 Data Management and Visualization Assignment',
                style={'color': '#189AB4',
                       'font-size': '30px',
                       'font-family': 'sans-serif',
                       'padding': '10px'}
                ),
        html.Div(children='New York - Yellow Taxi Trip Data Analysis',
                 style={'color': '#F2E34C',
                        'font-size': '20px',
                        'font-family': 'sans-serif',
                        'padding': '10px'}
                 )
                ])

    ### Add Controls to page base and Create Graph objects for A
    page_base.children.append(set_control_a())
    page_base.children.append(html.Div(dcc.Graph(id='graph_a')))

    ### Add Controls to page base and Create Graph objects for B
    page_base.children.append(set_control_b())
    page_base.children.append(html.Div(dcc.Graph(id='graph_b')))

    ### Add Controls to page base and Create Graph objects for C
    page_base.children.append(set_control_c())
    page_base.children.append(html.Div(dcc.Graph(id='graph_c')))

    return page_base



