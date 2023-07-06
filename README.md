# Py Bank 
import os
import csv

path = "./Resources/budget_data.csv"

#Variables
total_months = 0
total_profit_loss = 0
changes = []
dates = []

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    prev_profit_loss = 0

    for row in csvreader:
        dates.append(row[0])
        profit_loss = int(row[1])
        total_months += 1
        total_profit_loss += profit_loss

        if total_months > 1:
            change = profit_loss - prev_profit_loss
            changes.append(change)

        prev_profit_loss = profit_loss

avg_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index + 1]
greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index + 1]

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file = os.path.join('Analysis', 'pyBank_output.txt')

with open(output_file, "w") as pyBankoutput:
    pyBankoutput.write("Financial Analysis\n")
    pyBankoutput.write("-----------------------------\n")
    pyBankoutput.write(f"Total Months: {total_months}\n")
    pyBankoutput.write(f"Total: ${total_profit_loss}\n")
    pyBankoutput.write(f"Average Change: ${avg_change:.2f}\n")
    pyBankoutput.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    pyBankoutput.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")



# Py Poll
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
