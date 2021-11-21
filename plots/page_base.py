from dash import html, dcc
from plots.control_set import set_control


def set_page_base():
    page_base = html.Div(children=[
        html.H1(children='CA682 Data Management and Visualization Assignment'),
        html.Div(children='''New York - Yellow Taxi Trip Data Analysis''')
    ])

    ### Add Controls to page base
    page_base.children.append(set_control())

    ### Create Graph objects
    page_base.children.append(html.Div(dcc.Graph(id='bar_graph_1')))

    return page_base



