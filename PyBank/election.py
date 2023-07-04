import os
import csv

# Set relative path for csv file
path = "./Resources/election_data.csv"

#Variables
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

# Read csv file
with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Reading header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # Calculate percentage of votes for each candidate
    for votes in num_votes:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        percentage = "{:.3f}%".format(percentage)
        percent_votes.append(percentage)

    # Find the winning candidate
    winner_votes = max(num_votes)
    winner_index = num_votes.index(winner_votes)
    winning_candidate = candidates[winner_index]

# Printing the output
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to text file
output_file = os.path.join('Analysis', 'pyPoll_output.txt')

with open(output_file, "w") as pyPolloutput:
    pyPolloutput.write("Election Results\n")
    pyPolloutput.write("--------------------------\n")
    pyPolloutput.write(f"Total Votes: {total_votes}\n")
    pyPolloutput.write("--------------------------\n")
    for i in range(len(candidates)):
        pyPolloutput.write(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})\n")
    pyPolloutput.write("--------------------------\n")
    pyPolloutput.write(f"Winner: {winning_candidate}\n")
    pyPolloutput.write("--------------------------\n")
