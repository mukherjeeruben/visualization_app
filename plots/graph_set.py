import plotly.express as px
from data_access_layer.process_dal import get_taxi_data, get_year_revenue_data, get_vendor_revenue_data


def fig_graph_a(year, chunk_count, selected_city_count, selected_vendor):
    if year is None:
        fig = px.bar()
    else:
        df = get_taxi_data(year, chunk_count, selected_city_count, selected_vendor)
        fig = px.bar(df, x="Payment Type Count",
                         y="Pickup Location",
                         color="Payment Type",
                         text="Payment Type Count",
                         orientation='h',
                         barmode='stack')
        fig.update_layout(
            title='Payment Type in yellow taxi',
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                domain=[0, 1],
            ),
            xaxis=dict(
                zeroline=False,
                showline=False,
                showticklabels=True,
                showgrid=True,
                domain=[0, 0.42],
            ),
            legend=dict(x=1.038, y=1.038, font_size=10),
            margin=dict(l=100, r=20, t=70, b=70),
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)',
        )
    return fig


def fig_graph_b(year, chunk_count, selected_city_count, selected_vendor):
    if year is None:
        fig = px.line()
    else:
        df = get_year_revenue_data(year)
        df = px.data.gapminder().query("continent=='Oceania'")
        # print(df.info())
        # print(df)
        fig = px.line(df, x="year", y="lifeExp", color='country')
    return fig


def fig_graph_c(year, chunk_count):
    if year is None:
        fig = px.scatter()
    else:
        df = get_vendor_revenue_data(year, chunk_count)
        fig = px.scatter(df, x="total_amount", y="vendorname",
                         size="tip_amount", color="vendorname", hover_name="tip_amount", log_x=True, size_max=60)
    return fig



