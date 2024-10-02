#Process a list in a variety of ways，list:[21,25,21,23,22,20]

#1.Definition list
mylist = [21,25,21,23,22,20]

#2.Add one number
mylist.append(31)

#3.Add one list
mylist.extend([29,33,30])

#4.Take out the first number
num1 = mylist[0]
print(f"Successfully Take out {num1}.")

#5.Take out the last number
num2 = mylist[-1]
print(f"Successfully Take out {num2}.")

#6.Find the number 31
index = mylist.index(31)
print(f"The element 31 in the list of subscripts is {index}")

print(f"The whole list is {mylist}")