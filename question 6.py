#input a sentence array, iterate backwards and add words to new array
def question6(userInput):
    temp = []
    
    for i in range(1, len(userInput)+1):
        temp.append(userInput[-i])

    print(" ". join(temp)) #print list as a string

    print("""
================
Run time = 2n+3
BigO = O(n)
================
""")


question6(input("Enter a sentence: ").split(" "))

'''
Pseudocode:

REVERSE()
    input <- [] #list of sentence
    temp <- []
    for i <- 1 to length[input]
        temp.APPEND(input[-i])
    return temp
'''
