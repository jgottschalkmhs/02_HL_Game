# HL Component 8 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements

SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

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
                num_won += 1
                break

        elif guess == SECRET and guesses_left == (GUESSES_ALLOWED - 1):
            feedback = "\nAwesome! You got it on the first guess"
            num_won += 1
            break

        else:
            if guess < SECRET:
                feedback = "\nToo low, please try a higher number" \
                           "\nYou still have {} guesses left".format(guesses_left)
                print(feedback)
            elif guess > SECRET:
                feedback = "\nToo high, please try a lower number" \
                           "\nYou still have {} guesses left".format(guesses_left)
                print(feedback)

            else:
                feedback = "\nWell done! You guessed the secret number"
                num_won += 1
                if guesses_left == 1:
                    feedback = feedback + "\nYou had 1 guess remaining"
                else:
                    feedback = feedback + "\nYou had {} guesses remaining".format(guesses_left)
                    break

    print(feedback)
    print("\nWon: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

    if rounds_played == rounds:
        print("Thank you for playing the Higher/Lower game! ")
    else:
        continue

