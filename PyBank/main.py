# #This will allow us to create file paths accross operating systems
import pathlib

# #Path to collect data from Recources folder
csvpath =pathlib.Path('Resources/budget_data.csv')

# # Module for reading CSV files
import csv

with open(csvpath, mode='r') as csvfile:
  #CSV reader specifies delimiter and variable that holds content 
  reader = csv.reader(csvfile, delimiter= ',')

  total_months = 1
  total_PL = 0
  previous_PL = 0
  
  #Read the header row first (skip ths step if there is now header)
  header = next(csvfile)
  #print(f"CSV Header: {header}")
  
  first_row = next(reader)
  previous_PL = int(first_row[1])
  changes = []
  months = []

  for row in reader:
  #total number of months included in the dataset
    total_months += 1
    months.append(row[0])

  #net total amount of P&L over the entire period
    PL = int(row[1])
    total_PL += PL

  # average of the changes in "Profit/Losses" over the entire period
    PL_change = PL - previous_PL
    changes.append(PL_change)
    previous_PL = PL
  
  average_change = sum(changes) / (total_months-1)

# greatest increase in profits (dates and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]
print(greatest_increase_month)


# greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]
print(greatest_decrease_month)



print("Financial Analysis")
print("------------------")
print("Total Months:" + str(total_months))
print("Total:" + str(total_PL))
print(f'Average change: {str(average_change)}')
print (f'Greatest Increase in Profits: {str(greatest_increase_month)} ${str(greatest_increase)}')
print (f'Greatest Decrease in Profits: {str(greatest_decrease_month)} ${str(greatest_decrease)}')
print(changes)


