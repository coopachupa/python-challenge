import csv
import os
csvpath = os.path.join ("Resources", 'budget_data.csv') 
with open(csvpath) as csv_file:
    csvreader = csv.reader (csv_file)

    csv_header = next (csv_file)
    print (f"Header: {csv_header}")

#   I am looking at this profit and loss data to how much money was made and lost every month 
#   I first need to name all the variables in order to "store" the information or calculations 
