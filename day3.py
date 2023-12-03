import aoc
from operator import mul
from functools import reduce

st = open(0).read().strip().splitlines()

grid = []
for line in st:
    row = []

    num_str = ''
    for c in line:
        if c.isdigit():
            num_str += c
            continue

        if num_str:
            for x in range(len(num_str)):
                row.append(int(num_str))
            num_str = ''

        row.append(c)

    for x in range(len(num_str)):
        row.append(int(num_str))

    grid.append(row)

result = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '*':
            continue
        
        part = False

        adj = set()

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if col + dx >= len(st[0]) or row + dy >= len(st):
                    continue
                if dx == 0 and dy == 0:
                    continue

                d = grid[row+dy][col+dx]

                if isinstance(d, int):
                    adj.add(d)

        if len(adj) == 2:
            result += reduce(mul, adj, 1)

print(result)
