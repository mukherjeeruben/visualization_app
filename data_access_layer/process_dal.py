import pandas as pd
from data_access_layer.url_source_data import get_url_query_data, get_location_master_data, get_paytype_master_data
import config


def get_taxi_data():
    try:
        data_2020 = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == 2020][0],
                                       columns='tpep_pickup_datetime,pulocationid,payment_type,total_amount',
                                       condition_set='total_amount>10&vendorid=1', limit=100)

        ##Type Casting
        data_2020['pulocationid']=data_2020['pulocationid'].astype(int)
        data_2020['total_amount'] = data_2020['total_amount'].astype(float)

        ## Get Location Data
        location_masterdata = get_location_master_data()
        location_masterdata = location_masterdata.convert_dtypes()

        ## Rename Column
        data_2020.rename(columns={'pulocationid': 'LocationID'}, inplace=True)
        location_masterdata.rename(columns={'Borough': 'PickupLocation'}, inplace=True)

        ## Merge Data
        merged_df = data_2020.merge(location_masterdata, how='left', on='LocationID')

        ##Clean Data for null values
        merged_df.isna()
        merged_df.dropna()

        #Group by source location
        result_df = merged_df.groupby('PickupLocation')
        return result_df
    except Exception as msf:
        print(str(msf))





