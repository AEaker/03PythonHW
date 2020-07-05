import os
import csv


filepath = os.path.join("Resources","budget_data.csv")
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    MonthCount = 0
    NetTotal = 0
    #previousrow
    previous = 0
    MaxInc = 0
    MaxDec = 0
    AvgList = []
    #first row variable
    i = 1

    for row in csvreader:
        #Month Total
        MonthCount = MonthCount + 1
        #Total Profit
        NetTotal = NetTotal + int(row[1])

        #Monthly Change
        x = int(row[1])
        Temp = x - previous
        AvgList.append(Temp)
        

        #Find Greatest increase
        if Temp > MaxInc: 
                MaxInc = Temp
                MaxIncMonth = row[0]
        #Find Greatest Decrease 
        if Temp < MaxDec: 
                MaxDec = Temp
                MaxDecMonth = row[0]
        
        #Get first row to remove from list
        if i == 1:
            firstrow = int(row[1])
        i = 0 
        #Reset previous row
        previous = int(row[1])

#Average Change 
AvgList.remove(firstrow)
Avg = sum(AvgList)/(MonthCount - 1)

#Print to terminal
print(csv_header)
print("Total Months:" + str(MonthCount))    
print("Total: $" + str(NetTotal))
print("Average Change: $" + str(round(Avg,2)))
print("Greatest Increase in Profits: " + MaxIncMonth + " ($" + str(MaxInc) + ")")
print("Greatest Decrease in Profits: " + MaxDecMonth + " ($" + str(MaxDec) + ")")

#Print to text file
Output = os.path.join("Analysis", "Analysis.txt")
Analysis = open(Output,"w")
Analysis.write("Financial Analysis\n ---------------------------")
Analysis.write("\nTotal Months:" + str(MonthCount))
Analysis.write("\nTotal: $" + str(NetTotal))
Analysis.write("\nAverage Change: $" + str(round(Avg,2)))
Analysis.write("\nGreatest Increase in Profits: " + MaxIncMonth + " ($" + str(MaxInc) + ")")
Analysis.write("\nGreatest Decrease in Profits: " + MaxDecMonth + " ($" + str(MaxDec) + ")")
Analysis.close()

