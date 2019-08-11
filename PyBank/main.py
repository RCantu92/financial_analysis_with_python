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

profit_int = 0
previous_month_profit_change = 0
profit_change = 0
profit_change_total = 0
total_entries = 0

# Make csv path into an object, in read version
with open(budget_data_path, 'r') as budget_data_file:
    
    # Pass in the csv file to the csv.reader() function (with ',' as the delmiter/separator)
    csv_reader = csv.reader(budget_data_file, delimiter = ',')
    
    # Skip the header row
    csv_header = next(csv_reader)
    
    # Make csv file into a list of lists
    csv_list = list(csv_reader)
    
    # Create a for loop to iterate through list items with two inputs: month, profit
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
        # And set the previous month's profit to solve for change
        previous_month_profit = profit
        total_months += 1
        net_total += profit
        
    # Create a for loop to iterate through profits to solve for average
    for month, profit_string in csv_list:
        
        # Convert profit index into intergers
        profit_int = int(profit_string)
        
        # Solve for profit change
        profit_change = profit_int - previous_month_profit_change
        
        # Set profit change to use to solve for the following month
        # Track total sum of profit changes
        previous_month_profit_change = profit_int
        profit_change_total += profit_change
        total_entries += 1
    
    # Solve for average of all profit changes and round to second decimal
    average_changes = round((profit_change_total / total_entries), 2)
        


# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")

# Set the output file path
output_path = Path("main.txt")

# Open the output path as a text object
with open(output_path, 'w') as txt_file:
    
    # Print results to txt_file
    print("Financial Analysis", file = txt_file)
    print("----------------------------", file = txt_file)
    print(f"Total Months: {total_months}", file = txt_file)
    print(f"Total: ${net_total}", file = txt_file)
    print(f"Average  Change: ${average_changes}", file = txt_file)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})", file = txt_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})", file = txt_file)