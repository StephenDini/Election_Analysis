# Total number of votes cast -
# A complete list of candidates who received votes -
# Total number of votes each candidate received - 
# Percentage of votes each candidate won - 
# The winner of the election based on popular vote
import csv
from itertools import count
import os

file_to_read = os.path.normpath('Resources\\election_results.csv')
file_to_write = os.path.normpath('Analysis\\election_analysis.txt')

def Winner_Check(candidates_votes):
    """ 
    Takes a dictionary with Candidates and their total votes. Compares each vote tally in order to find the candidates with the most votes

    Parameters:
            candidates_votes (dict): A dictionary containing Candidates and their vote tally

    Returns:
            leading (dict): Dictionary containing the winner's name and vote tally. 
    """
    leading = {"name":"None", 
                "count": 0}
    for keys in candidates_votes:
        if leading["count"] < candidates_votes[keys]:
            leading["name"] = keys
            leading["count"] = candidates_votes[keys] 
    return leading

# Safely open the file to read from
with open(file_to_read) as file:
    polling_data = csv.reader(file)
    header = next(polling_data)
    total_votes_cast = 0
    rows = []
    candidates = []
    county = []
    vote_totals = {}
    candidate_percent = {}

    # Iterate through the polling data
    for row in polling_data:
        # Organize rows into its own data set
        rows.append(row)

        # pull out candidats into there own data set and start a vote tally for each
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_totals[row[2]] = 0
        
        # pull out the County into its own data set
        if row[1] not in county:
            county.append(row[1])
        
        # Continue tallying the votes while iterating through the rest of the data. 
        if row[2] in vote_totals.keys():
            vote_totals[row[2]] = vote_totals[row[2]] + 1
    
    total_votes_cast = len(rows)
    keys = vote_totals.keys()
    values = vote_totals.values()

    # Calculating the percentag per candidate
    for key in vote_totals:
        p = (vote_totals[key] / total_votes_cast) * 100

        candidate_percent[key] = p
    
    winner = Winner_Check(vote_totals)

    print(total_votes_cast)
    print(header)
    print(candidates)
    print(county)
    print(vote_totals)
    print(keys)
    print(values)
    print(candidate_percent)
    print(winner)

    print("-"*65)
    for key in candidate_percent:
        print(f"{key}: recieved ({vote_totals[key]:,}) {candidate_percent[key]:.1f}% of the votes.")
    print(f'The winner is {winner["name"]} with {winner["count"]:,} total votes.')
    print(f'They won by earning {candidate_percent[winner["name"]]:.1f}% of the votes')
    print("-"*65)

# # Safely open the rile to write to
# with open(file_to_write, 'w') as file:
#     # Write three counties to the file.
#      file.write("Countries in Election\n")
#      file.write("-"*25 + "\n")
#      file.write("Araphoe\n")
#      file.write("Denver\n")
#      file.write("Jefferson\n")