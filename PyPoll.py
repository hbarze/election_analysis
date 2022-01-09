#Getting todays date
# Import the datetime class from the datetime module.
    # import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
    # now = dt.datetime.now()
# Print the present time.
    # print("The time right now is ", now)

# The Data we need to retrieve
File_toload = 'Resources/election_results.csv'
election_data = open(File_toload, 'r')
# To do: perform analysis. 

# Close the file. 
election_data.close()

# Open the election results and read the file
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file. 
with open(File_toload) as election_data:

    # To do: print the file object. 
    print(election_data)

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
#Open the election results and read the file. 
with open(file_to_load) as election_data:
    #To do: read and analyze the data: 
    file_reader = csv.reader(election_data)

    #Read & Print the header row.     
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 