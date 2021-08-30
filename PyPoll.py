# Add our dependencies.
import csv
import os
## Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

## Open the election results and read the file.
with open(file_to_load) as election_data:
    # TO DO - read & analyze data
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:

    # Write 3 counties to file
        txt_file.write('Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson')

# Close the file
txt_file.close()

# 1) total # of votes cast
# 2) complete list of candidates who got votes
# 3) total # of votes/candidate
# 4) % of votes for each candidate
# 5) winner of election

## close the file
election_data.close()