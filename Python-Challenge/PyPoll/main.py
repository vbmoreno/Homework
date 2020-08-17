#Dependency loads
import os
import csv

#File to load
budget_file = os.path.join ("/Users/basy/Desktop/homework/Python-Challenge/PyPoll/Resources/election_data.csv")

#Folder name to export final document
file_export = ("/Users/basy/Desktop/homework/Python-Challenge/PyBank/election_analysis.txt")

#The output we want
candidate_votes = {}
total_votes = 0
candidate_array = []
winning_candidate = ""
winning_count = 0


#Opening and reading the CSV file
with open(budget_file) as new_data:
    csvreader = csv.DictReader(new_data)

#Finding the rows in data
    for row in csvreader:
    
    #candidates row
        candidates = row["Candidate"]

# total votes
    total_votes = total_votes + 1
 

#Track the changes properly
    if candidates not in candidate_array:

        #Greatest increase and average
        candidate_votes[candidates] = 0
        candidate_array.append(candidates)



#Displaying information
output = (
f"\n\n\Financial Analysis\n"
f"---------------------\n"
f"Total Votes: {str(total_votes)}"
f"---------------------\n"
)

#Exporing .txt file to PyBank file
print(output)
with open ("/Users/basy/Desktop/homework/Python-Challenge/PyPoll/election_analysis.txt", "w") as txt_file:
    txt_file.write(output)
