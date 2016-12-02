def add(b,c):

    total = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
    
    # loop through rows
    for row in range(len(b)):
       # loop through columns
       for column in range(len(c)):
           total[row][column] = b[row][column] + c[row][column]

    return total


def subtract(b,c):

    total = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
    
    # loop through rows
    for row in range(len(b)):
       # loop through columns
       for column in range(len(c)):
           total[row][column] = b[row][column] - c[row][column]

    return total


def multiply(b,c):

    total = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

    # loop through rows of b
    for rowb in range(len(b)):
       # loop through columns of c
       for columnc in range(len(c)):
           # loop through values/rows of c
           for rowc in range(len(c)):
            temp = b[rowb][rowc] * c[rowc][columnc]
            total[rowb][columnc] = total[rowb][columnc] + temp

    return total


def scalar(num, matrix): #multiply matrix with a number

    total = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

    #loop througb rows
    for row in range(len(matrix)):
        #loop through columns
        for column in range(len(matrix)):
            #multiply every element with scalar number
            total[row][column] = num*matrix[row][column]

    return total



b = [[1,3,7],[5,9,-1],[9,0,3]]
c = [[1,-3,0],[7,0,-4],[2,2,5]]

a= subtract(multiply(b,c), scalar(2,(add(b,c))))
for i in range(len(a)):
  print(a[i])


'''
Pseudocode: (square matrix)

ADDITION(A,B)
  total <- [[],[],[]]
  for row <- 0 to length(A)
    for column <- 0 to length(B)
      total[row][column] <- A[row][column] + B[row][column]
  return total


  SUBTRACTION(A,B)
  total <- [[],[],[]]
  for row <- 0 to length(A)
    for column <- 0 to length(B)
      total[row][column] <- A[row][column] - B[row][column]
  return total


  MULTIPLICATION(A,B)
  total <- [[],[],[]]
  for row <- 0 to length(A)
    for column <- 0 to length(B)
      for row2 <- 0 to length(B)
        temp <- A[row][row2] * B[row][column]
        total[row][column] <- total[row][column] + temp
  return total

'''