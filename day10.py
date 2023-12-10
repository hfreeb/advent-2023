puzzle_in = open(0).read().strip().splitlines()

start_row = None
start_col = None
for i, line in enumerate(puzzle_in):
    if 'S' in line:
        start_row = i
        start_col = line.index('S')
        break

# Input-specific
puzzle_in[start_row] = puzzle_in[start_row].replace('S', '|')
direction = (1, 0)

row = start_row + direction[0]
col = start_col + direction[1]
distance = 1

pipes = {(row, col)}

while row != start_row or col != start_col:
    pipe = puzzle_in[row][col]
    if pipe == '|' or pipe == '-':
        # Keep direction
        pass
    elif pipe == 'L' or pipe == '7':
        direction = (direction[1], direction[0])
    elif pipe == 'J' or pipe == 'F':
        direction = (-direction[1], -direction[0])

    row += direction[0]
    col += direction[1]
    distance += 1

    pipes.add((row, col))

print(distance // 2)

total = 0
for row, line in enumerate(puzzle_in):
    for col, symbol in enumerate(line):
        if (row, col) in pipes:
            continue

        intersections = 0
        for col_check in range(col+1, len(line)):
            if line[col_check] in ('|', 'J', 'L') and (row, col_check) in pipes:
                intersections += 1

        if intersections % 2 == 1:
            total += 1

print(total)
