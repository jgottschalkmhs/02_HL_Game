# HL component 7 - Generates desired number of rounds...

rounds = int(input("How many rounds? "))
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played+1))
    rounds_played += 1

print("You have gotten to the end of the game")
