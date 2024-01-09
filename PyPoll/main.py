# Modules
import os
import csv

# File path
# Used from Python documentation https://docs.python.org/3/library/os.path.html
path = os.path.dirname(os.path.abspath(__file__))

# Variables
totalVotes = 0
candidateData = []

# Open CSV
with open(f"{path}\\Resources\\election_data.csv", encoding='UTF-8') as csvFile:
    # Read CSV
    csvReader = csv.reader(csvFile, delimiter=",")

    # Remove header
    csvHeader = next(csvReader)

    # Convert CSV to list
    csvRows = list(csvReader)

    for i in range(len(csvRows)):
        # Increment total votes regardless of who for
        totalVotes += 1

        # Add new candidate to list if not already added
        # If they are already there, increment their votes by 1
        # any() function used from https://stackoverflow.com/questions/3897499/check-if-value-already-exists-within-list-of-dictionaries-in-python
        # next() function used from https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
        if(not any(d["name"] == csvRows[i][2] for d in candidateData)):
            candidateData.append({"name": csvRows[i][2], "votes": 1})
        else:
            candidateData[next((index for (index, d) in enumerate(candidateData) if d["name"] == csvRows[i][2]), None)]["votes"] += 1
        

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for i in range(len(candidateData)):
    print(f"{candidateData[i]["name"]}: {round((candidateData[i]["votes"] / totalVotes) * 100, 3)}% ({candidateData[i]["votes"]})")
print("-------------------------")
# max() function used from https://stackoverflow.com/questions/5320871/how-to-find-the-min-max-value-of-a-common-key-in-a-list-of-dicts
print(f"Winner: {max(candidateData, key=lambda x:x["votes"])["name"]}")
print("-------------------------")

# Write results to text file
with open(f"{path}\\election_data_output.txt", 'w') as txtFile:
    txtFile.write("Election Results\n")
    txtFile.write("-------------------------\n")
    txtFile.write(f"Total votes: {totalVotes}\n")
    txtFile.write("-------------------------\n")
    for i in range(len(candidateData)):
        txtFile.write(f"{candidateData[i]["name"]}: {round((candidateData[i]["votes"] / totalVotes) * 100, 3)}% ({candidateData[i]["votes"]})\n")
    txtFile.write("-------------------------\n")
    # max() function used from https://stackoverflow.com/questions/5320871/how-to-find-the-min-max-value-of-a-common-key-in-a-list-of-dicts
    txtFile.write(f"Winner: {max(candidateData, key=lambda x:x["votes"])["name"]}\n")
    txtFile.write("-------------------------\n")
