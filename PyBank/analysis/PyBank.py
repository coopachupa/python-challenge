# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/cooper/Desktop/python-challenge2/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("./Users/cooper/Desktop/python-challenge2/PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_net = None
greatest_increase = {'month': '', 'amount': 0}
greatest_decrease = {'month': '', 'amount': 0}  

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total months and net
        total_months += 1
        total_net += int(row[1])

        # Calculate the net change
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        previous_net = int(row[1])

        # Calculate the greatest increase in profits
        if net_change > greatest_increase['amount']:
            greatest_increase['month'] = row[0]
            greatest_increase['amount'] = net_change

        # Calculate the greatest decrease in losses
        if net_change < greatest_decrease['amount']:
            greatest_decrease['month'] = row[0]
            greatest_decrease['amount'] = net_change

# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Losses: {greatest_decrease['month']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
