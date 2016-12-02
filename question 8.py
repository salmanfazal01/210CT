def question8(userInput):
    
    if (userInput == ""): # empty string
        return userInput
    elif (userInput[0] in "aeiouAEIOU"): #Check if first char is a vowel
        return question8(userInput[1:]) #If yes, return string from second char
    else:        
        return ( userInput[0] + question8(userInput[1:]) ) 
        #If no, store first char & return new string from second char


#print(question8(input("Enter string: ")))
print(question8("salman is awesome"))

'''
Pseudocode:

REMOVE-VOWELS(A)
    if A = NIL
        return A
    else if A[0] in "aeiouAEIOU"
        return REMOVE-VOWELS(A[1:])
    else
        return A[0] + REMOVE-VOWELS(A[1:])

'''
