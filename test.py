import os
import csv

csvpath = os.path.join('Py_Bank_Budget_Data.csv') #specify the file to read
output_path = os.path.join('Py_Bank_Summary')

with open(csvpath, 'r') as csvfile:

    # CSV reader is a reference to the csv file and specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    #skip first line
    header = next(csvreader)

    PL_list = [] #a list to store the profit and lost column items
    PL_change = [] #a list to store the change amounts between P&L rows
    num_rows = 0
    
    for row in csvreader: #for loop to cycle through each row
        num_rows = num_rows + 1 #to sum rows which equal the months
        PL_list.append(int(row[1])) #adding each line in profit & loss column to a list

    for item in range(len(PL_list)-1): #run a loop to go through items in the PL_list. subtracting one so stays in range
        change_amount = int(PL_list[item +1] - int(PL_list[item])) #calculate each change in rows
        PL_change.append(change_amount) #add change amounts to another list called PL_change
    

    #print summary analysis to "Py-Bank_Summary.txt"
    #with open(output_path, 'w') as csvfile:

    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(num_rows))
    print("Total: " + str(sum(PL_list)))
    print("Average Change: " + str((sum(PL_change))/(num_rows-1)))   #calculates and prints the average change
    print("Greatest Incease in Profits: " + str(max(PL_change)))
    print("Greatest Decrease in Profits: " + str(min(PL_change)))