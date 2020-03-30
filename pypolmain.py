# Module
import os
import csv

pwd

# Import and open path location
csvpath = "./budget_data.csv"
csvpath_output = ("./budget_data.txt")

with open("./budget_data.csv") as election_data.csv:
    csvreader = csv.reader(election_data.csv)


# List to store data
total_votes = 0
List_candidates = []
percentage_votes = 0
votes_candidates = ["",0]
popular_vote=[]

for row in election_data.csv:
    total_votes =  votes + 1
   List_candidates = row[candidates]
   percentage_votes = ((candidate/votes)*100) + "%"))
   popular_vote = 

# Export text file
  "Election Results\n"
    " \n"
    "-----------------------------------------\n"
f'Total Votes: {total_votes}\n'
 " \n"
    "-----------------------------------------\n"
f'List_candidates{List_candidates}\n'
 " \n"
    "-----------------------------------------\n"
f'Winner: {popular_vote}\n'
" \n"
    "-----------------------------------------\n"
