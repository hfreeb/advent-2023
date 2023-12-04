import aoc
from operator import mul
from functools import reduce

input = open(0).read().strip().splitlines()

result1 = 0
result2 = 0

copies = {}

for idx, line in enumerate(input):
    line = line[line.index(':'):]
    winners, numbers = map(aoc.ints, line.split("|"))

    count = 1
    if (idx + 1) in copies:
        count += copies[idx + 1]

    matches = 0
    points = 0

    for number in numbers:
        if number in winners:
            matches += 1

            if points == 0:
                points = 1
            else:
                points *= 2

    for i in range(matches):
        if (idx+2+i) in copies:
            copies[idx+2+i] += count
        else:
            copies[idx+2+i] = count

    result1 += points
    result2 += count

print(result1, result2)
