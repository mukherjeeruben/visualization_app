import dash
from plots.page_base import set_page_base
from dash.dependencies import Input, Output
import config
from plots.graph_set import fig_graph_a, fig_graph_b, fig_graph_c

dash_app = dash.Dash(__name__)
server = dash_app.server
dash_app.layout = set_page_base()


@dash_app.callback(Output('graph_a', component_property='figure'), Input('dropdown1', 'value'), Input('dropdown2', 'value'), Input('dropdown3', 'value'), Input('dropdown4', 'value'))
def render_graph_a(selected_year, selected_month, selected_city_count, selected_vendor):
    fig = fig_graph_a(selected_year, selected_month, selected_city_count, selected_vendor)
    return fig


@dash_app.callback(Output('graph_b', component_property='figure'), Input('dropdown12', 'value'), Input('dropdown13', 'value'))
def render_graph_b(selected_month, selected_year):
    fig = fig_graph_b(selected_month, selected_year)
    return fig


@dash_app.callback(Output('graph_c', component_property='figure'), Input('dropdown20', 'value'),Input('dropdown21', 'value'))
def render_graph_b(selected_year, selected_month):
    fig = fig_graph_c(selected_year, selected_month)
    return fig


dash_app.title = 'Visualization App'

if __name__ == '__main__':
    dash_app.run_server(debug=config.debug)
