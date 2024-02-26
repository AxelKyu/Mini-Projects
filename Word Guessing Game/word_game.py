import time
word = "Elephant"
count = 0
score = 0
hint_count = 0
print("The animal is very big, vegeterian and it's babies name is calf")
while count <= 3:
    user_input = input("Enter your word: ")
    count += 1
    if user_input.capitalize() == word:
        print(f"{user_input} is correct")
        if hint_count == 0:
            print(f"Number of hints used: {hint_count}")
            score += 5
            print(f"Your score is: {score}")
        elif hint_count != 0:
            print(f"Number of hints used: {hint_count}")
            score += 3
            print(f"Your score is: {score}")
        break
    elif user_input != word:
        print("Your answer is incorrect")
        hint = input("Press H for hint: ")
        if hint.upper() == "H":
            print("The animal is very big and has a trunk")
            count -= 1
            hint_count += 1
    elif count == 3:
        print("Your tries are over!")
        score -= 5
        print(f"Your score is: {score}")
        if hint_count == 0:
            print(f"Number of hints used: {hint_count}. Try again later!")
        elif hint_count != 0:
            print(f"Number of hints used: {hint_count}. Try again later!")