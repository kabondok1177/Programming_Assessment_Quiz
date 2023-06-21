import random

while True:
    # Define a list of possible question templates
    templates = [
        "triangle", "straight line"
    ]

    # Select a random template
    template = random.choice(templates)

    # Generate random nouns and other words
    if template == "triangle":
        angle_1 = random.randint(89.75)
        angle_2 = random.randint(89.75) 
        answer = 180 - angle_1 - angle_2

        question = f"You have a triangle with angles {angle_2} and {angle_1}.  What is the third angle?"
        print("spoiler alert", answer)

    input()
