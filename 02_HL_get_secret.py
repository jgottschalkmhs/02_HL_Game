# HL component 2 - Generates random number between low and high


import random
import math

# set boundaries
LOW = 1
HIGH = 4


# find a random number within range
number = random.randint(LOW, HIGH)


# find length & log base 2 of random number (HLGI)
HLGI = "{}".format(number)
digHLGI = len(HLGI)
dig2HLGI = "{}".format(digHLGI)

logb2_of_HLGI = math.log2(number)
minguessHLGI = "{:.0f}".format(logb2_of_HLGI)

# calculate number of guesses
# formula: number of guesses = (2 * digits in HLGI) + minimum guesses needed via binary search
guesallow = (2*dig2HLGI) + minguessHLGI


# print results
print("HLGI: " + HLGI)
print("\t")
print("Digits in the HLGI: " + dig2HLGI)
print("\t")
print("Log base 2 of HLGI: " + minguessHLGI)
print("\t")
print("Number of guesses allowed is 2 times the number of digits in \nthe HLGI plus the log base 2"
      " of the HLGI. For the values above,\nthe number of guesses allowed is: " + guesallow)