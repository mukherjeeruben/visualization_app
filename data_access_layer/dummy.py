import pandas as pd
from data_access_layer.url_source_data import get_url_query_data, get_location_master_data, get_paytype_master_data, get_vendor_master_data
import config
import plotly.express as px
x_df=get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == 2020][0],
                                       columns='vendorid,total_amount,tip_amount',
                                       condition_set='total_amount>10', limit=1000)


# type_casting
x_df[['tip_amount','total_amount']] = x_df[['tip_amount','total_amount']].astype(float)
x_df['vendorid'] = x_df['vendorid'].astype(int)

# Get vendor data
vendor_masterdata = get_vendor_master_data()
vendor_masterdata = vendor_masterdata.convert_dtypes()
vendor_masterdata.info()
## Merge Data
merged_vendor_df = x_df.merge(vendor_masterdata, how='left', on='vendorid')
merged_vendor_df.convert_dtypes()
merged_vendor_df['VendorName']=merged_vendor_df['VendorName'].astype(str)


## Groupby vendorid
new_vendor_df = merged_vendor_df.groupby(['VendorName'], as_index=False).aggregate({'total_amount':'sum', 'tip_amount':'sum'})

## Plotting the Graph
fig = px.scatter(new_vendor_df, x="total_amount", y="VendorName",
                 size="tip_amount", color="VendorName",hover_name="tip_amount", log_x=True, size_max=60)
fig.show()

print('Hi')
