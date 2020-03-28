# Higher/Lower Game

# Version 1.3 log

# To do:
# 1) Adding difficulties to the game - completed
# 2) Setting each difficulties' different algorithm for guesses - completed
# 3) Add more commenting to make code easier to understand in future references - completed
# 4) Work on visual appeal (highlighting and bold texts) - completed

# Import libraries
import random
import math

# Define high and low (to eliminate weird error messages?)
high = ""
low = ""


# Number checking function goes here
def intcheck(question, low = None, high = None):

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


# Statement generator
def h1_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


# Introduction to go here
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

print("-------------------------------------------------------------------------\n")

# Game loop starts here
keep_going = ""
while keep_going == "":

    # Set front-end game difficulty
    difficulty = ""
    game_diff = ""
    difficulty_keep_going = ""
    while difficulty_keep_going == "":
        difficulty = input(">>> Please choose a game difficulty to play\n\n"
                           "(Type the letter code or the difficulty itself)\n"
                           "|\033[44;42m   Easy (E)   \033[m|\033[44;43m   Medium (M)   \033[m|\033[44;41m"
                           "   Hard (H)   \033[m|\n\n\n\033[1mDifficulty: \033[0m\n")
        while difficulty.lower() != "e" and difficulty.lower() != "easy" and difficulty.lower() != "m" and \
                difficulty.lower() != "medium" and difficulty.lower() != "h" and difficulty.lower() != "hard":
            print("")
            difficulty = input("Sorry, I didn't catch that. Enter E, M or H for\n"
                               "easy, medium or hard difficulties, respectively.\n\n\033[1mDifficulty: \033[0m")

        # Set back-end difficulty value
        if difficulty.lower() == "easy" or difficulty.lower() == "e":
            game_diff = "Easy"
        elif difficulty.lower() == "medium" or difficulty.lower() == "m":
            game_diff = "Medium"
        else:
            game_diff = "Hard"

        # confirm difficulty
        difficulty_keep_going = input("The difficulty you have chosen is {}.\n"
                                      "Push <enter> to change it, or any other key to proceed.".format(game_diff))
        print()

        # Upper/lower boundary input
        low = intcheck(">>> Please choose a\033[1m lower boundary: \033[0m", 1, 999991)
        high = intcheck(">>> Please choose a\033[1m higher boundary: \033[0m", low + 9, 1000000)

        # Generic information for all formulae
        range = high - low + 1
        max_raw = math.log2(range)
        max_rounded_up = math.ceil(max_raw)
        guesses_allowed = ""

        # Max guesses for Easy difficulty
        if game_diff == "Easy":
            # Really easy - 2 to 10 extra guesses than needed by binary search
            part1 = math.ceil(max_raw)
            len_range = len(str(range - 1))
            part2 = 2 * int(len_range)
            guesses_allowed = part1 + part2

        # Max guesses for Medium difficulty
        elif game_diff == "Medium":
            # Min # of guesses required using binary search (Log base 2 of range, rounded up to nearest whole number)
            guesses_allowed = math.ceil(max_raw)

        # Max guesses for Hard difficulty
        elif game_diff == "Hard":
            # Requires luck to win - not enough guesses for complete binary search & bigger range = even lesser guesses
            if max_raw > 5:
                guesses_allowed = max_rounded_up - 2
            elif max_raw > 2:
                guesses_allowed = max_rounded_up - 1
            else:
                guesses_allowed = max_rounded_up

        else:
            # Code should never reach this part
            print("Error 01 - elif statements insufficient for proper criteria")


    # How many rounds?
    rounds = intcheck(">>> How many\033[1m rounds\033[0m do you want to play?\n"
                      "    All rounds will have different secret numbers, but the range\n"
                      "    will stay as your lower and upper boundary all throughout. \n"
                      "    You can choose to start over with different boundaries after\n"
                      "    you have finished all rounds. Max: 25 rounds. \033[1mRounds: \033[0m", 1, 25)
    print()

    # Set up lists
    game_summary = []  # list to record results of each round
    game_stats = []  # list to hold number of guesses (to work out average)

    # Heads-up about # of guesses and secret number
    print("\033[1mA secret number has been generated. It's in between your given boundaries (inclusive).")
    print("You have a maximum of {} guesses to guess the secret number, per round.".format(guesses_allowed))
    print("The secret number will change each round, but will remain within the boundaries.\033[0m")

    # Define variables
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
        print("\n\033[1m\033[44;42m Won: {}    |    Lost: {} \033[m\033[0m".format(num_won, rounds_played
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
