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
    verb = "55"

    # Define a dictionary of possible answers
    answers = {
        " You have a {noun}, one {noun2} is 30, the other {noun2} is  ?": "The {noun} of {noun2} is a fruit.",
        "Who {noun3 } {noun}?": f"People {verb} {noun}.",
        f"When did {noun} {verb}?": f"{noun} {verb} in the afternoon.",
        f"Why is {noun} {verb}?": f"{noun} is {verb} because it's delicious.",
        f"How does {noun} {verb}?": f"{noun} {verb} by using its mouth."
    }

    # Substitute the placeholders in the template with the generated numbers
    questions = template.format(noun=noun, noun2=noun2, verb=verb,)

    # Retrieve the corresponding answer
    answers = answers[template]

    return questions, answers


# Generate a question and its answer
question, answer = generate_question_format_1()

print("Question:", question)
print("Answer:", answer)
