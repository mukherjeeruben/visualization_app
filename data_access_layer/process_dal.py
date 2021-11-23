import pandas as pd
import calendar
from data_access_layer.url_source_data import get_url_query_data, get_location_master_data, get_paytype_master_data, get_vendor_master_data
import config
import numpy as np
from time_log import code_init, execution_end


def get_taxi_data(year, chunk_count, city_count, selected_vendor):
    code_init()
    try:
        raw_data = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                       columns='tpep_pickup_datetime,pulocationid,payment_type,total_amount',
                                       condition_set='total_amount>10&vendorid='+str(selected_vendor),
                                       limit=[x['keyval'] for x in config.chunk_set if x['chunk'] == chunk_count][0])

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
        result_df.rename(columns={'payment_type': 'Total Rides'}, inplace=True)
        result_df.rename(columns={'SourceLocation': 'Pickup Location'}, inplace=True)
        result_df.rename(columns={'PaymentTypeName': 'Payment Type'}, inplace=True)

        execution_end()
        return result_df

    except Exception as msf:
        print(str(msf))


def get_year_revenue_data(month, year):
    code_init()
    try:
        date_range = None
        for range_val in config.date_rangeset:
            if month == range_val['month']:
                date_range = '\''+str(year)+range_val['startdate']+'\''+' and '+'\''+str(year)+range_val['enddate']+'\''
        raw_data = get_url_query_data(base_url=config.base_url,
                                       year_key=[x['keyval'] for x in config.query_year if x['year'] == year][0],
                                       columns='vendorid,tpep_pickup_datetime',
                                       condition_set='tpep_pickup_datetime between '+ date_range,
                                       limit=config.line_graph_chunk)


        ##Type Casting and Cleanng
        raw_data['vendorid'] = pd.to_numeric(raw_data['vendorid'], errors='coerce').fillna(0).astype(np.int64)
        date_set = raw_data['tpep_pickup_datetime'].str.split('T', expand=True)
        raw_data = pd.merge(raw_data, date_set, left_index=True, right_index=True)
        # raw_data = raw_data.drop(['tpep_pickup_datetime'], axis=1)
        raw_data.rename(columns={0: 'Date'}, inplace=True)
        raw_data['Date'] = pd.to_datetime(raw_data['Date'], format='%Y-%m-%d')
        raw_data['Day'] = pd.DatetimeIndex(raw_data['Date']).day
        raw_data[1] = raw_data['Date'].dt.day_name(locale='English')
        raw_data.rename(columns={1: 'Dayname'}, inplace=True)

        ## Get Vendor Master Data
        vendor_masterdata = get_vendor_master_data()
        vendor_masterdata = vendor_masterdata.convert_dtypes()


        ## Merge Data
        merged_location_df = raw_data.merge(vendor_masterdata, how='left', on='vendorid')


        # Group by vendor name and date
        result_df = merged_location_df.groupby(['vendorname', 'Day', 'Dayname'], as_index=False).agg({'vendorid': 'sum'})

        ##Format Columns and data
        result_df['tpep_pickup_datetime'] = result_df['Dayname'].map(str) + '(' + result_df['Day'].map(str) + ')'
        result_df.rename(columns={'tpep_pickup_datetime': 'WeekDay'}, inplace=True)
        result_df.rename(columns={'vendorid': 'Ride Count'}, inplace=True)
        result_df.rename(columns={'vendorname': 'Vendor Company'}, inplace=True)
        result_df = result_df.convert_dtypes()
        enddate_list = result_df.loc[result_df['Day'] == result_df['Day'].max()].values.tolist()

        execution_end()
        return result_df, enddate_list

    except Exception as msf:
        print(str(msf))


def get_vendor_revenue_data(year, chunk_count):
    try:
        code_init()
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

        ## Merge Data
        merged_vendor_df = raw_data.merge(vendor_masterdata, how='left', on='vendorid')
        merged_vendor_df.convert_dtypes()
        merged_vendor_df['vendorname'] = merged_vendor_df['vendorname'].astype(str)
        merged_vendor_df = merged_vendor_df[merged_vendor_df['vendorname'] != '<NA>']

        ## Groupby vendorid
        new_vendor_df = merged_vendor_df.groupby(['vendorname'], as_index=False).aggregate({'total_amount': 'sum', 'tip_amount': 'sum'})

        execution_end()
        return new_vendor_df

    except Exception as msf:
        print(str(msf))











