#Case 1: Getting paid

import random

money = 64800

for i in range(1,25):
    score = random.randint(1,10)

    if score< 5:
        print(f"employee {i} Performance score is {score}, not up to standard, no payment, next.")

        continue

    #Determine if the balance is enough
    if money >= 4000:
        money -= 4000
        print(f"employee {i}, Performance score is enough, salary:4000 yuan, Corporate balance:{money} ")
    else:
        print(f"Balance is not enough, Current balance:{money} yuan, Send it in next month.")
        break


