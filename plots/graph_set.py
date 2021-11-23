import plotly.express as px
from data_access_layer.process_dal import get_payment_type_data, get_year_revenue_data, get_vendor_revenue_data
import config


def fig_graph_a(year, month, selected_city_count, selected_vendor):
    if year is None:
        fig = px.bar()
    else:
        df = get_payment_type_data(year, month, selected_city_count, selected_vendor)
        fig = px.bar(df, x="Total Rides",
                         y="Pickup Location",
                         color="Payment Mode Type",
                         text="Total Rides",
                         orientation='h',
                         barmode='stack',
                         height=int(20*int(selected_city_count)+200))
        fig.update_layout(
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                domain=[0, 1],
                titlefont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                )
            ),
            xaxis=dict(
                zeroline=False,
                showline=False,
                showticklabels=True,
                showgrid=False,
                titlefont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                )
            ),
            legend=dict(x=1.038, y=1.038, font_size=12),
            margin=dict(l=100, r=20, t=60, b=70),
            paper_bgcolor='white',
            plot_bgcolor='white',
        )
        annotations = []
        # Title
        annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                xanchor='left', yanchor='bottom',
                                text='Payment mode count of cab vendor : '+str([x['VendorName'] for x in config.Vendors_dataset][0]) +' ('+str(month)+', '+str(year)+')',
                                font=dict(family='Arial',
                                          size=24,
                                          color='rgb(82, 82, 82)'),
                                showarrow=False))

        # Source
        annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                                xanchor='center', yanchor='top',
                                text='Source: NYC Taxi & Limousine Commission ' +
                                     'Storytelling with data',
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))

        fig.update_layout(annotations=annotations)
    return fig


def fig_graph_b(month, year):
    if year is None:
        fig = px.line()
    else:
        df, enddate_list = get_year_revenue_data(month, year)
        fig = px.line(df, x="WeekDay", y="Ride Count", color='Vendor Company', markers=True, symbol="Vendor Company")

        fig.update_layout(
            xaxis=dict(
                title=None,
                showline=True,
                showgrid=False,
                showticklabels=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=2,
                tickmode='linear',
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                showticklabels=True,
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
                titlefont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                )
            ),
            autosize=False,
            margin=dict(
                autoexpand=False,
                l=50,
                r=120,
                t=110
            ),
            showlegend=False,
            plot_bgcolor='white'
        )

        annotations = []
        colors = ['rgb(67,67,67)', 'rgb(115,115,115)']
        lable_list = list()
        y_cords = list()
        for row in enddate_list:
            lable_list.append(row[0])
            y_cords.append(row[3])

        # Adding labels

        for y_ts, label, color in zip(y_cords, lable_list, colors):
            # labeling the left_side of the plot
            annotations.append(dict(xref='paper',
                                    x=0.95,
                                    y=y_ts,
                                    xanchor='left',
                                    yanchor='middle',
                                    text=label,
                                    font=dict(family='Arial',
                                              size=12),
                                    showarrow=False))

        # Title
        annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                xanchor='left', yanchor='bottom',
                                text='New York : Yellow Taxi ride data per day for ' +'('+str(month)+', '+str(year)+')',
                                font=dict(family='Arial',
                                          size=24,
                                          color='rgb(82, 82, 82)'),
                                showarrow=False))

        # Source
        annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.230,
                                xanchor='center', yanchor='top',
                                text='Source: NYC Taxi & Limousine Commission ' +
                                     'Storytelling with data',
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))

        fig.update_layout(annotations=annotations)

    return fig


def fig_graph_c(year, chunk_count):
    if year is None:
        fig = px.scatter()
    else:
        df = get_vendor_revenue_data(year, chunk_count)
        fig = px.scatter(df, x="total_amount", y="vendorname",
                         size="tip_amount", color="vendorname", hover_name="tip_amount", log_x=True, size_max=60)

    return fig



