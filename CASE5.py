#Case 5: Handle a list to a collection
#1.Definition
my_list = ['Poppin\'Party', 'Roselia', 'Afterglow', 'Hello Happy World',
           'Pastel Palettes', 'RAISE A SUILEN', 'Morfonica', 'Mygo', 'Avemujica']

#2.Define one empty collection
my_set = set()

#3.Use for loop
for element in my_list:
    my_set.add(element)

print(f"the list is {my_list}")
print(f"After use for loop, we get a new set:{my_set}")

'''
#使用python内置的set()函数：
#举例：
myList=[1,2,3,3,3,2,2,1,5,6,7,8,5,9,0] 
#注意：列表是用中括号括起来的
mySet=set(myList)
print(mySet)

#使用python内置的list()函数：
#举例：
mySet={2,3,6,1,2,3,4,5}
#注意：集合是用大括号括起来的
myList=list(mySet)
print(myList)

'''
