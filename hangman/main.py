import random
game = ["rock", "paper", "scissors"]
user_input = input("Enter rock, paper or scissors: ")
while user_input not in game:
    user_input = input("Enter rock, paper or scissors: ")
bot = random.choice(game)
if user_input == "rock" and bot == "paper":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You lost!")
elif user_input == "rock" and bot == "scissors":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You won!")
elif user_input == "paper" and bot == "rock":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You won!")
elif user_input == "paper" and bot == "scissors":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You lost!")
elif user_input == "scissors" and bot == "paper":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You won!")
elif user_input == "scissors" and bot == "rock":
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("You lost!")
elif user_input == bot:
    print(f"Your choice {user_input}", f"Computers choice {bot}")
    print("It's a draw")