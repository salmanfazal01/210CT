myList = [1,4,5,6,9,10,12,14,16,19,20,22,23,24,29,30] #Create a list
low = int(input("Enter low interval: "))
high = int(input("Enter high interval: "))

def binary(myList):          
    
    mid = int(len(myList)//2) #mid point of of the list

    if(len(myList) == 0):   # Base condition: list will keep slicing.
        print("\nNumber not found!") # If list is empty, number not found
        return False            
    
    else:    
            if (low < myList[mid] < high): #if mid between intervals
                print("number found")
                return True

            elif (myList[mid] > high): #return start to mid
                return binary(myList[:mid])
            else:
                return binary(myList[mid+1:]) #return mid to end

binary(myList)