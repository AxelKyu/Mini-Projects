import random


tries = 0


def hangman():
    #   Defining the secret words
    secret_words = ["Tranquility", "Adventure", "Wanderlust", "Discovery", "Empower", "Illuminate", "Courage"]
    #   Choosing secret word
    word = random.choice(secret_words)
    tries = len(word)
    #   Hints cases for secret words
    match secret_words:
        case 1:
            print("It is called quality or being in state of tranquil")
        case 2:
            print("Exciting or unusual thrilling experience")
        case 3:
            print("A strong desire to travel")
        case 4:
            print("Finding something or making for the first time")
        case 5:
            print("To give someone power of authority")
        case 6:
            print("Making something visible or brighter")
        case 7:
            print("The ability to do something that frightens one")

    #   Getting input of the character for the game
    user_input = input("Enter character of the word!")
