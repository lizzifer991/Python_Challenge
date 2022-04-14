#Import os & csv
import os
import csv
#Set up path
PyBankcsv = os.path.join("Resources", "budget_data.csv")
#Lists
date = []
profit = []
changes = []
#Variables needed
count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0 
#Open Csv path
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
 #Calculating Total months       
        count = count + 1
        date.append(row[0])
#Calculating the Total Profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
#Calculating the Average monthly change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        changes.append(monthly_change_profits)
        total_change_profit = total_change_profit + monthly_change_profits
        initial_profit = final_profit
#Calculate the Average change in profits
        average_change_profits = (total_change_profit/count)
#Find Max Change/date and Min Change/date for profits 
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        increase_date = date[changes.index(greatest_increase)]
        decrease_date = date[changes.index(greatest_decrease)]
#Print results with Title "Financial Analysis"
    print("-----------------------------------------------------------")
    print("Finacial Analysis")
    print("-----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase)+ ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease)+ ")")
    print("-----------------------------------------------------------")
#Create Text File for results
with open('Financial_Analysis.txt', 'w') as text:
    text.write("-----------------------------------------------------------\n")
    text.write("Finacial Analysis"+ "\n")
    text.write("-----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("Average Change: " + "$" + str(int(average_change_profits))+ "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")
    text.write("-----------------------------------------------------------\n")