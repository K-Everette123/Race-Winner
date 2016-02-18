'''
    Name: Race winner
    Author: Kyle Everette
    Last modified: 2/17/16

    Program that finds the person with the longest distance run in a text file and creates a new one to
    output the winner.
'''

def our_max(stuff):         #Function to find largest number in list
    largest = stuff[0]

    for item in stuff:
        if item > largest:      
            largest = item
    return largest        
    
    
def convert(miles):         #Function to convert miles to km 
    return miles/0.62137
        

file = open("distances.txt", "r")       #Opens original text file

for runner in file:             #Turns file into a list
    temp = runner.split()
    ru_holder = []
    ru_holder.append(temp[0])
    ru_holder.append(temp[1])
    for x in temp[2:3]:             #Turn string to float
        ru_holder.append(float(x))
    ru_holder.append(temp[3])          
    if temp[3] == "mi":                 #Uses convert function to convert distances in miles to km
        miles = ru_holder[2]
        ru_holder.remove(ru_holder[2])
        ru_holder.insert(2, convert(miles))
        ru_holder.remove(ru_holder[3])
        ru_holder.insert(3, "km")
    file.close
    
    winner = open("winner.txt", "w")        #Create new file
    ru_final = str(ru_holder[2])
                              
    winner.write("The winner is " + ru_holder[0] + " " +\
                 ru_holder[1] + " with a distance of " +\
                 our_max(ru_final) + " km!")


    
    winner.close() 
