import random


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (i.e., not too low / too high etc)
            if situation == "any integer":
                return response
            elif situation == "both":
                if low <= response <= high:
                    return response
            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("**** Welcome to the Geometry Quiz ****")
    print()
    print("For each game, you will be asked...")
    print("- What question format would you like to do \n"
          " '***Angles on a straight line or Angles in a triangle.***' \n"
          " Computer will generate geometry questions from the question format of your choice. \n"
          " After you answer all of your questions, the computer will mark your answers, \n"
          " you will then be given your quiz results.")
    print(" If you would like to end the game before the end of your turn, please enter xxx")
    print("*** Good Luck! :)  ***")
    print()
    print("Press enter for INFINITE mode")
    return ""


questions_asked = 0
rounds_won = 0

played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()

print("Program continues")

mode = "regular"

rounds = int_check("How many questions: ", low=1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {questions_asked + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {questions_asked + 1} of {rounds}"

    print(heading)

    questions_asked += 1

    # check if we are out of rounds
    if questions_asked > rounds:
        break

    # Define a list of possible question templates
    templates = [
        "triangle", "straight line", "right angled triangle"
    ]

    # Select a random template
    template = random.choice(templates)
    print("chosen template:", template)

    # Generate random nouns and other words
    if template == "triangle":
        angle_1 = random.randint(1, 89)
        angle_2 = random.randint(1, 89)
        answer = 180 - angle_1 - angle_2

        question = f"You have a triangle with angles {angle_1} and {angle_2}. What is the third angle?"
        print("Question:", question)
        user_answer = int_check("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            rounds_won += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")

    if template == "straight line":
        total_angle = 180
        angle_1 = random.randint(1, total_angle - 1)
        angle_2 = total_angle - angle_1
        answer = 180 - angle_1 - angle_2

        question = f"There is a triangle on a straight line. One of the ange is {angle_1} and the second angle is" \
                   f" {angle_2}. " \
                   f"What would the third angle be?"
        print("Question:", question)
        user_answer = int_check("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            rounds_won += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")

    if template == "right angled triangle":
        right_angle = 90
        angle_1 = random.randint(1, 89)
        answer = 180 - right_angle - angle_1

        question = f"You have a right angled triangle. One angle is {angle_1} and the right angle is {right_angle}. " \
                   f"What is your third angle?"
        print("Question:", question)
        user_answer = int_check("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            rounds_won += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")

    print()  # Empty line between questions

print(f"\n You answered {rounds_won} right out of {questions_asked} rounds.")
