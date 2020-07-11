

import os
import csv

filepath = os.path.join("Resources/election_data.csv")
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    
    #List of Candidates
    CanList = [row[2] for row in csvreader]
    
    #Length = all votes totaled.     
    TotalVotes = len(CanList)
    
    #Tally Counter (simplify)
    ListOfCans = dict((x,CanList.count(x)) for x in set(CanList))
    
    #Winner Winner, Chicken Dinner
    Winner = max(ListOfCans, key=ListOfCans.get)
    
    #Sorting tool for later
    Sort = sorted(ListOfCans.items(), key=lambda x:x[1], reverse=True)
    #Print to Terminal
    print("Election Results")
    print("\n---------------")
    print("\nTotal Votes: " + str(TotalVotes))
    print("\n---------------")
    #Print candidates sorted by highest values
    [print(f"{key}: {value/TotalVotes:.2%} ({value})") for key, value in Sort]
    print("\n---------------")
    print("\nWinner: " + Winner)
    print("\n---------------")

#Write it all to a .txt in folder titled "Analysis"
Output = "Analysis/Analysis.txt"
os.makedirs(os.path.dirname(Output), exist_ok=True)
A = open(Output, "w")
A.write("Election Results")
A.write("\n---------------")
A.write("\nTotal Votes: " + str(TotalVotes))
A.write("\n---------------\n")
[A.write(f"{key}: {value/TotalVotes:.2%} ({value})\n")for key, value in Sort]          
A.write("\n---------------")
A.write("\nWinner: " + Winner)
A.write("\n---------------") 
A.close()

#Am I supposed to close the csv file I'm reading? LOL
