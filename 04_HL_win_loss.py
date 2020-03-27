# HL component 3 - compares user guess with secret number

# To Do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    if guesses_left < 1:
        if guess < SECRET:
            feedback = "\nSorry you lost"
            break
        else:
            feedback = "\nWell done! You guessed the secret number.\n" \
                       "\nYou got it on the final guess."
            break

    elif guess == SECRET and guesses_left == (GUESSES_ALLOWED - 1):
        feedback = "\nAwesome! You got it on the first guess"
        break

    else:
        if guess < SECRET:
            feedback = "\nToo low, please try a higher number" \
                       "\nYou still have {} guesses left".format(guesses_left)
        elif guess > SECRET:
            feedback = "\nToo high, please try a lower number" \
                       "\nYou still have {} guesses left".format(guesses_left)

        else:
            feedback = "\nWell done! You guessed the secret number"
            if guesses_left == 1:
                feedback = feedback + "\nYou had 1 guess remaining"
            else:
                feedback = feedback + "\nYou had {} guesses remaining".format(guesses_left)
                break
    print(feedback)
print(feedback)

print("\nThank you for playing Higher/Lower game!")
