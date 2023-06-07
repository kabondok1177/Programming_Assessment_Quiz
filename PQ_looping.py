def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
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

            # check that integer is valid (ie: not too low / too hig etc)
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


# main routine goes here

questions_asked = 0
rounds_won = 0

mode = "regular"

rounds = int_check("How many rounds", 1, exit_code="")

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

    miss_is_awesome = input("End it?")
    if miss_is_awesome == "xxx":
        break

    questions_asked += 1

    # check if we are out of rounds
    if questions_asked >= rounds:
        break
