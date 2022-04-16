#Import os & csv
import os
import csv
#Set up path
PyPollcsv = os.path.join('..', 'Resources', 'election_data.csv')
#Lists & Varibles
Candidates = []
Individual_Candidates = []
Votes = []
Percent_Votes = []
Total_Votes = 0
#Open Csv path
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
#Calculating Total Votes       
        Total_Votes = Total_Votes + 1
        Candidates.append(row[2])
#Calculating the total votes & percenatage of votes per candidate
    for i in set (Candidates):
        Individual_Candidates.append(i)
#Calculating the total votes per candidate
        x = Candidates.count(i)
        Votes.append(x)
#Calculating the percentage of votes per candidate
        y = (x/Total_Votes)*100
        Percent_Votes.append(y)
#Identify the winner based on votes
    Popular_Vote = max(Votes)
    Winner = Individual_Candidates[Votes.index(Popular_Vote)]
#Print results with Title "Election Results"
    print("-----------------------------------------------------------")
    print("Election Results")
    print("-----------------------------------------------------------")
    print("Total Votes: " + str(Total_Votes))
    print("-----------------------------------------------------------")
    for i in range(len(Individual_Candidates)):
        print(Individual_Candidates[i] + ":" + str(Percent_Votes[i]) + "% (" + str(Votes[i])+ ")")
    print("-----------------------------------------------------------")
    print("And the winner is:" + Winner)
    print("-----------------------------------------------------------")
#Create Text File for results
with open('Election_Results.txt', 'w') as text:
    text.write("-----------------------------------------------------------\n")
    text.write("Election Results"+ "\n")
    text.write("-----------------------------------------------------------\n\n")
    text.write("Total Votes: " + str(Total_Votes) + "\n")
    text.write("-----------------------------------------------------------\n\n")
    for i in range(len(set(Individual_Candidates))):
        text.write(Individual_Candidates[i] + ":" + str(Percent_Votes[i]) + "% (" + str(Votes[i]) + ")\n")
    text.write("-----------------------------------------------------------\n")
    text.write("And the winner is: " + Winner + "\n")
    text.write("-----------------------------------------------------------\n")