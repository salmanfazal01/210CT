def question3(num):
    
    if(num % num**0.5 == 0): #If number divided by its square root has no decimal:
        print("This number is a perfect square")
    else:
        #If not, convert its square root to a whole number then square it
        print("The lowest perfect square is:", int(num**0.5)**2)


question3(int(input("Enter number to calculate highest perfect square: ")))

'''
Pseudocode:

PERFECT-SQUARE(A)
    if A mod SQRT(A) = 0
        return FALSE
    else
        return SQUARE ( INT(SQRT(A)) )

'''

