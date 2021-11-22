import pandas as pd
from data_access_layer.url_source_data import get_url_query_data, get_location_master_data, get_paytype_master_data, get_vendor_master_data
import config


def get_taxi_data(year, chunk_count, city_count, selected_vendor):
    try:
        raw_data = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                       columns='tpep_pickup_datetime,pulocationid,payment_type,total_amount',
                                       condition_set='total_amount>10&vendorid='+str(selected_vendor), limit=[x['keyval'] for x in config.chunk_set if x['chunk'] == chunk_count][0])

        ##Type Casting
        raw_data['pulocationid']=raw_data['pulocationid'].astype(int)
        raw_data['total_amount'] = raw_data['total_amount'].astype(float)
        raw_data['payment_type'] = raw_data['payment_type'].astype(int)

        ## Get Payment Type Data
        payment_masterdata = get_paytype_master_data()
        payment_masterdata = payment_masterdata.convert_dtypes()
        payment_masterdata['payment_type'] = payment_masterdata['payment_type'].astype(int)

        ## Get Location Data
        location_masterdata = get_location_master_data()
        location_masterdata = location_masterdata.convert_dtypes()
        location_masterdata['SourceLocation'] = location_masterdata['Zone'].map(str) + '(' + location_masterdata['Borough'].map(str) + ')'

        ## Rename Column
        raw_data.rename(columns={'pulocationid': 'LocationID'}, inplace=True)

        ## Merge Data
        merged_location_df = raw_data.merge(location_masterdata, how='left', on='LocationID')
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


def get_year_revenue_data(year=2020):
    try:
        raw_data = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                       columns='vendorid,tpep_pickup_datetime',
                                       condition_set='''tpep_pickup_datetime between '2020-01-01' and '2020-01-31T09:27:32.000'&vendorid=1 or vendorid=2''', limit=100)

        ##Type Casting
        raw_data['vendorid'] = raw_data['vendorid'].astype(int)
        raw_data['tpep_pickup_datetime'] = pd.to_datetime(raw_data['tpep_pickup_datetime'])
        raw_data['tpep_pickup_datetime'] = raw_data['tpep_pickup_datetime'].dt.date

        ## Get Vendor Master Data
        vendor_masterdata = get_vendor_master_data()
        vendor_masterdata['vendorid'] = vendor_masterdata['vendorid'].astype(int)
        vendor_masterdata = vendor_masterdata.convert_dtypes()

        ## Merge Data
        merged_location_df = raw_data.merge(vendor_masterdata, how='left', on='vendorid')

        # Group by source location and payment type
        result_df = merged_location_df.groupby(['vendorname'], as_index=False).agg({'tpep_pickup_datetime': 'sum'})
        # TODO PENDING
        print(result_df)



    except Exception as msf:
        print(str(msf))


def get_vendor_revenue_data(year, chunk_count):
    try:
        raw_data = get_url_query_data(base_url=config.base_url,
                                  year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                  columns='vendorid,total_amount,tip_amount',
                                  condition_set='total_amount>10', limit=[x['keyval'] for x in config.chunk_set if x['chunk'] == chunk_count][0])

        # type_casting
        raw_data[['tip_amount', 'total_amount']] = raw_data[['tip_amount', 'total_amount']].astype(float)
        raw_data['vendorid'] = raw_data['vendorid'].astype(int)

        # Get vendor data
        vendor_masterdata = get_vendor_master_data()
        vendor_masterdata = vendor_masterdata.convert_dtypes()
        vendor_masterdata.info()
        ## Merge Data
        merged_vendor_df = raw_data.merge(vendor_masterdata, how='left', on='vendorid')
        merged_vendor_df.convert_dtypes()
        merged_vendor_df['vendorname'] = merged_vendor_df['vendorname'].astype(str)

        ## Groupby vendorid
        new_vendor_df = merged_vendor_df.groupby(['vendorname'], as_index=False).aggregate({'total_amount': 'sum', 'tip_amount': 'sum'})

        return new_vendor_df

    except Exception as msf:
        print(str(msf))











