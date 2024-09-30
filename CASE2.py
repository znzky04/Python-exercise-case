#Case 2:Mini ATM

#Define global variables
money = 4000000
name = None

name = input("Please enter your name:")

def query(show_header):
    if show_header:
        print("---------Check balance---------")
    print(f"{name}, Your balance remains: {money} yuan.")

def saving(num):
    global money
    money += num
    print("----------Savings----------")
    print(f"{name},You have successfully deposited {num} yuan.")

    query(False)

def get_money(num):
    global money
    money -= num
    print("----------Withdraw----------")
    print(f"{name},You have successfully withdrew money {num} yuan.")

    query(False)

def main():
    print("----------Main Menu-----------")
    print(f"{name},Hi,Welcome to the bank ATM. Please select operation:")
    print("Check Balance\t[press 1]")
    print("Saving Money \t[press 2]")
    print("Get Money   \t[press 3]")
    print("Exit        \t[press 4]")
    return input("Please enter your selection:")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("How much money do you want to save? Please enter:"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("How much money do you want to withdraw? Please enter:"))
        get_money(num)
        continue
    else:
        print("The program exited!")
        break


