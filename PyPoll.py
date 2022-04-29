# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total Number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
import random
import numpy

file_to_load = "election_results.csv"

file_to_save = "election_analysis.txt"

# 1. Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

voter_turnout = 0
counties = []
county_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        # voter_turnout += 1
        #county_votes += 0
        county = row[1]

        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
#       # If county matches a county (county2) in the counties list += 1 to its votes.
        for county2 in counties:
            if county == county2:
                county_votes[county] += 1



with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    county_votes_results_summary = (
        f" \nCounty Votes:\n")
    txt_file.write(county_votes_results_summary)

    # Print the final vote count of each county.
    for county in counties:
        #county_name = county_votes[county]

        county_votes_results = (f"{county}: {county_votes[county]}\n")

    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        county_vote_spread = (f"{county}: {vote_percentage:.1f}% ({county_votes[county]:,})\n")

        #county_vote_spread_summary = (f"\n-------------------------\n")
        txt_file.write(county_vote_spread)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = county
            winning_percentage = vote_percentage

    county_winning_candidate_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_candidate}\n"
        f"-------------------------\n")

    txt_file.write(county_winning_candidate_summary)