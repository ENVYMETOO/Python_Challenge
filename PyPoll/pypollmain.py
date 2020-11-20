import os
import csv

mycsvpath =open('election_data.csv')

pollreader = csv.reader(mycsvpath)
#---------------------------------------------------------

totvotes = 0 #Hold total votes overall

candidates = [] #Holds all the candidates name

candidatesvotes = {} 

khanvotes = 0 #Total votes
khanperc = 0 #percentage of total votes
livotes = 0 #Total votes
liperc = 0
correyvotes = 0 #Total votes
correyperc = 0
otolleyvotes = 0 #Total votes
otolleyperc = 0

next(pollreader)
#print(next(pollreader))
#print(next(pollreader))

for row in pollreader:
    #calculate total votes overall
    totvotes += 1

    #Get unique candidates by changing the list to a dict to remove duplicates and then back to a list
    candidates.append(row[2])
    candidates = list(dict.fromkeys(candidates))
    dict.fromkeys(candidates)
    
    #Get votes for each candidates
    if row[2] == "Khan":
        khanvotes += 1
        khanperc = round((khanvotes/totvotes) * 100,2)
        
    elif row[2] == "Li":
        livotes += 1
        liperc = round((livotes/totvotes) * 100,2)
    elif row[2] == "Correy":
        correyvotes +=1
        correyperc = round((correyvotes/totvotes) * 100,2)
    else:
        otolleyvotes += 1
        otolleyperc = round((otolleyvotes/totvotes) * 100,2)

candidatesvotes = {"Khan":khanvotes, "Correy": correyvotes,"Li": livotes,  "O'Tooley": otolleyvotes}
winnervotes = 0

for candidate in candidates:
    votes = candidatesvotes.get(candidate)
    if votes > winnervotes:
        winnervotes = votes
        winner = candidate

print('-' * 25 )
print('Election Results')
print('-' * 25 )
print(f'Total Votes: {totvotes}')
print('-' * 25 )
print(f'Khan: {khanperc}% ({khanvotes})')
print(f'Correy: {correyperc}% ({correyvotes})')
print(f'Li: {liperc}% ({livotes})')
print(f'otolley: {otolleyperc}% ({otolleyvotes})')
print('-' * 25 )
print(f'Winner: {winner}')
print('-' * 25 )

poll_txt=("PyPollAna.txt")

with open (poll_txt, 'w') as txtfile:
    txtfile.write("-" * 25) 
    txtfile.write('Election Results \n')
    txtfile.write("-" * 25)
    txtfile.write(f'Total Votes: {totvotes} \n')
    txtfile.write('-' * 25 )
    txtfile.write(f'Khan: {khanperc}% ({khanvotes}) \n')
    txtfile.write(f'Correy: {correyperc}% ({correyvotes}) \n')
    txtfile.write(f'Li: {liperc}% ({livotes}) \n')
    txtfile.write(f'otolley: {otolleyperc}% ({otolleyvotes}) \n')
    txtfile.write('-' * 25)
    txtfile.write(f'Winner: {winner} \n')
    txtfile.write('-' * 25 )
