import random


def generate_question_format_1():
    # Define a list of possible question templates
    templates = [
        "What is the {noun} of {noun2}?",
        "Who {verb} {noun}?",
        "When did {noun} {verb}?",
        "Why is {noun} {verb}?",
        "How does {noun} {verb}?"
    ]

    # Select a random template
    template = random.choice(templates)

    # Generate random nouns and other words
    noun = "triangle"
    noun2 = "angle"
    noun3 = "55"

    # Define a dictionary of possible answers
    answers = {
        " You have a {noun}, one {noun2} is 30, the other {noun2} is  ?": "The {noun} of {noun2} is a fruit.",
        "Who {noun3 } {noun}?": f"People {noun3} {noun}.",
        f"When did {noun} {noun3}?": f"{noun} {noun3} in the afternoon.",
        f"Why is {noun} {noun3}?": f"{noun} is {noun3} because it's delicious.",
        f"How does {noun} {noun3}?": f"{noun} {noun3} by using its mouth."
    }

    # Substitute the placeholders in the template with the generated numbers
    questions = template.format(noun=noun, noun2=noun2, noun3=noun3, noun4=noun4)

    # Retrieve the corresponding answer
    answer = answers[template]

    return questions, answer


# Generate a question and its answer
question, answer = generate_question_format_1()

print("Question:", question)
print("Answer:", answer)
