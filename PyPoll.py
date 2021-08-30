# Add our dependencies.
import csv
import os
## Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize vote counter & candidate options & candidate votes
total_votes=0
candidate_options=[]
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add to total vote count
        total_votes+=1
        # print candidate name from each row + list all available candidates
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        # begin tracking candidate's vote count + adding to vote count
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
             #  To do: print out the winning candidate, vote count and percentage to
             #   terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
   
    # Print the candidate list
##print(candidate_votes)      
    # Print the candidate list
##print(candidate_options)
    # Print the total votes.       
##print(f"A total of {total_votes:,} votes has been cast.")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write 3 counties to file
        txt_file.write(winning_candidate_summary)

# Close the file
        txt_file.close()

# 1) total # of votes cast
# 2) complete list of candidates who got votes
# 3) total # of votes/candidate
# 4) % of votes for each candidate
# 5) winner of election

## close the file
election_data.close()