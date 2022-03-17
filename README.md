# Election_Analysis
## Poject Overview
A Colorado Board of Elections employee has given you the following tasks to complet the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes aech candidate rcieved. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election bsed on popular vote.

## Resources

* Data Source: election_results.csv
* Software: 
	* Pyton 3.10.1
	* VSCode 1.65.2
	* Sublime Text Build 4126

## Summary
The analysis of the election show that:

* There were "369,711" votes cast in the election.
* The candidates were:
	* Charles Casper Stockham
	* Diana DeGette
	* Raymon Anthony Doane
* The candidate results were:
	* Charles Casper Stockham recieved "23.0%" of the vote and "85,213" number of votes.
	* Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes.
	* Raymon Anthony Doane recieved "3.1%" of the vote and "11,606" number of votes.
* The winner of te election was:
	* Diana DeGette who recieved "73.8%" of the vote and "272,892" number of votes. 

## Challenge Overview
The Colorado Board of Elections requested more information in order to have a better image of where the votes are coming from. 

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Challenge Summary
The analysis of the newly requested information show that:

* The County's were:
	* Jefferson
	* Denver
	* Arapahoe
* The counties turn outs were:
	* The votes from Jefferson contributed to 10.5% of the total vote and 38,855 votes were cast in this county. 
	* The votes from Denver contributed to 82.8% of the total vote and 306,055 votes were cast in this county.
	* The votes from Araphoe contributed to 6.7% of the total vote and 24,801 votes were cast in this county.
* The county with the largest Turnout was:
	* Denver

## Code Snippets
Both candidates and county percentage results were computed using the orginal dictionary. Since we use a key to find the values this kept variables to a minimum. A conditional was added in order to filter between the two.

```python
# Continue tallying the votes for each candidate while iterating through the rest of the data. 	
if row[2] in vote_totals.keys():
	vote_totals[row[2]] = vote_totals[row[2]] + 1

# Continue tallying the votes for each county while iterating through the rest of the data. 
if row[1] in vote_totals.keys():
	vote_totals[row[1]] = vote_totals[row[1]] + 1
```
```python
# Calculating the percentag per candidate and per county
for key in vote_totals:
        if key in candidates:
            p = (vote_totals[key] / total_votes_cast) * 100

            candidate_percent[key] = p
        elif key in county:
            p = (vote_totals[key] / total_votes_cast) * 100

            county_percent[key] = p
```

I chose to encapsulate two functions, Winner_Check() and Most_Votes_Country() so that they could be reused easily if neccessary. Both have a docstring comment added for clarification.

```python
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
```

## Reusability
This code has been writen such that any data matching the same format will be able to produce an accurate analysis. 

## Extending functionality
In order to verify the results if might be best to implement a function which will verify that the Ballot IDs are unique. A print out alerting an official that an investigation might be needed can also be created. 