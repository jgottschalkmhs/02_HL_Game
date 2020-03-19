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
    if guesses_left > 1:
        if guess > SECRET:
            feedback = "Too high, please try again."
        elif guess < SECRET:
            feedback = "Too low, please try again."
        else:
            feedback = "Great job"
    # If user has one guess left...
    elif guesses_left == 0:
        if guess > SECRET:
            feedback = "Too high. You only have one guess left!"
        elif guess < SECRET:
            feedback = "Too low. You only have one guess left!"
        else:
            feedback = "Great job!"


    print(feedback)

if guess == SECRET:
    # If user guessed right the first time...
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it in one guess!")
    # If user has had more than one guess...
    else:
        print("Good job! You guessed the number! You got it in {} guesses. You had {} guesses left"
              .format(GUESSES_ALLOWED - guesses_left, guesses_left))


