import pandas as pd
from sodapy import Socrata
import config

try:
    data_list = list()
    client = Socrata("data.cityofnewyork.us", None)
    for year in config.query_year.values():
        results = client.get(year, limit=config.chunk_set)
        data_list.append(results)
        # results_df = pd.DataFrame.from_records(results)
    print(data_list)
except Exception as msf:
    print(str(msf))