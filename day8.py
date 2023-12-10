import math
import re

puzzle_in = open(0).read().strip().splitlines()

instructions = puzzle_in[0]

result = 0

network = {}

for line in puzzle_in[2:]:
    source, l, r = re.fullmatch(r"(.+) = \((.+), (.+)\)", line).groups()
    network[source] = (l, r)

steps = 0
pos = 'AAA'
while pos != 'ZZZ':
    if instructions[steps % len(instructions)] == 'L':
        pos = network[pos][0]
    else:
        pos = network[pos][1]
    steps += 1

print(steps)

nodes = []
for node in network.keys():
    if node.endswith('A'):
        nodes.append(node)

done = False

total_steps = []
for pos in nodes:
    steps = 0
    while not pos.endswith('Z'):
        if instructions[steps % len(instructions)] == 'L':
            pos = network[pos][0]
        else:
            pos = network[pos][1]
        steps += 1

    total_steps.append(steps)

print(math.lcm(*total_steps))
