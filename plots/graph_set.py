import plotly.express as px
from data_access_layer.process_dal import get_taxi_data


def bar_fig(year, chunk_count):
    if year is None:
        fig = px.bar()
    else:
        df = get_taxi_data(year, chunk_count)
        fig = px.bar(df, x="PickupLocation", y="RideCount", color="PickupLocation", text="RideCount")
    return fig
