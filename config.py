debug = True  # Push False on Server
base_url='''https://data.cityofnewyork.us'''
location_master_data = '''https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'''

query_year = [{'year': 2017, 'keyval': 'biws-g3hs'},
              {'year': 2018, 'keyval': 't29m-gskq'},
              {'year': 2019, 'keyval': '2upf-qytp'},
              {'year': 2020, 'keyval': 'kxp8-n2sj'}]


chunk_set =[{'chunk': 'Less than 1000', 'keyval': 10000},
            {'chunk': 'Less than 100000', 'keyval': 100000},
            {'chunk': 'Less than 1000000', 'keyval': 1000000},
            {'chunk': 'Less than 2500000', 'keyval': 2500000},
            {'chunk': 'Less than 5000000', 'keyval': 5000000},
            {'chunk': 'Maximum', 'keyval': 6525000}]

payment_mode = '''[{"payment_type" : 1, "PaymentTypeName": "Credit card"},
                {"payment_type" : 2, "PaymentTypeName": "Cash"},
                {"payment_type" : 3, "PaymentTypeName": "No charge"},
                {"payment_type" : 4, "PaymentTypeName": "Dispute"},
                {"payment_type" : 5, "PaymentTypeName": "Unknown"},
                {"payment_type" : 6, "PaymentTypeName": "Voided trip"}] '''

