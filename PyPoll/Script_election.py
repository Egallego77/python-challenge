# #This will allow us to create file paths accross operating systems
import pathlib

# #Path to collect data from Recources folder
election_csvpath =pathlib.Path('PyPoll/Resources/election_data.csv')

#Module for reading CSV files
import csv

with open(election_csvpath, mode='r') as csvfile:
    #CSV reader specifies delimiter and variable that holds content 
    reader = csv.reader(csvfile, delimiter= ',')
    header = next(csvfile)

    votes = {}

    for row in reader:
        #complete list of canditates who received votes
        #candidates vote count
        candidate_name = row[2]

        if candidate_name in votes:
            votes[candidate_name] += 1
        else:
            votes[candidate_name] = 1
    
    print (votes)
    vote_counts = (list(votes.values()))

    # Total number of votes cast
    total_count = sum(vote_counts)
    print(total_count)

winner = list(votes.keys())[0]
votes_summary = {}
for candidate in votes.keys():
    if votes[candidate] >votes[winner]:
        winner = candidate
    votes_summary[candidate] = {'votes': votes[candidate], 'vote_pct': round((votes[candidate]/total_count)*100,2)}
    if candidate== winner:
        votes_summary[candidate]["is_winner"] = True
    else:
        votes_summary[candidate]["is_winner"] = False
print(votes_summary)
    
election_result = pathlib.Path('PyPoll/Analysis/election_results.txt')

with open(election_result,'w') as outputfile:
    csvwriter = csv.writer(outputfile)
    election_result = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_count}\n"
    f"-------------------------\n"
    )
    print(election_result, end="")
    outputfile.write(election_result)
    for candidate in votes_summary.keys():
        voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
        print(voter_output, end="")
        outputfile.write(voter_output)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
    outputfile.write(winning_candidate_summary)
    print(winning_candidate_summary)