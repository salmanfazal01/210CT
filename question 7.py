#parameters => 2 as dividing factor and number
def question7(factor, number):

    boolean = False #is it a prime?
    
    if(number <= 2):
        boolean = True #If mumber is less than 2, its a prime.
    
    elif(factor >= number):
        #If the dividing factor > number, its a prime
        #(as number has been divided by all lower factors)
        boolean = True
    
    else:
        if(number % factor == 0):
            boolean = False #If number is divisible by factor, its not a prime.
        else:
            return question7(factor+1, number) #If not, then increment factor.
    print(boolean)

question7(2, 31)

'''
Pseudocode:

PRIME(FACTOR, NUMBER)

    if NUMBER <= 2
        return TRUE
    else if FACTOR >= NUMBER
        return TRUE
    else
        if NUMBER mod FACTOR = 0
            return FALSE
        else
            return PRIME(FACTOR+1, NUMBER)
'''