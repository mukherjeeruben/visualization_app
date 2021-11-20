import pandas as pd
from sodapy import Socrata
import config

def get_location_master_data():
    data = pd.read_csv(config.location_master_data)
    data = data.drop(columns = ['Zone','service_zone'])
    return data

def get_taxi_data():
    try:
        results_df = pd.DataFrame()
        result_list = list()
        client = Socrata("data.cityofnewyork.us", None)
        for year in config.query_year.values():
            results = client.get(year, limit=config.chunk_set)
            result_list.append(results)

        for year_records in result_list:
            for rows in year_records:
                results_df = results_df.append(rows, ignore_index=True)
        print(results_df)
        new_res_df = results_df.drop(columns = ['vendorid','tpep_dropoff_datetime',
           'passenger_count', 'trip_distance', 'ratecodeid', 'store_and_fwd_flag',
            'dolocationid', 'fare_amount', 'extra',
           'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
            'congestion_surcharge'])

        print(new_res_df)
        new_res_df['pulocationid']=new_res_df['pulocationid'].astype(int)

        print(new_res_df.info())
        new_res_df.isna()
        new_res_df.dropna()

        x_df = get_location_master_data()
        x_df['LocationID']=x_df['LocationID'].astype(int)
        x_df['Borough']=x_df['Borough'].astype(str)
        new_res_df.rename(columns={'pulocationid':'LocationID'},inplace = True)
        print(x_df)
        print(x_df.info())
        print(new_res_df)
        merged_df = new_res_df.merge(x_df,how='left',on='LocationID')
        print(merged_df.info())
        x=merged_df.groupby('Borough').count()
        print(x)
        return(x)
        #print(new_res_df)
    except Exception as msf:
        print(str(msf))

        # results_df1 = pd.DataFrame.from_records(year_records)