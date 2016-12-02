import random

def question1(userList):
    
    print("\nEntered List: " + str(userList)) #original list

    newList = [] #empty list to append random numbers
    
    for i in range( len(userList) ):
        random_number = random.choice(userList) #select random original list
        newList.append(random_number) #append original value to new list
        userList.remove(random_number) #remove value to avoid duplicates

    print("\nShuffled List: "+str(newList)) #new list
 
#save numbers in a list
question1(input("Insert list of numbers (space seperated): ").split(" "))
