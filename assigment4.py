"""Python Easy Online class,
Homework #4: if statement"""

"""myUniqueList = []
myLeftOvers = []

Adding to items myUniqueList and checking existing values
def addList (students):
    if students not in myUniqueList:
        print(True)
        myUniqueList.append(students)
        print(myUniqueList)
    else:
        print(False)
        myLeftOvers.append(students)
        print(myLeftOvers)

    



addList("Joe")
addList("Joe")
addList("Sunday")
addList("Joe")
addList("Victor")
addList("Sam")
addList("Gilbert")
addList("Helen")
addList("Gilbert")
addList("Chuks")
addList("Joe")
addList("Han")
addList("Sam")
addList("Godin")
addList(4)
addList(4)

newStudents = []

for w in myLeftOvers:
    print(w)
    if w == "Joe":
        print("Joe is among the loftovers")
    newStudents.append(w)

print(newStudents)"""

letters = [1,2,3,4,5,6,7,8,9,0]
oddNumbers = []

evenNumbers = []

for p in letters:
    if p%2 == 1:
        print("This is an odd number")
        oddNumbers.append(p)
    if p%2 == 0:
        print("The number is an even number")
        evenNumbers.append(p)

print(oddNumbers)
print(evenNumbers)

for p in range(20):
    print(p)
    if p%2 == 1:
        print("odd")
        oddNumbers.append(p)
    else:
        print("even")
        evenNumbers.append(p)
print(oddNumbers)
print(evenNumbers)