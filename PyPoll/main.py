import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files
electionpath_csv = os.path.join('Resources', 'election_data_Test.csv')

# Specifying the file to write to
VoterSummaryWriteUp = os.path.join("Analysis", "Voting_Results_Ith.txt")


    # Definitions of variables: --------------------------------------------------------------------------------------

Counter = 0                         # 
TotalVotes = 0                      # The total number of votes cast
TotalCandidateVotes = 0             # The total number of votes each candidate won
Winner = ""                         # The winner of the election based on popular vote

CandidateWinPercentage = 0          # The percentage of votes each candidate won           


# List to hold the 3 rows ([0],[1],[2]) that our source file has data on
Voter_ID = []                       #
Voter_County = []                   #
Candidates_Running = []             # A complete list of candidates who received votes

# ------------------------------------------------------------------------------------------------------


# Open and read csv
with open(electionpath_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
        
    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")               #Test to see if header and csv is being read
    

# Code start: --------------------------------------------------------------------------------------
    i=0 # Iterator to return the specific position of values in the [] lists.
    
    for row in csv_reader:
        Voter_ID.append(row[0])
        Voter_County.append(row[1])
        Candidates_Running.append(row[2])
        
        TotalVotes += 1
        print(row)
    
print('--------------------------------------1' + '\n') 

    
print(TotalVotes)       # Original Result was: 3521001

print('--------------------------------------' + '\n') 
raise SystemExit
raise SystemExit































# Expected Results print on console terminal and text file...

#  -------------------------
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------


print('---------- End -------------' + '\n')
# Ithamar Francois