name = input("What's you name? ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are a on dirt road, it has come to an end and you can go left or right. Which way do you expect to go? ").lower()

if answer == 'left':
    answer = input(
        "You come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim across? ").lower()

    if answer == 'swim':
        print("You swim across and now you are breakfast to the crocodile. ")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lost the game.")

elif answer == 'right':

    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross or go back? Type in cross to cross or back to go back. ").lower()

    if answer == "cross":
        answer = input(
            "You cross the bridge an meet a stranger. Do you talk to him (yes/no)? ").lower()

        if answer == 'yes':
            print("Congrats- you won the game!")
            quit()
        else:
            print("Game over!")
            quit()
    elif answer == "back":
        print("You go back to the main road and you lost the game.")
    else:
        print("Not a valid option. You lost the game.")

else:
    print("Not a valid option. You lose.")
