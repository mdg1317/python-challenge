# Modules
import os
import csv

# File path
# Used from Python documentation https://docs.python.org/3/library/os.path.html
path = os.path.dirname(os.path.abspath(__file__))

# Variables
totalMonths = 0
totalProfit = 0
change = 0
averageChange = 0
greatestIncrease = 0
greatestIncreaseMonth = "None"
greatestDecrease = 0
greatestDecreaseMonth = "None"

# Open CSV
with open(f"{path}\\Resources\\budget_data.csv", encoding='UTF-8') as csvFile:
    # Read CSV
    csvReader = csv.reader(csvFile, delimiter=",")

    # Remove header
    csvHeader = next(csvReader)

    # Convert CSV to list
    csvRows = list(csvReader)

    for i in range(len(csvRows)):
        # Increment total months and add new profit
        totalMonths += 1
        totalProfit += int(csvRows[i][1])

        if(i > 0):
            # Get current profit change
            change = int(csvRows[i][1]) - int(csvRows[i - 1][1])

            # Check if current change is either greater than current greatest increase
            # or less than current greatest decrease and set accordingly
            if(change > greatestIncrease):
                greatestIncrease = change
                greatestIncreaseMonth = csvRows[i][0]
            elif(change < greatestDecrease):
                greatestDecrease = change
                greatestDecreaseMonth = csvRows[i][0]

            # Add current change to the accumulated previous changes
            averageChange += change

    # Get average profit change
    # round() function used from Python documentation https://docs.python.org/3/library/functions.html#round
    averageChange = round(averageChange / (totalMonths - 1), 2)

# Print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {totalMonths}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")

# Write results to text file
with open(f"{path}\\budget_data_output.txt", 'w') as txtFile:
    txtFile.write("Financial Analysis\n")
    txtFile.write("----------------------------\n")
    txtFile.write(f"Total months: {totalMonths}\n")
    txtFile.write(f"Total: ${totalProfit}\n")
    txtFile.write(f"Average Change: ${averageChange}\n")
    txtFile.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    txtFile.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})\n")