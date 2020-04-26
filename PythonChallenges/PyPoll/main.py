import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
fh = open("PyPollOutput.txt", "w")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    winner = ""
    winning_votes = 0
    poll = {}
    candidates = {}
    line_count = 0
    votes = 0

    # Read each row of data after the header
    for row in csvreader:
        poll[row[0]] = row[2]
        candidates[row[2]] = row[2]
        line_count += 1    

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {line_count}')
    print('-------------------------')

    fh.write(f'Election Results\n')
    fh.write(f'-------------------------\n')
    fh.write(f'Total Votes: {line_count}\n')
    fh.write(f'-------------------------\n')

    for role in candidates.keys():
        
        for key in poll.keys():
            if poll.get(key) == role:
                votes += 1

        if votes > winning_votes:
            winning_votes = votes
            winner = role

        temp = "{:.3%}".format(votes/line_count)
        print(f'{role}: {temp} ({votes})')
        fh.write(f'{role}: {temp} ({votes})\n')
        votes = 0

    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

    fh.write("-------------------------\n")
    fh.write(f'Winner: {winner}\n')
    fh.write("-------------------------\n")
    fh.close()