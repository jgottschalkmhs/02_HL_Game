# Higher/Lower Game

# Version 1.2 log

# Improvements/things to add:
# 1) Clarify user inputs & reasons behind certain limitations
# 2) Clarify difference between rounds and looping the whole game at the end
# 3) Remove all typos/spelling errors


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


welcome = h1_statement("\033[1m    ===     Higher/Lower Game        ===", "=\033[0m")
print("\nWelcome to HL game, by Aref Osman. The game will generate a secret number\n"
      "between the 2 numbers that you will give shortly. Your task is to find that number\n"
      "by guessing integer values in the range you have given, receiving feedback only as\n"
      "'too low' or 'too high'. The program will not tell you how far or close you are from\n"
      "guessing the secret number correctly. A set algorithm will determine the number of\n"
      "guesses that you will be allowed to use per round.")
print()
print("\nNote: In Python, anytime you want to 'push a key', make sure it's a valid character\non the keyboard."
      " After you push a valid key, push <enter> to submit your input.\n")
tip_input = input("\033[44;47mTo find out a useful tip for the game, push any key. Otherwise, push enter to start"
                  " playing!\033[m")

if tip_input != "":
    print("\n\033[1mJK! April fools! You're on your own :((((\033[0m\n")
else:
    print("\n\033[1mGood one! You wouldn't need it anyway - trust me!\033[0m")

print("----------------------------------------------------\n")

# Introduction to go here

# Game loop starts here
keep_going = ""
while keep_going == "":

    # Upper/lower boundary input
    low = intcheck("Please choose a \033[1mlower boundary: \033[0m", 1, 999991)
    high = intcheck("Please choose a higher boundary.\n"
                    "It has to be at least 9 more than your lower boundary.\n"
                    "\033[1mHigher boundary: \033[0m", low + 9, 1000000)

    # How many rounds?
    rounds = intcheck("How many rounds do you want to play?\n"
                      "All rounds will have different secret numbers, but the range\n"
                      "will stay as your lower and upper boundary all throughout. \n"
                      "You can choose to start over with different boundaries after\n"
                      "you have finished all rounds. Max: 25 rounds. \033[1mRounds: \033[0m", 1, 25)
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
    print("\033[1mA secret number has been generated. It's in between your given boundaries (inclusive).")
    print("You have a maximum of {} guesses to guess the secret number, per round.".format(guesses_allowed))
    print("The secret number will change each round, but will remain within the boundaries.\033[0m")

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
            guess = intcheck("\033[1mWhat is your guess? \033[0m", low, high)

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
                               "\nYou still have \u0332{} guesses left\n".format(guesses_left)
                    print(feedback)

                elif guess > secret:
                    feedback = "\n\033[44;46mToo high, please try a lower number\033[m" \
                               "\nYou still have \u0332{} guesses left\n".format(guesses_left)
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
        summary = "Round {}: {} guesses made ({})".format(rounds_played + 1, guesses_allowed - guesses_left, status)
        game_summary.append(summary)

        game_stats.append(guesses_allowed - guesses_left)

        # Adds number of guesses to list so that average can be worked out

        print("\n\033[1m\033[44;42m Won: {} \t | \t Lost: {} \033[m\033[0m".format(num_won, rounds_played
                                                                                   - num_won + 1))
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
    print("Best: {} guess(es)".format(best))
    print("Worst: {} guesses".format(worst))
    print("Average: {:.0f} guess(es)".format(average))

    # Loop game or not? + farewell
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()

print("Thank you for playing! Hope you enjoyed it! ")
