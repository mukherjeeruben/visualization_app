from dash import html, dcc
from plots.graph_set import line_fig, world_map_fig
from plots.control_set import set_control


def set_page_base():
    page_base = html.Div(children=[
        html.H1(children='Data Visualization 1'),
        html.Div(children='''Data Renderer''')
    ])

    ### Add Controls to page base
    page_base.children.append(set_control())

    ### Create Graph objects
    page_base.children.append(html.Div(dcc.Graph(id='1', figure=line_fig())))
    page_base.children.append(html.Div(dcc.Graph(id='2', figure=world_map_fig())))

    return page_base
