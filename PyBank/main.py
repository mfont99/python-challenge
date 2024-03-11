
import csv                                                                      # imports
import os

row_count = 0                                                                   # variables

running_total = 0

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""

first_month = True

current_profit = 0
previous_profit = 0

profit_change = 0
total_profit_change = 0

with open('Resources/budget_data.csv','r') as csv_file:                         # reading in raw data
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:

        row_count += 1                                                          # counts rows

        running_total += int(line[1])                                           # running total of profits

        current_profit = int(line[1])                                           # sets current profit value from .csv
        profit_change = current_profit - previous_profit
        
        if first_month is False:                                                # skips the profit change for the first month

            total_profit_change += profit_change                                # running total of profit changes

        if profit_change > greatest_increase:                                   # updates the greatest increase 

            greatest_increase = profit_change
            greatest_increase_month = line[0]                                   # updates the month where the greatest increase occurs 

        if profit_change < greatest_decrease:                                   # updates the greatest decrease

            greatest_decrease = profit_change
            greatest_decrease_month = line[0]                                   # updates the month where the greatest decrease occurs

        previous_profit = current_profit                                        # changes the previous profit to be the current one before moving on to the next row
        first_month = False                                                     # tells the loop that it's not the first month, so average changes start being calculated

    average_profit_change = total_profit_change/(row_count - 1)                 # calculates average profit change ("row_count - 1" because there is one fewer profit change than rows themselves)

    print(f'Financial Analysis\n\n--------------------------------\n')
    print(f'Total months: {row_count}\n')
    print(f'Total: ${running_total}\n')
    print(f'Average Change: ${average_profit_change:.2f}\n')                    # syntax for rounding to a specific number of decimal points from AI
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')



file_path = os.path.join("analysis","results.txt")                              # specifying file location

with open(file_path,'w') as results:                                            # writing to that file

    results.write(f'Financial Analysis\n\n--------------------------------\n')
    results.write(f'Total months: {row_count}\n')
    results.write(f'Total: ${running_total}\n')
    results.write(f'Average Change: ${average_profit_change:.2f}\n')
    results.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    results.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')