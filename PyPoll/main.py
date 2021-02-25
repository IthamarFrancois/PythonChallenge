import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files
electionpath_csv = os.path.join('Resources', 'election_data_Test.csv')

# Specifying the file to write to
VoterSummaryWriteUp = os.path.join("Analysis", "Voting_Results_Ith.txt")


    # Definitions of variables: --------------------------------------------------------------------------------------

Counter = 0                         # 
TotalVotes = 0                      # The total number of votes cast
TotalCandidateVotes = 0             # The total number of votes each candidate won

CurrentPolitician = ""
Winner = ""                         # The winner of the election based on popular vote

CandidateWinPercentage = 0          # The percentage of votes each candidate won           


# List to hold the original 3 rows ([0],[1],[2]) that our source file has data on
Voter_ID = []                       #
Voter_County = []                   #
Candidates_Running = []             # A complete list of candidates who received votes

Candidates = dict()

Counted_Votes = []                  # Custom list for Misc
Custom_List = []                    # Custom list for Misc
Custom_List = []                    # Custom list for Misc

Custom_Sort = []                    # Custom list for Misc
Custom_Candidates = []              # Custom list for Misc
# ------------------------------------------------------------------------------------------------------


# Open and read csv
with open(electionpath_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
        
    # Read the header row first
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")               #Test to see if header and csv is being read
    

# Code start: --------------------------------------------------------------------------------------
    i=0 # Iterator to return the specific position of values in the [] lists.
    
    for row in csv_reader:
        TotalVotes += 1
        #Voter_ID.append(row[0])
        #Voter_County.append(row[1])
        #Counted_Votes
        Candidates_Running.append(row[2])
        #Candidates_Running.count(row[2])
        




    for i in range(len(Candidates_List)):
        CurrentPolitician = Candidates_List[i]
        if CurrentPolitician[i] in Candidates_Running:
            #print("Yes")
        
        
        else CurrentPolitician[i] not in Candidates_Running:







    for i in range(len(Candidates_Running)):
        CurrentPolitician = Candidates_Running[i]
        
        if Candidates_Running[i] in Candidates:
            print("Yes")
        if Candidates_Running[i] not in Candidates:
            Candidates[i] = {"Name": CurrentPolitician}
            print("No")
           
        
    print(f'{Candidates["Name"]}')     


        
        #if (Candidates_Running[i].count > 0) and (Candidates_Running[i] > GreatestInc):
        #    GreatestInc = Candidates_Running[i]
        #    GreatestMonth = Date_Data[i]
                
        #if (Profit_Change[i] < 0) and (Profit_Change[i] < GreatestDec):
        #    GreatestDec = Profit_Change[i]
        #    LowestMonth = Date_Data[i]
        #print(Candidates_Running[i]) 




        # ???
        # Custom_Sort = sorted(Candidates_Running)
        # Custom_Sort = sorted(Candidates_Running, reverse=True)
        # Custom_Sort.sort(reverse=True)

        #print(Candidates_Running.count(row[2]))
        #print(Candidates_Running.count(row[2]))

        #print(row)                          # [0],[1],[2]
    
print('--------------------------------------1' + '\n') 

    
#print(TotalVotes)       # Original Result was: 3521001, test sheet is: 199 (200 rows - 1 for header)

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