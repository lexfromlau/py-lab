print("Welcome to my computer quiz!")

count = 0
answers = 0

answer = input("Do you want to play? ")

if answer.lower() != "yes":
    print("Okay, maybe next time")
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
answers += 1

if answer.lower() == "central processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect. CPU stands for: central processing unit")

answer = input("What does GPU stand for? ")
answers += 1

if answer.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect. GPU stands for: graphics processing unit")

answer = input("What does RAM stand for? ")
answers += 1

if answer.lower() == "random access memory":
    print("Correct!")
    count += 1
else:
    print("Incorrect. RAM stands for: random access memory")

print(f"You got {count} out of {answers}")