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
    print(" '*** Angles on a straight line or Angles in a triangle.***' \n"
          " Computer will generate geometry questions. \n"
          " You will have 2 question formats 1 will be angles on a straight line angles in a triangle. "
          " After you answer all of your questions, the computer will mark your answers, \n"
          " you will then be given your quiz results.")
    print("")
    print("*** Good Luck! :)  ***")
    print()
    print("press enter for INFINITE mode")
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print("Program continues")
    