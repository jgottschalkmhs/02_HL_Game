# Higher/Lower Game

# Version 1.4 log

# To do:
# 1a) (Theoretical) Make different boundary requirements for each difficulty
# 1b) (Practical) Cut, then paste boundary inputs 3 times for each difficulty, with different max\min  values for each
# 2) Add option to choose your own number of guesses
# 3) Change location of "Rounds" explanation to the beginning with the into + instructions
# 4a) Changing most 'else' statements into 'elif', and changing the 'else' statements into error messages of the
#     code not working properly (ie: code should never reach 'else' part of the code, only 'if' or 'elif')
# 4b) Create READ_ME file with all error messages and their convenience defined, and how to troubleshoot them.
# 5) Improve bits and pieces of the visual appeal of the project

# >>> Ideas for future versions:
# Change difficulties to: Easy, Challenging, Hard and Extreme

# Give more accurate feedback (low rather than too low or high rather than too high)
# Add suggestions-taking code + link to local storage (database perhaps)
# Use statement generator more often for visual appeal
# Add animation at the end of the game
# Create Developer mode: asks for password first > then allows user to use program without any limitations
# Create Casual/fun mode: asks for password first > normal program but with funny elements (ie: number of guesses =
#       letters in user's name & max rounds = their age etc...)
# PLay some music?

# Import libraries
import random
import math


# Number checking function goes here
def intcheck(question, low = None, high = None):

    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} (inclusive).".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or equal to {}, " \
                "and less than {}.".format(low, high)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or equal to {}.".format(high)
    else:
        error = "Please enter a positive integer."

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
print("All rounds will have different secret numbers, but the range\n"
      "will stay as your lower and upper boundary all throughout. \n"
      "You can choose to start over with different boundaries after\n"
      "you have finished all rounds. Max: 25 rounds.")
print()
print("\nNote: In Python, anytime you want to 'push a key', make sure it's a valid character\non the keyboard."
      " After you push a valid key, push <enter> to submit your input.\n")
tip_input = input("\033[44;47mTo find out a useful tip for the game, push any key.\033[m\n"
                  "\033[44;47mOtherwise, push <enter> to start playing!\033[m")

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
    
    # GK: Loop to allow users to change their mind on the difficulty level
    difficulty_keep_going = ""
    while difficulty_keep_going == "":
        # GK: Easy, medium and hard options have been highlighted in green, orange and red
        # GK: You could put details of the codes here (ie: which bit of the code below makes the label red?
        difficulty = input(">>> Please choose a game difficulty to play\n\n"
                           "(Type the letter code or the difficulty itself)\n"
                           "|\033[44;42m   Easy (E)   \033[m|\033[44;43m   Medium (M)   \033[m|\033[44;41m"
                           "   Hard (H)   \033[m|\n\n\n\033[1mDifficulty: \033[0m\n")
        
        # GK: Repeat the 'difficulty' question until a valid answer is entered
        while difficulty.lower() != "e" and difficulty.lower() != "easy" and difficulty.lower() != "m" and \
                difficulty.lower() != "medium" and difficulty.lower() != "h" and difficulty.lower() != "hard":
            print()
            difficulty = input("Sorry, I didn't catch that. Enter E, M or H for\n"
                               "easy, medium or hard difficulties, respectively.\n\n\033[1mDifficulty: \033[0m")

        # Set back-end difficulty value
        if difficulty.lower() == "easy" or difficulty.lower() == "e":
            game_diff = "Easy"
        elif difficulty.lower() == "medium" or difficulty.lower() == "m":
            game_diff = "Medium"
        elif difficulty.lower() == "hard" or difficulty.lower() == "h":
            game_diff = "Hard"
        else:
            print("Error 128 - big deal! Report to developer immediately.")

        # confirm difficulty
        difficulty_keep_going = input("The difficulty you have chosen is {}.\n"
                                      "Push <enter> to change it, or any other key to proceed.".format(game_diff))
        print()

    # Define variable (to eliminate weird error messages?)
    guesses_allowed = ""
    guess_input_status = ""

    # Easy difficulty
    if game_diff == "Easy":
        # Boundary inputs
        low = intcheck(">>> Please choose a\033[1m lower boundary: \033[0m", 1, 999999991)
        high = intcheck(">>> Please choose a\033[1m higher boundary: \033[0m", low + 1, 1000000000)
        # Guesses calculator
        # Really easy - 2 to 10 extra guesses than needed by binary search
        range = high - low + 1
        max_raw = math.log2(range)
        max_rounded_up = math.ceil(max_raw)
        part1 = math.ceil(max_raw)
        len_range = len(str(range - 1))
        part2 = 2 * int(len_range)
        guesses_allowed = part1 + part2
        # Allow custom guess input
        guess_input_status = "yes"

    # Medium difficulty
    elif game_diff == "Medium":
        # Boundary inputs
        low = intcheck(">>> Please choose a\033[1m lower boundary: \033[0m", 1, 999991)
        high = intcheck(">>> Please choose a\033[1m higher boundary: \033[0m", low + 9, 1000000)
        # Guesses calculator
        # Min # of guesses required using binary search (Log base 2 of range, rounded up to nearest whole number)
        range = high - low + 1
        max_raw = math.log2(range)
        guesses_allowed = math.ceil(max_raw)
        # Allow custom guess input
        guess_input_status = "yes"

    # Hard difficulty
    elif game_diff == "Hard":
        # Boundary inputs
        low = intcheck(">>> Please choose a\033[1m lower boundary: \033[0m", 1, 999991)
        high = intcheck(">>> Please choose a\033[1m higher boundary: \033[0m", low + 19, 1000000)
        # Guesses calculator
        # Requires luck to win - not enough guesses for complete binary search & bigger range = even lesser guesses
        max_rounded_up = math.ceil(math.log2(high - low + 1))
        if math.log2(high - low + 1) > 5:
            guesses_allowed = max_rounded_up - 2
        elif math.log2(high - low + 1) > 2:
            guesses_allowed = max_rounded_up - 1
        else:
            guesses_allowed = max_rounded_up
        # Prevent custom guess input
        guess_input_status = "no"

    else:
        # Code should never reach this part
        print("Error 128 - big deal! Report to developer immediately.")

    # How many rounds?
    rounds = intcheck(">>> Please choose the number of\033[1m rounds\033[0m you want to play: ", 1, 25)
    print()

    # Check for custom input for guesses
    if guess_input_status == "yes":
        custom_g_input = input("The preset algorithm has allowed you {} guesses. Do you want to\n"
                               "choose your\033[1m custom number\033[0m of guesses? ".format(guesses_allowed))
        while custom_g_input.lower() != "yes" and custom_g_input.lower() != "y" and custom_g_input.lower() != "no"\
                and custom_g_input.lower() != "n":
            custom_g_input = input("Sorry, I don't understand. Type either Yes/Y or No/N: ")
        if custom_g_input.lower() == "yes" or custom_g_input.lower() == "y":
            guesses_allowed = intcheck("How many guesses do you want to have? \n", 1, 999999999)
        elif custom_g_input.lower() == "no" or custom_g_input.lower() == "n":
            print("No problem. Best of luck!\n")
        else:
            print("Error 128 - big deal! Report to developer immediately.")

    elif guess_input_status == "no":
        print()

    else:
        print("Error 128 - big deal! Report to developer immediately.")

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
