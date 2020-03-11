# HL - Get (and check) user input

# To do
# Check a "lowest" is an integer (any positive integer + lower bound of 0)
# Check that "highest" is more than "lowest" and less than/equal to 10,000 (lower bound and upper bound)
# Check that "rounds" is more than 1 and less than 10 (upper bound and lower bound)
# Check that guess is between "lowest" and "highest" (lower bound and upper bound)


# Number checking function goes here
def intcheck(question, low = None, high = None):

    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} (inclusive):".format(low, high)

    elif low is not None and high is None:
        error = "Please enter an integer that is more than or equal to {}, " \
                "and less than {}:".format(low,10000)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or equal to {}:".format(high)
    else:
        error = "Please enter an positive integer:"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue
            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


# Main routine

lowest = intcheck("Low Number: ", 1, 9991)
print("\nSuccess!\n")
highest = intcheck("High number: ", lowest + 9, 10000)
rounds = intcheck("Rounds: ", 1, 10)
guess = intcheck("Guess: ", lowest, highest)