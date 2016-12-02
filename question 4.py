def question4():
    
    print("""
========================================
QUESTION 1

import random                        (1)
userList = input("Enter List: ")     (1)
newList = []                         (1)
for i in range(len(userList)):       (n)
    index = random.choice(userList)  (n)
    newList.append(index)            (n)
    userList.remove(index)           (n)

------------------
Run time = 4n + 3
BigO = O(n)
========================================

QUESTION 2

input = int(input())                 (1)
counter = 0                          (1)
num = 1                              (1)

while input >= 1:                    (n)
    num = num * input                (n)
    input = input - 1                (n)

for i in range(1, len(str(num))):    (n)
    if ( str(num)[-i] == '0' ):      (n)
        counter+=1                   (n?)
    else:                            (1)
        break                        (1)
    
print(counter)                       (1)

--------------------
Run time = 6n + 6
BigO = O(n)
========================================
""")


question4()
