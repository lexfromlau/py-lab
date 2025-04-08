def check_answer(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. {question.split()[2]} stands for: {correct_answer}")
        return False


print("Welcome to my computer quiz!")
count = 0
score = 0

if input("Do you want to play? ").lower() != "yes":
    print("Okay, maybe next time")
    quit()

print("Okay, let's play :)")

questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory"
}

for question, correct_answer in questions.items():
    count += 1
    if check_answer(question, correct_answer):
        score += 1

print(f"You got {score} out of {count}")
