import plotly.express as px
from data_access_layer.process_dal import get_taxi_data


def bar_fig(year, chunk_count, selected_city_count, selected_vendor):
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



