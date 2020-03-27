# HL component 11 - Maximum Guesses Calculator

import math

for item in range(0, 4):

    low = int(input("Low: "))
    high = int(input("High: "))

    range = high - low + 1
    max_raw = math.log2(range)
    part1 = math.ceil(max_raw)

    len_range = len(str(range - 1))
    part2 = 2 * int(len_range)

    max_guesses = part1 + part2

    print("Max guesses: {}".format(max_guesses))
    print()
