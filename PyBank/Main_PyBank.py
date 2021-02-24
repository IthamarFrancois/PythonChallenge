import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files
bankpath_csv = os.path.join('Resources', 'budget_data.csv')

# Testing of Write File Dest
# Specify the file to write to
output_csv = os.path.join("Analysis", "Test.csv")

# ------------------------------------------------------------------------------------------------------

# Open and read csv
with open(bankpath_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
        # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")
    

    # Definitions of variables: --------------------------------------------------------------------------------------
    MonthCounter = 0                 # The total number of months included in the dataset
    TotalAmount = 0                  # The net total amount of "Profit/Losses" over the entire period
    

    ProfitThisMonth = 0              # Tracker for the profit gain/loss this particular month
    PreviousMonthProfit = 0          # Reset start amount for profit values to calculate next "Profit/Losses"
    
    MonthlyChange = 0
    ProfLossRange = 0
    AvgProfLossChange = 0
    
    GreatestInc = 0
    GreatestMonth = 0
    GreatestDec = 0
    LowestMonth = 0

    Date_Range = []                  # Reading row[0] data
    Profit_Loss_Amounts = []         # Reading row[1] data
    Profit_Change = []               # To calc the average
    Greatest_Increase = []           # The greatest increase in profits (date and amount) over the entire period  
    Greatest_Decrease = []           # The greatest decrease in losses (date and amount) over the entire period

    Date_Data = []
    Profit_Data = []
    


    #raise SystemExit
# Code start: --------------------------------------------------------------------------------------
    i=0
    j=0
    for row in csv_reader:
        Date_Range.append(row[0])
        Profit_Loss_Amounts.append(row[1])
        
        
        Date_Data.append(row[0])
        Profit_Data.append(row[1])
        #RowData = zip(Row_Data,Profit_Loss_Amounts)

        
        #Profit_Change.append(row[0])
        ProfitThisMonth = int(row[1])
        MonthlyChange = (ProfitThisMonth - PreviousMonthProfit)
        Profit_Change.append(MonthlyChange)
        
        PreviousMonthProfit = ProfitThisMonth

        
        MonthCounter += 1
        TotalAmount = int(row[1]) + TotalAmount
        
    
    j = 0
    ProfLossRange = 0
    for i in range(len(Profit_Change)):
        ProfLossRange = ProfLossRange + Profit_Change[i]
        if (Profit_Change[i] > 0) and (Profit_Change[i] > GreatestInc):
            GreatestInc = Profit_Change[i]
            GreatestMonth = Date_Data[i]
        if (Profit_Change[i] < 0) and (Profit_Change[i] < GreatestDec):
            GreatestDec = Profit_Change[i]
            LowestMonth = Date_Data[i]
        print(Profit_Change[i])

    AvgProfLossChange = ProfLossRange / len(Profit_Change)

    print('--------------------------------------' + '\n') 
    print(i)
    print(MonthCounter)
    print(AvgProfLossChange)
    print(f'Greatest Month was: ' + str(GreatestMonth) + ' and the Greatest Month total was: $' + str(GreatestInc) + '')
    print(f'Lowest Month was: ' + str(LowestMonth) + ' and the Lowest Month total was: $' + str(GreatestDec) + '')
        
        
        #if  ProfLossRange == 0:
            #ProfLossRange = int(list(row[1]))
            #print(ProfLossRange)
            #print("Success")
        #else:
            #print("Fail")
            #break
        
            #j += 1

            #i = int(i + 1)
            #if row[1] == "310503":
                #print("Success")
            #break
            #print(row) 

    print('--------------------------------------2' + '\n') 
    #print(Date_Data[j]) 
    #print(Profit_Data[i])
    
      
    raise SystemExit  
        
        #test = row[1]
        #if RowDataTest == Row_Data:
            #print("Success")
            #j = i
        #else:
            #print("Failed")

    
    #print('--------------------------------------2' + '\n')    
    #print(j)
    #print(i)

    #for amt in Profit_Loss_Amounts:
        #Total_Amount = (int(amt) + Total_Amount)
        
        #print(amt)
        #print(Total_Amount)
    
    #for chg in Profit_Change:
        #print(chg)

#print(f'Total Months: ' + str(Total_Month_Counter) + ' Profit Amount total is: $' + str(Total_Amount) + '')



#Month_Count = (len(DateRange))    # = 86

# We can also add conditional logic (if statements) to a list comprehension
#NORMAL WAY





#july_temperatures = [87, 85, 92, 79, 106]
#hot_days = []
#for temperature in july_temperatures:
#    if temperature > 90:
#        hot_days.append(temperature)

#print(hot_days)
#print(hot_days[0])
#print(hot_days[1])

#print('---------------------------------------4' + '\n')


# List Comprehension of above with If conditional built-in
#hot_days = [temperature for temperature in july_temperatures if temperature > 90]
#print(hot_days)


    
   
    #raise SystemExit  

          #Formatting End Summary Goal
#print(f"Financial Analysis")
#print(f"----------------------------")
#print(f"Total Months: XXX")
#print(f"Total: $XXX"
#print(f"Average Change: $XXX")
#print(f"Greatest Increase in Profits: XXX $XXX")
#print(f"Greatest Decrease in Profits: XXX $XXX")



# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_csv, 'w', newline='') as csvfile:
    #   Initialize csv.writer
    #   csv_writer = csv.writer(csvfile, delimiter=',')
    #   csv_writer.writerow(["Testing", "Ithamar", "Francois"])
    #   csv_writer.writerows([])