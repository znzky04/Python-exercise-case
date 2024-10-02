#Case 4 :Handle a string

#1.Definition
my_str = "mygo is Bangdream It's Mygo"

#2.Count char
num = my_str.count("my")
print(f"There are {num} my characters in {my_str} string.")

#3.Replace all Spaces with |
new_my_str = my_str.replace(" ","|")
print(f"The string {my_str} has became: {new_my_str}")

#4.Split the string according to "|" to get the new list
my_str_list = new_my_str.split("|")
print(f"The string {new_my_str} splited result is {my_str_list} ")