# Total number of votes cast -
# A complete list of candidates who received votes -
# Total number of votes each candidate received - 
# Percentage of votes each candidate won - 
# The winner of the election based on popular vote
import csv
from itertools import count
import os

file_to_read = os.path.join('Resources/election_results.csv')
file_to_write = os.path.join('Analysis/election_analysis.txt')

def Winner_Check(candidates_votes, candidates):
    """ 
    Takes a dictionary with Candidates and their total votes. Compares each vote tally in order to find the candidates with the most votes

    Parameters:
            candidates_votes (dict): A dictionary containing Candidates and their vote tally
            candidates (list(String)): List containing candidates.

    Returns:
            leading (dict): Dictionary containing the winner's name and vote tally. 
    """
    leading = {"name":"None", 
                "count": 0}
    for keys in candidates_votes:
        if keys in candidates:
            if leading["count"] < candidates_votes[keys]:
                leading["name"] = keys
                leading["count"] = candidates_votes[keys] 
    return leading

def Most_Votes_County(county_votes, counties):
    """ 
    Takes a dictionary with counties and their total votes. Compares each vote tally in order to find the county with the most votes

    Parameters:
            county_votes (dict): A dictionary containing Candidates and their vote tally
            counties (List(String)): A list containing counties

    Returns:
            leading (dict): Dictionary containing the county which had the most votes cast from. 
    """
    leading = {"name":"None", 
                "count": 0}
    for keys in county_votes:
        if keys in counties:
            if leading["count"] < county_votes[keys]:
                leading["name"] = keys
                leading["count"] = county_votes[keys] 
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
    county_percent = {}

    # Iterate through the polling data
    for row in polling_data:
        # Organize rows into its own data set
        rows.append(row)

        # pull out candidats into there own data set and start a vote tally for each candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_totals[row[2]] = 0
        
        # pull out the County into its own data set and start a vote tally for each county
        if row[1] not in county:
            county.append(row[1])
            vote_totals[row[1]] = 0
        
        # Continue tallying the votes for each candidate while iterating through the rest of the data. 
        if row[2] in vote_totals.keys():
            vote_totals[row[2]] = vote_totals[row[2]] + 1
        
        # Continue tallying the votes for each county while iterating through the rest of the data. 
        if row[1] in vote_totals.keys():
            vote_totals[row[1]] = vote_totals[row[1]] + 1
    
    total_votes_cast = len(rows)

    # Calculating the percentag per candidate and per county
    for key in vote_totals:
        if key in candidates:
            p = (vote_totals[key] / total_votes_cast) * 100

            candidate_percent[key] = p
        elif key in county:
            p = (vote_totals[key] / total_votes_cast) * 100

            county_percent[key] = p
        
    winner = Winner_Check(vote_totals, candidates)
    county_who_voted_most = Most_Votes_County(vote_totals, county)

    print("Election Results")
    print("-"*65)
    print()
    print("County Votes:")
    for key in county_percent:
        print(f"{key}: {county_percent[key]:.1f}% ({vote_totals[key]:,})")
    print()
    print("-"*65)
    print(f'Largest County Turnout: {county_who_voted_most["name"]}')
    print("-"*65)
    print()
    for key in candidate_percent:
        print(f"{key}: {candidate_percent[key]:.1f}% ({vote_totals[key]:,})")
    print()
    print("-"*65)
    print(f'Winner: {winner["name"]}')
    print(f'Winning Vote Count: {winner["count"]:,}')
    print(f'Winning Percentage: {candidate_percent[winner["name"]]:.1f}%')
    print("-"*65)

# Safely open the rile to write to
with open(file_to_write, 'w') as file:
    # Write three counties to the file.
    file.write("Election Results\n")
    file.write("-"*25 + "\n")
    file.write(f'Total Votes: {total_votes_cast:,}\n')
    file.write("-"*25 + "\n")
    file.write("\n")
    file.write("County Votes: \n")
    for key in county_percent:
        file.write(f"{key}: {county_percent[key]:.1f}% ({vote_totals[key]:,})\n")
    file.write("\n")
    file.write("-"*25 + "\n")
    file.write(f'Largest County Turnout: {county_who_voted_most["name"]}\n')
    file.write("-"*25 + "\n")
    for key in candidate_percent:
        file.write(f"{key}: {candidate_percent[key]:.1f}% ({vote_totals[key]:,})\n")
    file.write("-"*25 + "\n")
    file.write(f'Winner: {winner["name"]}\n')
    file.write(f'Winning Vote Count: {winner["count"]:,}\n')
    file.write(f'Winning Percentage: {candidate_percent[winner["name"]]:.1f}% \n')
    file.write("-"*25 + "\n")