import pandas as pd
import requests
import config


def get_location_master_data():
    data = pd.read_csv(config.location_master_data)
    data = data.drop(columns=["Zone", "service_zone"])
    return data


def get_url_query_data(base_url, year_key, columns, condition_set, limit):
    api_url = base_url + '/resource/'+year_key+'.json?&$select='+columns+'&$where='+condition_set+'&$limit='+str(limit)
    url_raw_data = requests.get(api_url).json()
    df = pd.DataFrame.from_records(url_raw_data)
    return df


data_2020 = get_url_query_data(base_url=config.base_url, year_key=[x['keyval'] for x in config.query_year if x['year']==2019][0], columns='tpep_pickup_datetime,pulocationid,payment_type,total_amount', condition_set='total_amount>10&vendorid=1',limit=config.chunk_set)
print(data_2020)







