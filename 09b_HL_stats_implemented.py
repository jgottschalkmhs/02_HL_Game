# HL component 9b - End Game Stats

# To do
# Set up game-play list with each round's results
# Set up average, best and worst scores (see 09a Stats experiment)


SECRET = 7
GUESSES_ALLOWED = 4
rounds = int(input("How many rounds? "))
game_summary = []   # list to record results of each round
game_stats = []     # list to hold number of guesses (to work out average)

num_won = 0
rounds_played = 0

feedback = "n/a"
status = "won"

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))
        guesses_left -= 1

        if guesses_left < 1:
            if guess < SECRET:
                feedback = "\nSorry you lost (too low)"
                status = "lost"
                break
            elif guess > SECRET:
                feedback = "\nSorry you lost (too high)"
                status = "lost"
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

            elif guess == SECRET:
                feedback = "\nWell done! You guessed the secret number"
                num_won += 1
                if guesses_left == 1:
                    feedback = feedback + "\nYou had 1 guess remaining"
                else:
                    feedback = feedback + "\nYou had {} guesses remaining".format(guesses_left)
                    break

    print(feedback)

    # Adds results to summary list
    summary = "{}: {} ({})".format(rounds_played+1, GUESSES_ALLOWED - guesses_left, status)
    game_summary.append(summary)

    game_stats.append(GUESSES_ALLOWED - guesses_left)

    # Adds number of guesses to list so that average can be worked out


    print("\nWon: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

    if rounds_played == rounds:
        print("Thank you for playing the Higher/Lower game! ")
    else:
        continue

# print each round's outcome...
print()
print("*** Game scores ***")

# Outputs list of rounds and results
for item in game_summary:
    print(item)


# Calculate (and then print) game statistics
game_stats.sort()
best = game_stats[0]        # first item in sorted list
worst = game_stats[-1]      # last item in sorted list
average = sum(game_stats)/len(game_stats)

print()                 # For debugging purposes
print(game_stats)       # For debugging purposes
print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))
