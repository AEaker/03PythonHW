filepath = os.path.join("..","Resources","budget_data.csv")

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)