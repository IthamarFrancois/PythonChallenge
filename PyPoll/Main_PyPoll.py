import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files


# Using this py for scrap paper while working on code for Main_PyBank




# ------------------------------------------------------------------------------------------------------

Total_Month_Counter = 0         # The total number of months included in the dataset
Total_Amount = 0                # The net total amount of "Profit/Losses" over the entire period
Profit_Loss = 0                 # To calculate the changes in "Profit/Losses"
Average_Of_Changes = 0          # Average of Profit_Lose changes
#TotalMonths = len(row)

Greatest_Increase = []          # The greatest increase in profits (date and amount) over the entire period  
Greatest_Decrease = []          # The greatest decrease in losses (date and amount) over the entire period

#Define rows (after Split) to hold new lists
Changing_Months = []
Changing_Years = []
Amounts_Values = []


# Open and read csv
with open(bankpath_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    Total_Month_Counter = Total_Month_Counter + 1
    
    
    #row[1] = next(csvfile)
    #Total_Month_Counter = Total_Month_Counter + 1
    #print(row)
    
        # Read through each row of data after the header
    for row in csv_reader:
        Changing_Months.append((row[0].split('-'))
            #Changing_Years.append(row[1])
            #Amounts_Values.append(row[2])
        
            #Total_Amount.append(row[0])
    #   Total_Month_Counter = Total_Month_Counter + 1
        
        
            #Changing_Months.append(row.split("-"))
            #print((Changing_Months), (Total_Amount)) 
        
            print(Changing_Months[0])
            #Total_Amt.append(row[1])
        
        #print(row)


#for i in range(len(candy_list)):
    #print("[" + str(i) + "]" + candy_list[i])









---------------------------------------------------------------------------

# Read each row of data after the header
    for row in csvreader:
        print(row)


        Total_Month_Counter = 0


        # Read through each row of data after the header
    for row in csv_reader:
        #Changing_Months = row[0].split('-')
        Changing_Months.append(row[0])
        Changing_Years.append(row[1])
        #Amounts_Values.append(row[2])
        
        #Total_Amount.append(row[0])
        Total_Month_Counter = Total_Month_Counter + 1
        
        
        #Changing_Months.append(row.split("-"))
        #print((Changing_Months), (Total_Amount)) 
        
        print(Changing_Months)
        #print(Changing_Years[1])
        #Total_Amt.append(row[1])
        
        #print(row)


#for i in range(len(candy_list)):
    #print("[" + str(i) + "]" + candy_list[i])














    #Formatting End Summary Goal
#print(f"Financial Analysis")
#print(f"----------------------------")
#print(f"Total Months: XXX")
#print(f"Total: $XXX"
#print(f"Average Change: $XXX")
#print(f"Greatest Increase in Profits: XXX $XXX")
#print(f"Greatest Decrease in Profits: XXX $XXX")

    
    #Testing of Write File Dest
# Specify the file to write to
#output_csv = os.path.join("Analysis", "Test.csv")
#output_csv.write("Testing - Ithamar Francois")


# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_csv, 'w', newline='') as csvfile:
    # Initialize csv.writer
    #csv_writer = csv.writer(csvfile, delimiter=',')
   # csv_writer.writerow(["Testing", "Ithamar", "Francois"])
    #csv_writer.writerows([])
    
    
    
    # Initialize csv.writer
#    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
#   csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
#    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])






#----------------------------------------------------------------------
      #Define rows to hold new lists
Changing_Months = []
Changing_Years = []
Amounts_Values = []

      
      
        All_Row_Data = row[0].split('-')
        All_Row_Data.append(row[1])
        
        ##Changing_Months = All_Row_Data[0]
        ##Changing_Years = All_Row_Data[1]
        ##Amounts_Values = All_Row_Data[2]
        
        Changing_Months = All_Row_Data[0]
        Changing_Years = All_Row_Data[1]
        Amounts_Values = All_Row_Data[2]
        print(f" {Changing_Months} , {Changing_Years}, {Amounts_Values}")
        
        Total_Month_Counter += 1
        Total_Amount = int(Total_Amount + int(Amounts_Values))
    
print(f'Total Months Counted: ' + str(Total_Month_Counter) + ' and the Profit Amount total is: $' + str(Total_Amount) + '')
    
        

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_csv, 'w', newline='') as csvfile:
    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
    #csvwriter.writerow(['Month', 'Year', 'Profit/Loss'])

    #csvwriter.writerows([Changing_Months, Changing_Years, Amounts_Values])

        #----------------------------------------------------------------------








        #Changing_Months = row[0].split('-')
        #Changing_Months.append(row[0])
        #All_Row_Data = row[0].split('-')
        #All_Row_Data.append(row[1])

        #Changing_Years = row[0].split('-')
        #Changing_Years.append(row[1])
        
        #Amounts_Values = Changing_Years[2]

        #Changing_Months = Changing_Years[0]
        #Amounts_Values = Changing_Years[2]


        #Amounts_Values = row[0].split('-')
        #Amounts_Values.append(row[1])

        #print(All_Row_Data)
        
        #print(Changing_Months[0], Changing_Years[1], Amounts_Values[2])
        #print(f" {Changing_Months} , {Changing_Years}, {Amounts_Values}")
        #print((Changing_Months)
        #print(Changing_Years)
        #print(Amounts_Values)

        #AllData = zip(Changing_Months, Changing_Years, Amounts_Values)
        #print(list(AllData)[0])




        
        #print(Changing_Months)
