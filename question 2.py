def question2(userInput):
    
    #Calculate factorial
    total = 1
    while userInput >= 1:
        total = total * userInput
        userInput = userInput - 1
    print("\nfactorial:", total)

    #Calculate trailing zeros
    counter = 0
    for i in range(1, len(str(total))):
        if ( str(total)[-i] == '0' ):
            counter += 1 #increase counter if last char is a 0
        else:
            break #if another character found, stop the program
        
    print("\nTrailing 0's are:",counter)


question2(int(input("\nInput number to calculate trailing zeros: ")))