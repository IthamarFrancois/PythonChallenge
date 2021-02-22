import os       # First we'll import the os module which will allow us to create file paths across operating systems
import csv      # And csv module for reading CSV files
bankpath_csv = os.path.join('Resources', 'budget_data.csv')

#Testing of Write File Dest
# Specify the file to write to
output_csv = os.path.join("Analysis", "Test.csv")

# save the output file path
#output_file = os.path.join("output.csv")

#ALWAYS MAKE SURE TO DO THE ABOVE FOR READ/WRITE
# import os
# import csv
# x (x_csv) = os.path.join("..", "Folder where file is located", "FileToBeRead.csv")

# ------------------------------------------------------------------------------------------------------

Months = []
TotalMo = []
Amounts = []
TotalAmt = []
ChangeAvg = []
GreatestIncr = []
GreatestDecr = []

# Open and read csv
with open(bankpath_csv, newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

        # Read through each row of data after the header
    for row in csv_reader:
        Months = row[0].split('-')

        
        
        #Months.append(row.split("-"))
        print(Months)
        #TotalAmt.append(row[1])
        
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
with open(output_csv, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(["Testing", "Ithamar", "Francois"])
    
    
    
    # Initialize csv.writer
#    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
#   csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
#    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
