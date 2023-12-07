import aoc
from functools import cmp_to_key

st = list(map(lambda x: x.split(' '), open(0).read().strip().splitlines()))

result = 0

cards = 'AKQT98765432J'

def hand_type_j(a:str):
    highest = 0
    for c in cards:
        if c == 'J':
            continue

        replaced = a.replace('J', c)
        value = hand_type(replaced)
        if hand_type(replaced) > highest:
            highest = value
    return highest

def hand_type(a):
    freq = {}
    for char in a:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    if 5 in freq.values():
        return 6
    if 4 in freq.values():
        return 5
    if 3 in freq.values() and 2 in freq.values():
        return 4
    if 3 in freq.values():
        return 3
    if list(freq.values()).count(2) == 2:
        return 2
    if 2 in freq.values():
        return 1
    return 0

def compare(a_l, b_l):
    a = a_l[0]
    b = b_l[0]
    if hand_type_j(a) > hand_type_j(b):
        return 1
    elif hand_type_j(b) > hand_type_j(a):
        return -1

    for i in range(len(a)):
        if cards.index(a[i]) < cards.index(b[i]):
            return 1
        elif cards.index(a[i]) > cards.index(b[i]):
            return -1

    return 0

st = sorted(st, key=cmp_to_key(compare))

for i, line in enumerate(st):
    result += int(line[1])*(i+1)

print(result)
