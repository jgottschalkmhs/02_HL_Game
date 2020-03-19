# HL component 3 - compares user guess with secret number

# To do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'Well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""
feedback = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    # If user has 1+ guesses left...
    if guesses_left > 2:

        if guess > SECRET:
            feedback = "Too high, please try again."
        elif guess < SECRET:
            feedback = "Too low, please try again."
        elif guess == SECRET:
            # If user guessed right the first time...
            if guesses_left == GUESSES_ALLOWED - 1:
                feedback = "Amazing! You got it in one guess!"
            # If user has had more than one guess...
            else:
                if guesses_left == 1:
                    feedback = "Good job! You guessed the number! You got it in {} guesses. You had 1 guess left" \
                        .format(GUESSES_ALLOWED - guesses_left)
                elif guesses_left == 0:
                    feedback = "Superb! You guessed the number just in time! You used up all {} guesses." \
                               .format(GUESSES_ALLOWED - guesses_left)
                else:
                    feedback = "Great job! You guessed the number! You got it in {} guesses. You had {} guess(es) " \
                               "left".format(GUESSES_ALLOWED - guesses_left, guesses_left)
    # If user has one guess left...
    elif guesses_left == 1:
        feedback = feedback + "\nYou have one guess left"

    elif guesses_left == 0:
        if guess > SECRET:
            feedback = "Too high. Game over :("
        elif guess < SECRET:
            feedback = "Too low. Game over :("
        else:
            feedback = "Superb! You guessed the number just in time! You used up all {} guesses." \
                               .format(GUESSES_ALLOWED - guesses_left)

    print(feedback)
