print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of counties.")

#Using "and" statement:
if "Arapahoe" in counties and "El Paso" in counties: 
    print("Arapahoe and El Paso are in the list of counties.")
else: 
    print("Arapahoe or El Paso is not in the list of counties.")

#Using the or or "either" statement: 
if "Arapahoe" in counties or "El Paso" in counties: 
    print("Arapahoe or El Paso is in the list of counties.")
else: 
    print("Arapahoe and El Paso are not in the list of counties.")

#Iterating through lists and tuples
for county in counties: 
    print(county)

#Using the "range()" function
numbers = [0, 1, 2, 3, 4]
for num in numbers: 
    print(num)

for num in range(5):
    print(num)

#Using indexing to iterate through a list with strings
for i in range(len(counties)):
    print(counties[i])

#Iterating through a tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

#iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#Using "keys()" method to iterate over a dictionary:
for county in counties_dict.keys():
    print(county)
#or 
for county in counties_dict:
    print(counties_dict[county])
#Using "get()" method on the dictionary in the for loop
for county in counties_dict:
    print(counties_dict.get(county))

#Now getting the values of a dictionary using "values()"
for voters in counties_dict.values():
    print(voters)

#Getting the key-value pairs in a dictionary using "items()"
#for key, value in dictionary_name.items():
    #print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

#Getting each dictionary in a list of dictionaries
voting_data = [{"county": "Arapahoe", "Registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data: 
    print(county_dict)
#Using the "range()" function to iterate over the list. 
for i in range(len(voting_data)): 
    print(voting_data[i]['county'])

#Getting the values from a list of dictionaries using nested for loops
for county_dict in voting_data: 
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

