# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Define file paths for input and output
file_to_load = os.path.join("/Users/cooper/Desktop/python-challenge2/PyPoll/Resources/election_data.csv")  # Input CSV file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to store candidate names and their vote counts

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row in the CSV file
    for row in reader:
        total_votes += 1  # Increment total vote count
        candidate = row[2]  # Candidate name is in the third column

        # Increment the candidate's vote count in the dictionary
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Calculate percentage of votes for each candidate and find the winner
winner = None
max_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    # Check if the current candidate has more votes than the current winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Generate the output summary
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Append each candidate's results to the output
for candidate, votes, percentage in results:
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the output to the terminal
print(output)

# Save the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
