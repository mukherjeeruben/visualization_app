import plotly.express as px
from data_access_layer.process_dal import get_payment_type_data, get_year_revenue_data, get_vendor_revenue_data
import config


def fig_graph_a(year, month, selected_city_count, selected_vendor):
    if year is None:
        return empty_plot('Select Taxi Vendor, Top Locations, Month and Year for number of payment modes per vendor in a month')
    else:
        df = get_payment_type_data(year, month, selected_city_count, selected_vendor)
        fig = px.bar(df, x="Total Rides",
                         y="Pickup Location",
                         color="Payment Mode Type",
                         text="Total Rides",
                         orientation='h',
                         barmode='stack',
                         height=int(20*int(selected_city_count)+200))
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
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
                                text='Payment mode count of taxi vendor : '+str([x['VendorName'] for x in config.Vendors_dataset if x['VendorID'] == selected_vendor][0]) +' ('+str(month)+', '+str(year)+')',
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
        return empty_plot('Select Month and Year for number day rides per vendor of a month')
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
                                text='Ride data for taxi vendors per day for ' +'('+str(month)+', '+str(year)+')',
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


def fig_graph_c(year, month):
    if year is None:
        return empty_plot(message='Select Month and Year for fare division of Taxi Vendors')
    else:
        df = get_vendor_revenue_data(year, month)
        fig = px.bar(df,
                     y="Vendor Name",
                     x=['Base Fare', 'Extra Charge', 'MTA Tax', 'Tip', 'Improvement Surcharge'],
                     barmode='stack',
                     # text='Total Revenue',
                     height=300)

        # fig.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
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
                title='Fare Division',
                tickprefix="$",
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

        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=''
        ))
        annotations = []
        # Title
        annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                xanchor='left', yanchor='bottom',
                                text='Fare Division of Taxi Vendors for' + ' (' + str(month) + ', ' + str(year) + ')',
                                font=dict(family='Arial',
                                          size=24,
                                          color='rgb(82, 82, 82)'),
                                showarrow=False))

        # Source
        annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.23,
                                xanchor='center', yanchor='top',
                                text='Source: NYC Taxi & Limousine Commission Storytelling with data',
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))

        fig.update_layout(annotations=annotations)

    return fig


def empty_plot(message):
    template = {
            "layout": {
                "xaxis": {
                    "visible": False
                },
                "yaxis": {
                    "visible": False
                },
                "annotations": [
                    {
                        "text": message,
                        "xref": "paper",
                        "yref": "paper",
                        "showarrow": False,
                        "font": {
                            "size": 18
                        }
                    }
                ]
            }
        }

    return template