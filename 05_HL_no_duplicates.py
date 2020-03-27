# HL component 5 - no duplicates

# To do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number! PLease try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

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