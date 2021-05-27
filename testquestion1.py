answer = "A Stick"
question = "What's brown and sticky?\n"
def quiz(question, answer):
    print("Are you ready for a question?")
    user_input = input(question)
    if user_input.strip().title() == answer:
        print("YES!!!")
    else:
        print(f"Wow, you suck! The answer was {answer}.\n")
quiz(question, answer)
