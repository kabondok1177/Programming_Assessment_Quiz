# Functions go here...
# check user answer yes / no to a question
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
    print("For each game you will be asked...")
    print("- What question format would you like to do \n"
          " '***Angles on a straight line or Angles in a triangle.***' \n"
          " Computer will generate 4 geometry questions from the level of your choice. \n"
          " After you answer all 4 of your questions, the computer will mark your answers, \n"
          " you will then be given your quiz results.")
    print("The computer will calculate how many guesses you are allowed")
    print(" If you would like to end the game before the end of your turn please enter xxx")
    print("*** Good Luck! :)  ***")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print("Program continues")
    