debug = False  # Push False on Server
base_url='''https://data.cityofnewyork.us'''
location_master_data = '''https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'''

query_year = [{'year': 2019, 'keyval': '2upf-qytp'},
              {'year': 2020, 'keyval': 'kxp8-n2sj'}]

chunk_set = 6525000

payment_mode = '''[{"id" : 1, "val": "Credit card"},
                {"id" : 2, "val": "Cash"},
                {"id" : 3, "val": "No charge"},
                {"id" : 4, "val": "Dispute"},
                {"id" : 5, "val": "Unknown"},
                {"id" : 6, "val": "Voided trip"}] '''

