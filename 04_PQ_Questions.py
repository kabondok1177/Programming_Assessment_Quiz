import random

questions = [
    "What is your favorite color?",
    "What is the capital of France?",
    "What is the square root of 25?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What is the main ingredient in sushi?",
    "Who wrote the novel 'Pride and Prejudice'?",
    "What is the symbol for the chemical element gold?",
    "What is the tallest mountain in the world?",
    "Who discovered gravity?"
]


def generate_random_question():
    return random.choice(questions)


# Example usage
for _ in range(5):
    question = generate_random_question()
    print(question)
