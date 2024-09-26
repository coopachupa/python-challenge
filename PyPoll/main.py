import csv
import os
csvpath = os.path.join ("Resources", 'election_data.csv') 
with open(csvpath) as csv_file:
    csvreader = csv.reader (csv_file)

    csv_header = next (csv_file)
    print (f"Header: {csv_header}")



