import pandas as pd
from sodapy import Socrata
import config

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
except Exception as msf:
    print(str(msf))

    # results_df1 = pd.DataFrame.from_records(year_records)