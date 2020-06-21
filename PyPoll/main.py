import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
csvoutput = os.path.join("Analysis", "election_data_output.txt")    

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') #CSV reader is a reference to the csv file and specifies delimiter and variable that holds contents 

    header = next(csvreader) #skip first line

    voter_list = [] #list to store voter IDs
    
    candidate_dict = {} #dictionary to store candidates and their vote counts
   
    for row in csvreader: #for loop to cycle through each row
        voter_list.append(int(row[0])) #adds voters to the voter list ID, can use this to determine total number of votes cast

        if row[2] not in candidate_dict: #cycle through rows and add unique candidates found to the candidate dict and initiate value as 0
            candidate_dict.update({row[2]:0})

        if row[2] in candidate_dict.keys(): #if the candidate in row[2] is found in the dictionary: add one to their value in the dictionary.
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1
    
    total_votes = len(voter_list) #stores total votes as the length of the voter list (gives us total votes number)
       
    winner = max(candidate_dict, key=candidate_dict.get) #get the key with the max value

    #------------print election results--------------#
    print("Election Results")
    print("--------------------------")
    print(f'Total Votes: {total_votes}') 
    print("--------------------------")
    for candidate in candidate_dict: #cycles through each candidate in the candidate dictionary
        candidate_perc = candidate_dict[candidate]/total_votes *100 #calculates the percentage votes for each candidate in the dictionary
        print(f'{candidate} {candidate_perc:.3f}% ({candidate_dict[candidate]})') #prints results for each candidate in the candidate dictionary
    print("--------------------------")
    print(f'Winner: {winner}')


    #-------print outpute to file---------#
with open(csvoutput, "w") as csvwriter:

    csvwriter.write("Election Results\n")
    csvwriter.write("--------------------------\n")
    csvwriter.write(f'Total Votes: {total_votes}\n') 
    csvwriter.write("--------------------------\n")
    for candidate in candidate_dict: #cycles through each candidate in the candidate dictionary
        candidate_perc = candidate_dict[candidate]/total_votes *100 #calculates the percentage votes for each candidate in the dictionary
        csvwriter.write(f'{candidate} {candidate_perc:.3f}% ({candidate_dict[candidate]})\n') #prints results for each candidate in the candidate dictionary
    csvwriter.write("--------------------------\n")
    csvwriter.write(f'Winner: {winner}')






