import os
import csv

with open ('budget_data.csv') as bankdata:
    csv_f = csv.reader(bankdata)
#-----------------------------------------------------------------

    totmonths = 1
    totalrev = 0 # Counter for total rev
    change = 0 #Holds monthly change amount
    increase = 0 #Starting counter for increase amount
    decrease = 0 #Starting counter for decrease amount

    eachchnge = [] #List to hold each of the monthly changes

    next(csv_f)
    firstrow = next(csv_f) #Set first row
    janrev = int(firstrow[1]) #Get January revenue
    change = janrev # Starting revenue

    #change = janrev

    for row in csv_f:
        #Calculate Total Months
        totmonths += 1  

        #Net total profit/Losses
        totalrev = int(row[1]) + totalrev

        #Calculate profit/loss average
        # First calculate the change from month to month and add it to a list
        monthprofit = int(row[1])
        change = monthprofit - change
        eachchnge.append(change)

        #Get increase month
        if change > increase:
            increase = change
            increasemonth = row[0]

        #Get decrease month
        if change < decrease:
            decrease = change
            decreasemonth = row[0]

        change = int(row[1])
    
#Divide the list by the total number of months to get average
avgprofit = round(sum(eachchnge)/len(eachchnge),2)

print("-" * 25)
print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {totmonths}') 
print(f'Total: ${totalrev}')
print(f'Average Change: ${avgprofit}')
print(f'Greatest Increase in Profits: {increasemonth} (${increase})')
print(f'Greatest Decrease in Profits: {decreasemonth}(${decrease})')

#Write to a txt file
bank_txt=("PyBankAna.txt")

with open (bank_txt, 'w') as txtfile:
    txtfile.write("-" * 25)
    txtfile.write("Financial Analysis \n")
    txtfile.write("-" * 25) 
    txtfile.write(f'Total Months: {totmonths} \n') 
    txtfile.write(f'Total: {totalrev} \n')
    txtfile.write(f'Average Change: {avgprofit} \n')
    txtfile.write(f'Greatest Increase in Profits: ({increase}) \n')
    txtfile.write(f'Greatest Decrease in Profits: ({decrease}) \n') 