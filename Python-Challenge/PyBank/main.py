#Dependency loads
import os
import csv

#File to load
budget_file = os.path.join ("/Users/basy/Desktop/homework/Python-Challenge/PyBank/Resources/budget_data.csv")

#Folder name to export final document
file_export = ("/Users/basy/Desktop/homework/Python-Challenge/PyBank/pybank_analysis.txt")

#The output we want
total_months = 0
last_revenue = 0
value = 0
change = 0
profits = []

#Opening and reading the CSV file
with open(budget_file) as new_data:
    csvreader = csv.DictReader(new_data)

#Finding the rows in data
    for row in csvreader:
    
# reveneue row
revenue = row["Profit/Losses"]
    
#Revenue total
        last_revenue = last_revenue + int(float(row["Profit/Losses"])
    
#month total
        #total_months = total_months + 1

#Track the changes properly
        revenue_change = int(float(row["Profit/Losses"]) - last_revenue
        previous_revenue = int(row["Profit/Losses"])
        change = change + [change_in_revenue]
                                          
        change = int(row[1]) - change_in_revenue
        profits.append(change)
        value = int(row[1])

#Greatest increase and average
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        avg_change = sum(profits)/len(profits)
        month_of_change = month_of_change + [row["Date"]]

#Greatest decrease (lowest increase) in profits 
        greatest_decrease = min(profits)
        worst_decrease = profits.index(greatest_decrease)  
   

#Output for .txt
f"\n\n\Financial Analysis\n"
f"---------------------\n"
f"Total Months: {str(total_months)}"
f"---------------------\n"
f"Total: ${str(total_pl)}"
f"Average Change: ${str(round(avg_change,2))}"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

#Exporing .txt file to PyBank file
print(output)
with open ("/Users/basy/Desktop/homework/Python-Challenge/PyBank/pybank_analysis.txt", "w") as txt_file:
    txt_file.write(output)
