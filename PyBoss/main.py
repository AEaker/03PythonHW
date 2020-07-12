
import os
import csv

#Get State dictionary
from StateAbb import us_state_abbrev
#Get CSV data
inpath = "Resources/employee_data.csv"
#export to new file
outpath = "Analysis/fixed_employee_data.csv"
#make path for new file
os.makedirs(os.path.dirname(outpath), exist_ok=True)
#read old data
with open(inpath) as infile:
    csvreader = csv.reader(infile)
    csvheader = next(csvreader)
    #write new data
    with open(outpath, 'w',newline="") as outfile:
        out = csv.writer(outfile, delimiter=",")
        #write header
        out.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
        #write rest of lines 
        for row in csvreader:
            out.writerow([row[0], #row[0] = unchanged Employee ID
            row[1].split(" ")[0], row[1].split(" ")[1], #row[1] = Employee Name that is split into First and Last, separated by space
            row[2].split("-")[1] + "/" + row[2].split("-")[2] + "/" + row[2].split("-")[0], #row[2] = Date of Birth format changed
            "****-**-" + row[3].split("-")[2], #Privacy SSN
            us_state_abbrev.get(row[4])]) #get value of key from State Abbreviations dictionary
infile.close()
outfile.close()



