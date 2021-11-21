import dash
from plots.page_base import set_page_base
from dash.dependencies import Input, Output
import config
from plots.graph_set import bar_fig

dash_app = dash.Dash(__name__)
server = dash_app.server
dash_app.layout = set_page_base()


@dash_app.callback(Output('bar_graph_1', component_property='figure'), Input('dropdown1', 'value'), Input('dropdown2', 'value'), Input('dropdown3', 'value'), Input('dropdown4', 'value'))
def render_graph(selected_year, selected_count, selected_city_count, selected_vendor):
    fig = bar_fig(selected_year, selected_count, selected_city_count, selected_vendor)
    return fig


dash_app.title = 'Visualization App'

if __name__ == '__main__':
    dash_app.run_server(debug=config.debug)
