import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files
electionpath_csv = os.path.join('Resources', 'election_data_Test.csv')

# Specifying the file to write to
VoterSummaryWriteUp = os.path.join("Analysis", "Voting_Results_Ith.txt")

# ------------------------------------------------------------------------------------------------------

# Open and read csv
with open(electionpath_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
        
    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")               #Test to see if header and csv is being read
    

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






    
    ProfitThisMonth = 0                 # Tracker for the profit gain/loss this particular month
    PreviousMonthProfit = 0             # Reset/start amount of previous profit values to help calculate next "Profit/Losses" changes
    
    MonthlyChange = 0                   # Variable to represent the change in values between this month - last month. 
                                        # Data sent to Profit_Change list for new for loop to find greatest profit/months increase/decrease.
    
    MonthlyChangeSum = 0                # The sum of each month/year's overall changes together
    AvgProfLossChange = 0               # Variable to hold the rounded average of the overall Profit/Losses changes 
    
    GreatestInc = 0                     # The greatest increases in profits (date and amount) over the entire period
    GreatestMonth = 0
    
    GreatestDec = 0                     # The greatest decreases in losses (date and amount) over the entire period
    LowestMonth = 0         

    Profit_Change = []                  # List To hold changes of months' profits to help calculate increases/decreases in profits 
    Date_Data = []                      # List To hold list position/dates and help calculate the changes month to month
    
    


    #raise SystemExit
# Code start: --------------------------------------------------------------------------------------
    i=0 # Iterator to return the specific position of values in the [] lists.
    
    for row in csv_reader:
        Voter_ID.append(row[0])
        Voter_County.append(row[1])
        Candidates_Running.append(row[2])
        
        TotalVotes += 1
        print(row)
        
        ProfitThisMonth = int(row[1])
        MonthlyChange = (ProfitThisMonth - PreviousMonthProfit)
        Profit_Change.append(MonthlyChange)
        MonthlyChangeSum  =  MonthlyChangeSum + MonthlyChange
        PreviousMonthProfit = ProfitThisMonth
        
        MonthCounter += 1
        TotalAmount = int(row[1]) + TotalAmount
        

    for i in range(len(Profit_Change)):
        
        if (Profit_Change[i] > 0) and (Profit_Change[i] > GreatestInc):
            GreatestInc = Profit_Change[i]
            GreatestMonth = Date_Data[i]
        if (Profit_Change[i] < 0) and (Profit_Change[i] < GreatestDec):
            GreatestDec = Profit_Change[i]
            LowestMonth = Date_Data[i]
        #print(Profit_Change[i])   Used to show results of for loop values in terminal

    AvgProfLossChange = round((MonthlyChangeSum - (Profit_Change[0])) / (len(Profit_Change)-1),2)
    # The average for the changes in profits/loss = The sum of months changes - the first row of data's value (since it shouldn't count)
    #   Divided by the number of rows of months in the data list (86) minus one since list starts at position [0] so 85. Result is rounded 2 decimals
    print('\n')  # New line for spacing
    
    
    #print('----- Checks to show what the values of specific variables are by code's end -----' + '\n') 
    #print(MonthlyChangeSum)
    #print(Profit_Change[0])
    #print(len(Profit_Change)-1)
    #print(i)
    #print(MonthCounter)
    
    #AvgProfLossChange = round((MonthlyChangeSum - (Profit_Change[0])) / (len(Profit_Change)-1),2)
    #print(AvgProfLossChange)

    #print('---------------Test for print/terminal --------------' + '\n') 
    #print(f'Greatest Month was: ' + str(GreatestMonth) + ' and the Greatest Month total was: $' + str(GreatestInc) + '')
    #print(f'Lowest Month was: ' + str(LowestMonth) + ' and the Lowest Month total was: $' + str(GreatestDec) + '')
    #print('--------------------------------------' + '\n') 
    #raise SystemExit  -  To end code to test results previous to this line

    print(f"-------- Summary -----------" '\n')

def Summary():                                              # Created def function for uniqueness and creativity for Summart output
    print(f"   Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {MonthCounter} ")
    print(f"Total: ${TotalAmount} ")   
    print(f"Average Change: ${AvgProfLossChange} ")
    print(f"Greatest Increase in Profits: {GreatestMonth} (${GreatestInc}) ")
    print(f"Greatest Decrease in Profits: {LowestMonth} (${GreatestDec}) ")
    print(f"----------------------------" '\n')
    

    with open(SummaryWriteUp, 'w') as textfile:             # Initialization for 'write' feature to export data to .txt file                   
        textfile.write(f"   Financial Analysis" '\n')
        textfile.write(f"----------------------------" '\n')
        textfile.write(f"Total Months: {MonthCounter} " '\n')
        textfile.write(f"Total: ${TotalAmount} " '\n')   
        textfile.write(f"Average Change: ${AvgProfLossChange} " '\n')
        textfile.write(f"Greatest Increase in Profits: {GreatestMonth} (${GreatestInc}) " '\n')
        textfile.write(f"Greatest Decrease in Profits: {LowestMonth} (${GreatestDec}) " '\n')
        textfile.write(f"----------------------------" '\n')

    return                                                  # Closes def function to be used with the " Summary() " code line
    
     
Summary()                                                   # Call def function to begin print/write of Summary results


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

 