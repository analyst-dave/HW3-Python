import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    line_count = 0
    running_total = 0
    delta = 0
    delta_sum = 0
    greatest_gain = 0
    greatest_loss = 0
    previous_row = 0
    best_month = ''
    worst_month = ''

    # Read each row of data after the header
    for row in csvreader:
    
        # print(f'\t Date = {row[0]}, Profit/Losses = {row[1]}, delta = {int(row[1]) - previous_row}')
            
        delta = int(row[1]) - previous_row
        if previous_row != 0:
            delta_sum += delta

        if delta < 0: # loss
            if delta < greatest_loss: # check for greatest loss
                greatest_loss = delta
                worst_month = row[0] 
        else: # gain
            if delta > greatest_gain: # check for greatest gain
                greatest_gain = delta
                best_month = row[0]
                
        line_count += 1
        running_total += int(row[1])
        previous_row = int(row[1])

    print(f'Total Months: {line_count}')
    print(f'Running Total: ${running_total}')

    print(f'Delta sum: ${delta_sum}')
    print(f'Average  Change: ${(delta_sum)/line_count}')

    print(f'Greatest Increase in Profits: {best_month} (${greatest_gain})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_loss})')
        
