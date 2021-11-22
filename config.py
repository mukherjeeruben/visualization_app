debug = True  # Push False on Server
base_url='''https://data.cityofnewyork.us'''
location_master_data = '''https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'''

line_graph_chunk = 10000000

query_year = [{'year': 2017, 'keyval': 'biws-g3hs'},
              {'year': 2018, 'keyval': 't29m-gskq'},
              {'year': 2019, 'keyval': '2upf-qytp'},
              {'year': 2020, 'keyval': 'kxp8-n2sj'}]


chunk_set =[{'chunk': 'Less than 1000', 'keyval': 10000},
            {'chunk': 'Less than 100000', 'keyval': 100000},
            {'chunk': 'Less than 1000000', 'keyval': 1000000},
            {'chunk': 'Less than 1500000', 'keyval': 1500000},
            {'chunk': 'Less than 2000000', 'keyval': 2000000},
            {'chunk': 'Less than 2500000', 'keyval': 2500000},
            {'chunk': 'Less than 5000000', 'keyval': 5000000},
            {'chunk': 'Maximum', 'keyval': 6525000}]

payment_mode = '''[{"payment_type" : 1, "PaymentTypeName": "Credit card"},
                {"payment_type" : 2, "PaymentTypeName": "Cash"},
                {"payment_type" : 3, "PaymentTypeName": "No charge"},
                {"payment_type" : 4, "PaymentTypeName": "Dispute"},
                {"payment_type" : 5, "PaymentTypeName": "Unknown"},
                {"payment_type" : 6, "PaymentTypeName": "Voided trip"}] '''


city_count = [{'chunk': '10', 'keyval': 10},
            {'chunk': '25', 'keyval': 25},
            {'chunk': '50', 'keyval': 50},
            {'chunk': 'All', 'keyval': 'All'}]


Vendors_dataset = [{"VendorID": 1, "VendorName": "Creative Mobile Technologies"},
                    {"VendorID": 2, "VendorName": "VeriFone Inc"}]

date_rangeset = [{'month': 'January', 'startdate': '-01-01T00:00:00', 'enddate': '-01-31T23:59:00'},
                 {'month': 'February', 'startdate': '-02-01T00:00:00', 'enddate': '-02-28T23:59:00'},
                 {'month': 'March', 'startdate': '-03-01T00:00:00', 'enddate': '-03-31T23:59:00'},
                 {'month': 'April', 'startdate': '-04-01T00:00:00', 'enddate': '-04-30T23:59:00'},
                 {'month': 'May', 'startdate': '-05-01T00:00:00', 'enddate': '-05-31T23:59:00'},
                 {'month': 'June', 'startdate': '-06-01T00:00:00', 'enddate': '-06-30T23:59:00'},
                 {'month': 'July', 'startdate': '-07-01T00:00:00', 'enddate': '-07-31T23:59:00'},
                 {'month': 'August', 'startdate': '-08-01T00:00:00', 'enddate': '-08-31T23:59:00'},
                 {'month': 'September', 'startdate': '-09-01T00:00:00', 'enddate': '-09-30T23:59:00'},
                 {'month': 'October', 'startdate': '-10-01T00:00:00', 'enddate': '-10-31T23:59:00'},
                 {'month': 'November', 'startdate': '-11-01T00:00:00', 'enddate': '-11-30T23:59:00'},
                 {'month': 'December', 'startdate': '-12-01T00:00:00', 'enddate': '-12-31T23:59:00'}]

