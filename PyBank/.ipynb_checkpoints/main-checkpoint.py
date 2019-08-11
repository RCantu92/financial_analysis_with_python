# Import Path from pathlib
from pathlib import Path
# Import csv
import csv

# Set csv path to a variable
budget_data_path = Path("budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
average_changes = 0
greatest_increase_amount = 0
greatest_increase_month = None
greatest_decrease_amount = 0
greatest_decrease_month = None
previous_month_profit = 0

# Make csv path into an object, in read version
with open(budget_data_path, 'r') as budget_data_file:
    
    # Pass in the csv file to the csv.reader() function (with ',' as the delmiter/separator)
    csv_reader = csv.reader(budget_data_file, delimiter = ',')
    
    # Skip the header row
    csv_header = next(csv_reader)
    
    # Make csv file into a list of lists
    csv_list = list(csv_reader)
    
    # Create a foor loop to iterate through list items with two inputs: month, profit
    for month, profit_string in csv_list:
        
        # Convert profit index into intergers
        profit = int(profit_string)
        
        # Logic to determine greatest decease and increase amounts and months
        if total_months == 0:
            previous_month_profit = profit
            
        elif profit < previous_month_profit and profit < greatest_decrease_amount:
            greatest_decrease_amount = profit - previous_month_profit
            greatest_decrease_month = month
            
        elif profit > previous_month_profit and profit > greatest_increase_amount:
            greatest_increase_amount = profit - previous_month_profit
            greatest_increase_month = month
            
            
        # Calculate the total_months and net_total through the iterations
        previous_month_profit = profit
        total_months += 1
        net_total += profit
    
    average_changes = round((net_total / (total_months - 1)), 2)

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
# print(f"Average  Change: ${average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")