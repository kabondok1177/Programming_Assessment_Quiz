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

    # Generate random nouns, verbs, and other words
    noun = "apple"
    noun2 = "banana"
    verb = "eat"

    # Substitute the placeholders in the template with the generated words
    question = template.format(noun=noun, noun2=noun2, verb=verb)

    return question


def generate_question_format_2():
    # Define a list of possible question templates
    templates = [
        "Which {noun} {verb} {noun2}?",
        "Who {verb} {noun} and {noun2}?",
        "When did {noun} {verb} {noun2}?",
        "Why do {noun} and {noun2} {verb}?",
        "How are {noun} and {noun2} {verb}?"
    ]

    # Select a random template
    template = random.choice(templates)

    # Generate random nouns, verbs, and other words
    noun = "cat"
    noun2 = "dog"
    verb = "play"

    # Substitute the placeholders in the template with the generated words
    question = template.format(noun=noun, noun2=noun2, verb=verb)

    return question


# Generate and print a question using format 1
question_format_1 = generate_question_format_1()
print("Question Format 1:")
print(question_format_1)

# Generate and print a question using format 2
question_format_2 = generate_question_format_2()
print("Question Format 2:")
print(question_format_2)
