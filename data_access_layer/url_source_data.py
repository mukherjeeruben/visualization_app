import pandas as pd
import requests
import config


def get_paytype_master_data():
    data = pd.read_json(config.payment_mode)
    return data


def get_location_master_data():
    data = pd.read_csv(config.location_master_data)
    # data = data.drop(columns=["Zone", "service_zone"])
    data = data.drop(columns=["service_zone"])
    return data


def get_url_query_data(base_url, year_key, columns, condition_set, limit):
    api_url = base_url + '/resource/'+year_key+'.json?&$select='+columns+'&$where='+condition_set+'&$limit='+str(limit)
    url_raw_data = requests.get(api_url).json()
    df = pd.DataFrame.from_records(url_raw_data)
    return df












