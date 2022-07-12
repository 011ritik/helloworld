
import random

max_value = 6
min_value = 1



choice = str(input("Enter \'yes\' or \'y\' to roll the dice"))

roll_again = "yes"


while 'yes' == roll_again or 'y' == roll_again:

    print("Rolling the dice.....\n")

    print(random.randint(min_value,max_value))
    print("\n")


    roll_again = str(input("Enter \'yes\' or \'y\' to roll the dice\n"))


