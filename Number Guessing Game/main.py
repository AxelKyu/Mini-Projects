import random
import math
import time

#   initialization of upper and lower bound
lower_bound = int(input("Enter lower bound interval: "))
upper_bound = int(input("Enter upper bound interval: "))

#   Getting the guess number
random_integer = random.randint(lower_bound, upper_bound)

#   initialization of count
count = 0

print("You've got", round(math.log(upper_bound - lower_bound + 1, 2)), "chances")

#   Initialization of loop
while round(math.log(upper_bound - lower_bound + 1, 2)) > count:
    user_input = int(input("Enter your guess: "))
    count += 1
    if user_input > random_integer:
        print("Your guess is to high!")
    elif user_input < random_integer:
        print("Your guess is too low!")
    elif user_input == random_integer:
        print("Congratulations you guessed the correct number!")
        print(f"Total number of guess: {count}")
    elif round(math.log(upper_bound - lower_bound + 1, 2)) < count:
        print("Your out of guesses!")
        print(f"Total number of guess: {count}")
