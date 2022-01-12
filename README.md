# election_analysis
Using Visual Studio Code in Module 3: PyPoll with Python

## Project Overview: 
Seth and Tom, Colorado Board of Elections employees have given you tasks to complete the election audit of a recent local congressional election. Using Python 3.10.1, and Visual Studio Code, you will complete the following: 

1. Calculate the total # of votes to cast. 
2. Get a complete list of candidates who recieved votes. 
3. Calculate the total number of votes each candidate recieved. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

##Resources: 
- Data source: election_results.csv; located in: /Users/henrybarze/Desktop/VDAB Projects/Modules/Module 3- PyPoll With Python/Module Files/election_analysis
- Software: Python 3.10.1 64-bit, using VS Code Version: 1.63.2 (Universal)

## Summary: 
The Analysis of the election shows that:
- There were 369,711 total votes cast in the election. 
- The Candidates were:
  Charles Casper Stockham
  Diana DeGette
  Raymon Anthony Doane
  
- The candidate results were: 
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was: 
  Winner: Diana DeGette
 
## 1. Challenge Overview:
The election commission has requested some additional data to complete the audit: 
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
Working with the election_results.csv file, use for loops, conditional statements, membership and logical operators to find the results. 

## 2. Challenge Summary: 
- How many votes were cast in this congressional election?
  - Total Votes: 369,711

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct:
  - We used a for loop to iterate through the csv file, then retrieved the county vote count by counting each vote for a certain county name. The for loop knows to add to the count of each county name because in step #4 we created a conditional statment where if the county name of the vote was not previously included in our county_list variable, then that county name was appended to the county_list variable. Lastly, as seen in the screenshot below, in step #5 we state that if the county_name is included in county_list, then that county_name is added (from the notation += 1) to that county's vote. 
<img width="485" alt="Screen Shot 2022-01-11 at 10 56 12 PM" src="https://user-images.githubusercontent.com/96043107/149072014-3b6d2c20-b777-4893-b87b-91a73b57fd2f.png">

The percentage of total votes code begins by creating a county_vote_percentage variable before the first "with open()" statement by setting it equal to zero. Then, as seen in the screenshot below, in step #6 we set our county_vote_percentage equal to the "float(votes) / float(total_votes) * 100". We use the "float" notation to change the "votes" and "total_votes" variables from integers to floating-point decimal numbers. 
<img width="774" alt="Screen Shot 2022-01-11 at 11 04 33 PM" src="https://user-images.githubusercontent.com/96043107/149072833-c35d65ec-a947-4b50-8d2d-2a5c6057096d.png">


- Which county had the largest number of votes?
  - Denver county did, with 306,055 votes. 

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Repeated question. 
  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  -The winner was Diana DeGette with 272,892 votes making up 73.8% of the total votes. 
 
## Election-Audit Summary: 
- Provide a business proposal to the election commission on how this script can be used-with some modifications- for any election. Give at least two examples of how this script can be modified to be used for other elections. 
  - This script can be used currently on csv files that contain the following information about a vote: The Ballot ID, the county, and the candidate. For other elections, further code would need to be written for more descriptive variables depending on the level of election-- for example, in a presidential election, code would need to be written for which state the vote was cast in. Also, if an election ballot requested futher information about the voter, such as their political party affiliate, thosee could also be included in the analysis. Lastly, cases where a ballot has not been properly filled out, or where there are null values in the dataset, would be able to be accounted for and included in our analysis. 
