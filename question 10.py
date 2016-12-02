def question10(myList):
    all_sequences = [] #empty list (2 dimension list)

    temp = [] #a sub-sequence

    for x,y in enumerate(myList): #index, value
        
        if(x == 0):
            temp.append(y) #append first value to temp
       
        else:            
            if(myList[x] > myList[x-1]): #if x is greater than previous one:               
                temp.append(y) #append list value to temp
                
            else: #if value of x is not greater than previous one:
                all_sequences.append(temp[:]) #append entire temp list to all_sequences
                temp[:] = [] #clear the temp list
                temp.append(y) #append the new lowest value to temp

    all_sequences.append(temp)           
    print(max(all_sequences, key=len))


question10([1,2,3,0,2,3,5,6,7,1,4,5,6,9])