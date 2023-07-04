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
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

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
