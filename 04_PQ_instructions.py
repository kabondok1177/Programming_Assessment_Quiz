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
    print("- What level you would like to play? \n"
          " 'Easy, Medium or Hard'. \n"
          " Computer will generate a question from the level of your choice. \n"
          " You will get 5 questions \n"
          " after you answer all 5 of your questions, computer will mark your answers \n"
          " you will then be given your quiz results.")
    print("The computer will calculate how many guesses you are allowed")
    print("enter the number of rounds you want to play")
    print("guess the secret number")
    print()
    print("*** Good Luck! :)  ***")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print("Program continues")
