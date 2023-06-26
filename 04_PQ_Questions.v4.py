import random

while True:
    # Define a list of possible question templates
    templates = [
        "triangle", "straight line", "right angled triangle"
    ]

    # Select a random template
    template = random.choice(templates)

    # Generate random nouns and other words
    if template == "triangle":
        angle_1 = random.randint(1, 89)
        angle_2 = random.randint(1, 89)
        answer = 180 - angle_1 - angle_2

        question = f"You have a triangle with angles {angle_2} and {angle_1}.  What is the third angle?"
        print("spoiler alert", answer)

    input()

    if template == "straight line":
        total_angle = 180
        angle_1 = random.randint(1, total_angle - 1)
        angle_2 = total_angle - angle_1
        answer = angle_2

        question = f"There are 3 angles on a straight line two of the angles are {angle_1} and {angle_2}. What would " \
                   f"the " \
                   f"third angle be?"
        print("spoiler alert", answer)

    input()

    if template == "right angled triangle":
        right_angle = 90
        angle_1 = random.randint(1, 89)
        answer = 180 - right_angle - angle_1

        question = f"You have a right angled triangle, one angle is {angle_1} and the right angle is {right_angle}" \
                   f" what is your third angle?"
        print("spoiler alert", answer)

    input()
