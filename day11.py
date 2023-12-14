import itertools

puzzle_input = list(map(list,open(0).read().strip().splitlines()))

result = 0

galaxies = []
for row in range(len(puzzle_input)):
    for col in range(len(puzzle_input[0])):
        if puzzle_input[row][col] == '#':
            galaxies.append((row, col))

combos = list(itertools.combinations(galaxies, 2))

for a, b in combos:
    row1 = min(a[0], b[0])
    row2 = max(a[0], b[0])
    col1 = min(a[1], b[1])
    col2 = max(a[1], b[1])

    distance = 0
    for i in range(row2 - row1):
        if all([puzzle_input[row1+i][col] == '.' for col in range(len(puzzle_input[0]))]):
            distance += 1000000
        else:
            distance += 1

    for i in range(col2 - col1):
        if all([puzzle_input[row][col1+i] == '.' for row in range(len(puzzle_input))]):
            distance += 1000000
        else:
            distance += 1

    result += distance


print(result)
