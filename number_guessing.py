import random

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess > random_number:
            print("You are above the number")

        elif user_guess < random_number:
            print("You are below the number")
    else:
        print("Please type a number next time")

    if user_guess == random_number:
        print(f"You got it! It took {guesses} guesses")
        break
    else:
        print("You got it wrong!")
