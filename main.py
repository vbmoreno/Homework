# Module
import os
import csv

pwd

# Import and open path location
with open{budget_data, 'r', newline=""} as budget_data.csv:
    csvreader = csv.reader (budget_data.csv, delimeter=',')
    csv_header = next(budget_data.csv)

budget_data = os.path.join("desktop", "budget_data.csv")
csvreader = csv.reader(budget_data.csv)

# List to store data
total_months=0
total_profit=0
average_change=0
greatest_increase=[]
greatest_decrease=[]
P = []
months = []

# Row instructions for printing
for row in csvreader:
    P.append(int(row[1]))
    months.append(row[0])
        print(row)

# Row formulas
total_months = len(months)
total_profit = 
average_change = sum(profits)/len(profits)

for row in budget_data.csv:
    if str(greatest_increase) in row:
        greatest_increase = row[0]
    if str(greatest_increase) in row:
        greatest_decrease = row[0]

# Export text file
  "Financial Analysis\n"
    " \n"
    "-----------------------------------------\n"
f'Total Months:{total_months}\n'
f'Total Profits: {total_profit}\n'
f'Average Change: {average_change}\n'
f'Greatest Increase: {greatest_increase}\n'
f'Greatest Decrease: {greatest_decrease}\n'
