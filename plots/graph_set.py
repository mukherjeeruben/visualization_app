import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from urllib.request import urlopen
import json
from data_access_layer.process_dal import get_taxi_data

def line_fig():
    # df = pd.DataFrame({
    #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    #     "Amount": [4, 1, 2, 2, 4, 5],
    #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    # })
    df = get_taxi_data()
    fig = px.bar(df, x="LocationID", y="LocationID", color="LocationID")
    return fig


def world_map_fig():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                     dtype={"fips": str})
    fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                        colorscale="Viridis", zmin=0, zmax=12,
                                        marker_opacity=0.5, marker_line_width=0))
    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=3, mapbox_center={"lat": 37.0902, "lon": -95.7129})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig