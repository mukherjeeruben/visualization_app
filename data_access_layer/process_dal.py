import pandas as pd
from data_access_layer.url_source_data import get_url_query_data, get_location_master_data, get_paytype_master_data
import config


def get_taxi_data(year, chunk_count, city_count, selected_vendor):
    try:
        data_2020 = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                       columns='tpep_pickup_datetime,pulocationid,payment_type,total_amount',
                                       condition_set='total_amount>10&vendorid='+str(selected_vendor), limit=[x['keyval'] for x in config.chunk_set if x['chunk'] == chunk_count][0])

        ##Type Casting
        data_2020['pulocationid']=data_2020['pulocationid'].astype(int)
        data_2020['total_amount'] = data_2020['total_amount'].astype(float)
        data_2020['payment_type'] = data_2020['payment_type'].astype(int)

        ## Get Payment Type Data
        payment_masterdata = get_paytype_master_data()
        payment_masterdata = payment_masterdata.convert_dtypes()
        payment_masterdata['payment_type'] = payment_masterdata['payment_type'].astype(int)

        ## Get Location Data
        location_masterdata = get_location_master_data()
        location_masterdata = location_masterdata.convert_dtypes()
        location_masterdata['SourceLocation'] = location_masterdata['Zone'].map(str) + '(' + location_masterdata['Borough'].map(str) + ')'

        ## Rename Column
        data_2020.rename(columns={'pulocationid': 'LocationID'}, inplace=True)

        ## Merge Data
        merged_location_df = data_2020.merge(location_masterdata, how='left', on='LocationID')
        merged_df = merged_location_df.merge(payment_masterdata, how='left', on='payment_type')

        ##Clean Data for null values
        merged_df.isna()
        merged_df.dropna()

        ## Get top count records

        set_count = [x['keyval'] for x in config.city_count if x['chunk'] == city_count][0]
        if set_count != 'All':
            type_merged_df = merged_df.convert_dtypes()
            top_location_df = type_merged_df.groupby('SourceLocation', as_index=False).size().nlargest(set_count,'size')
            top_location_df = top_location_df.convert_dtypes()
            toplocation_list = [str(location) for location in top_location_df['SourceLocation']]

        #Group by source location and payment type
        result_df = merged_df.groupby(['SourceLocation', 'PaymentTypeName'], as_index=False).agg({'payment_type': 'sum'})
        result_df = result_df.convert_dtypes()

        ##Clean Data
        result_df = result_df[result_df['SourceLocation'] != '<NA>(Unknown)']
        if set_count != 'All':
            result_df = result_df[result_df['SourceLocation'].isin(toplocation_list)]

        ## Rename Column
        result_df.rename(columns={'payment_type': 'Payment Type Count'}, inplace=True)
        result_df.rename(columns={'SourceLocation': 'Pickup Location'}, inplace=True)
        result_df.rename(columns={'PaymentTypeName': 'Payment Type'}, inplace=True)

        return result_df

    except Exception as msf:
        print(str(msf))









