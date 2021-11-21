from dash import html, dcc
from plots.control_set import set_control


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

    ### Add Controls to page base
    page_base.children.append(set_control())

    ### Create Graph objects
    page_base.children.append(html.Div(dcc.Graph(id='bar_graph_1')))

    return page_base



