import random

print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")


def guessing():
    random_number = random.randrange(1, 99)
    print(random_number)
    difficulty = input("choose  difficulty: type 'easy' or 'hard': ")
    number_guess = 5
    print(f"you have {number_guess} remaining")

    if difficulty == "easy":
        number_guess = 10
    else:
        number_guess = 5

    while number_guess:

        number = int(input("Enter the number: "))
        if number < random_number:
            number_guess -= 1
            print("number is low.")
            print(f"you have {number_guess} remaining")
            print("guess again")

        elif number > random_number:
            number_guess -= 1
            print("This number is high")
            print(f"you have {number_guess} remaining")
        elif number == random_number:

            print("correct number")
        if number_guess==0:
            print("you have run out of guesses")
        if number_guess == 0 or number == random_number:
            number_guess = 0
            restart = input("Would you like to restart: 'y' or 'N' ").lower()
            if restart == "y":
                guessing()
            else:
                return "Goodbye"




guessing()
