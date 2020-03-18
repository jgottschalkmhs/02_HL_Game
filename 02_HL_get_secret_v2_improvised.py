# HL component 2 - Generates random number between low and high


import random
import math

# set boundaries
LOW = 20
HIGH = 50


# find a random number within range
number = str(random.randint(LOW, HIGH))


# find length of number & log base 2 of range between boundaries
dhlgi = str(len(number))
range = HIGH - LOW + 1
bnrysrch_minguesses = "{:.0f}".format(int(math.log2(range)))

# calculate number of guesses
# formula: number of guesses = (2 * digits in range between boundaries) + minimum guesses needed via binary search
max_guesses = (2*int(dhlgi)) + int(bnrysrch_minguesses)


# print results
print("HLGI: " + number)
print("\t")
print("Lower boundary: " + str(LOW))
print("\t")
print("Higher boundary: " + str(HIGH))
print("\t")
print("Range between boundaries: " + str(range))
print("\t")
print("Log base 2 of range: " + bnrysrch_minguesses)
print("\t")
print("Number of guesses allowed is '2' times 'the number of digits in \nthe range between upper and lower boundaries'"
      " plus 'the log base 2 \nof the HLGI (Higher/Lower Game Integer)'. For the values above,\nthe number of guesses "
      "allowed is: " + str(max_guesses))