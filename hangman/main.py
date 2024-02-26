import random


tries = 0


def hangman():
    #   Defining the secret words
    secret_words = ["Tranquility", "Adventure", "Wanderlust", "Discovery", "Empower", "Illuminate", "Courage"]
    #   Choosing secret word
    word = random.choice(secret_words)
    tries = len(word)
    #   Hints cases for secret words
    if word == "Tranquility":
        print("It is called quality or being in state of tranquil")
    elif word == "Adventure":
        print("Exciting or unusual thrilling experience")
    elif word == "Wanderlust":
        print("A strong desire to travel")
    elif word == "Discover":
        print("Finding something or making for the first time")
    elif word == "Empower":
        print("To give someone power of authority")
    elif word == "Illuminate":
        print("Making something visible or brighter")
    elif word == "Courage":
        print("The ability to do something that frightens one")

    #   Getting input of the character for the game
    user_input = input("Enter character of the word: ")


hangman()