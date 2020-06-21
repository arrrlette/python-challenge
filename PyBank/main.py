import os
import csv

csvpath = os.path.join('Resources','Py_Bank_Budget_Data.csv')
csvoutput = os.path.join('Analysis', 'Py_Bank_Budget_Data_Output.txt')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # CSV reader is a reference to the csv file and specifies delimiter and variable that holds contents
 
    header = next(csvreader) #skip first line

    PL_list = [] #a list to store the profit and lost column items
    PL_change = [] #a list to store the change amounts between P&L rows
    month = [] # a list to store the months
    num_rows = 0 #a vairable that keeps track of number of rows (which equals number of months, not inlcuding header)
    
    
    for row in csvreader: #for loop to cycle through each row
        num_rows = num_rows + 1 #to sum rows which equal the months
        month.append(str(row[0]))
        PL_list.append(int(row[1])) #adding each line in profit & loss column to a list

    for item in range(len(PL_list)-1): #run a loop to go through items in the PL_list. subtracting one so stays in range
        change_amount = int(PL_list[item +1] - int(PL_list[item])) #calculate each change in rows
        PL_change.append(change_amount) #add change amounts to another list called PL_change
    
    average_change = round(sum(PL_change)/(num_rows-1),2) #calculates the average change
    greatest_increase = max(PL_change) #calculates the greatest change in profit/loss
    greatest_decrease = min(PL_change) #calculates the greatest decrease in profit/loss

    #------------pull month value for greatest increase/decrease in profit---------------
    greatest_increase_index = PL_change.index(greatest_increase)+1 #pull index for month where greatest change occurred plus 1 to account for skipped header and first line
    #print(greatest_increase_index) #print index of greatest increase for testing
    greatest_increase_month = month[greatest_increase_index] #pull month associated with greatest increase index
    #print(greatest_increase_month) #prints the month associated with greatest increase index for testing

    greatest_decrease_index = PL_change.index(greatest_decrease)+1
    greatest_decrease_month = month[greatest_decrease_index]
    

    #-------print financial analysis to terminal----------#
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {num_rows}")
    print(f"Total: ${sum(PL_list)}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Incease in Profits: {greatest_increase_month} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")

    #-------print outpute to file---------#
    with open(csvoutput, "w") as csvwriter:

        csvwriter.write("Financial Analysis\n")
        csvwriter.write("-------------------------------\n")
        csvwriter.write(f"Total Months: {num_rows}\n")
        csvwriter.write(f"Total: ${sum(PL_list)}\n")
        csvwriter.write(f"Average Change: ${average_change}\n") 
        csvwriter.write(f"Greatest Incease in Profits: {greatest_increase_month} ${greatest_increase}\n")
        csvwriter.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}\n")
