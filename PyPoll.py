#Getting todays date
# Import the datetime class from the datetime module.
    # import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
    # now = dt.datetime.now()
# Print the present time.
    # print("The time right now is ", now)

# The Data we need to retrieve
#File_toload = 'Resources/election_results.csv'
#election_data = open(File_toload, 'r')
# To do: perform analysis. 

# Close the file. 
#election_data.close()

# Open the election results and read the file
#import csv
#from functools import total_ordering
#import os
#Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file. 
#with open(File_toload) as election_data:

    # To do: print the file object. 
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt") 
# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")
# Create a filename variable to a direct or indirect path to the file. 
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Add our dependencies. 
import csv
import os
# Assign a veriable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter. 
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declaring the empty dictionary: 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

#Open the election results and read the file. 
with open(file_to_load) as election_data:
    #To do: read and analyze the data: 
    file_reader = csv.reader(election_data)
    #Read & Print the header row.     
    headers = next(file_reader)
    # Print each row in the CSV file. 
    for row in file_reader:
        # 2. Ass to the total vote count. 
        total_votes += 1
        # Print the candidate name for each row. 
        candidate_name = row[2]
        # Add the candidate name to the candidate list. 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates. 
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
        # Determine the percentage of votes for each candidate by looping through the counts. 
        # 1. iterate thru the candidate list:
        
        #Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
            # Save the final vote count to the text file. 
    txt_file.write(election_results)
    for candidate_name in candidate_votes: 
        # 2. Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes. 
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print(winning_candidate_summary)
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




    
# 3. Print the total votes. 
# print(total_votes)
#Print the candidate list.
#print(candidate_options)
#Print the candidate vote dictionary.
# print(candidate_votes)

# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 