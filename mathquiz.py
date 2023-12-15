import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def quiz():
    score = 0
    num_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be asked 5 math questions.")

    for _ in range(num_questions):
        question, correct_answer = generate_question()

        user_answer = input(f"What is {question}? ")

        if int(user_answer) == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    print(f"You got {score} out of {num_questions} questions correct. Thanks for playing!")

if __name__ == "__main__":
    quiz()
