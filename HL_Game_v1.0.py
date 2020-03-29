# Higher/Lower Game

# To do
# Join all components neatly
# Do usability testing
# Complete evidence taking and submit assignment

import random
import math

# Number checking function goes here


def intcheck(question, low=None, high=None):

    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} (inclusive):".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or equal to {}, " \
                "and less than {}:".format(low, 1000000)
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


def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()


# Introduction to go here

# Game loop starts here
keep_going = ""
while keep_going == "":

    # Upper/lower boundary input
    low = intcheck("Please choose a lower boundary: ", 1, 999991)
    high = intcheck("Please choose a higher boundary: ", low + 9, 1000000)

    # How many rounds?
    rounds = intcheck("How many rounds? ", 1, 25)
    game_summary = []  # list to record results of each round
    game_stats = []  # list to hold number of guesses (to work out average)

    # Maximum guesses calculator
    print()
    range = high - low + 1
    max_raw = math.log2(range)
    part1 = math.ceil(max_raw)
    len_range = len(str(range - 1))
    part2 = 2 * int(len_range)
    guesses_allowed = part1 + part2
    print("Max guesses: {}".format(guesses_allowed))

    num_won = 0
    rounds_played = 0
    feedback = "n/a"
    status = "won"

    # Begin game
    while rounds_played < rounds:

        # Generate HLGI (secret number)
        secret = random.randint(low, high)

        guess = ""
        guesses_left = guesses_allowed
        already_guessed = []

        # Round number - heads-up to user
        start_round = h1_statement("--    Round {} of {}    -- ".format(rounds_played + 1, rounds), "-")

        # Comparisons
        while guess != secret and guesses_left >= 1:
            guess = intcheck("\033[1mWhat is your guess?: \033[0m", low, high)

            # checks that guess is not a duplicate
            if guess in already_guessed:
                print("You have already guessed that number! PLease try again. "
                      "You *still* have {} guesses left".format(guesses_left))
                continue

            already_guessed.append(guess)
            guesses_left -= 1

            # Lose/final guess situation
            if guesses_left < 1:
                if guess < secret:
                    feedback = "\nSorry you lost (too low). The secret number was " \
                               "{}".format(secret)
                    status = "lost"
                    break
                elif guess > secret:
                    feedback = "\nSorry you lost (too high). The secret number was " \
                               "{}".format(secret)
                    status = "lost"
                    break
                else:
                    feedback = "\n\033[44;46mWell done! You guessed the secret number.\033[m\n" \
                               "\n\033[44;46mYou got it on the final guess.\033[m"
                    num_won += 1
                    break

            # Got it on first try
            elif guess == secret and guesses_left == (guesses_allowed - 1):
                feedback = "\n\033[44;46mAwesome! You got it on the first guess\033[m"
                num_won += 1
                break

            # Higher or lower comparing
            else:
                if guess < secret:
                    feedback = "\n\033[44;46mToo low, please try a higher number\033[m" \
                               "\nYou still have \u0332{} guesses left".format(guesses_left)
                    print(feedback)

                elif guess > secret:
                    feedback = "\n\033[44;46mToo high, please try a lower number\033[m" \
                               "\nYou still have \u0332{} guesses left".format(guesses_left)
                    print(feedback)

                # Win situation
                elif guess == secret:
                    feedback = "\n\033[44;46mWell done! You guessed the secret number\033[m"
                    num_won += 1
                    if guesses_left == 1:
                        feedback = feedback + "\nYou had \u03321 guess remaining"
                    else:
                        feedback = feedback + "\nYou had \u0332{} guesses remaining".format(guesses_left)
                        break

        print(feedback)

        # Adds results to summary list
        summary = "Round {}: {} ({})".format(rounds_played + 1, guesses_allowed - guesses_left, status)
        game_summary.append(summary)

        game_stats.append(guesses_allowed - guesses_left)

        # Adds number of guesses to list so that average can be worked out

        print("\n\033[1m\033[44;42m Won: {} \t | \t Lost: {} \033[m\033[0m".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

    # Display total scores
    print()
    print("*** Game scores ***")

    # Outputs
    for item in game_summary:
        print(item)

    # Calculate (and then print) game statistics
    game_stats.sort()
    best = game_stats[0]  # first item in sorted list
    worst = game_stats[-1]  # last item in sorted list
    average = sum(game_stats) / len(game_stats)

    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    # Loop game or not? + farewell
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()

print("Thank you for playing! Hope you enjoyed it! ")
