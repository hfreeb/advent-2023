st = list(map(list, open(0).read().strip().splitlines()))

def roll(grid):
    # North
    for col in range(len(st[0])):
        tilted_row = 0
        for row in range(len(st)):
            if st[row][col] == '#':
                tilted_row = row + 1
            elif st[row][col] == 'O':
                if tilted_row != row:
                    grid[tilted_row][col] = 'O'
                    grid[row][col] = '.'
                tilted_row += 1

    # West
    for row in range(len(st)):
        tilted_col = 0
        for col in range(len(st[0])):
            if st[row][col] == '#':
                tilted_col = col + 1
            elif st[row][col] == 'O':
                if tilted_col != col:
                    grid[row][tilted_col] = 'O'
                    grid[row][col] = '.'
                tilted_col += 1

    # South
    for col in range(len(st[0])):
        tilted_row = len(st[0]) - 1
        for row in range(len(st) - 1, -1, -1):
            if st[row][col] == '#':
                tilted_row = row - 1
            elif st[row][col] == 'O':
                if tilted_row != row:
                    grid[tilted_row][col] = 'O'
                    grid[row][col] = '.'
                tilted_row -= 1

    # East
    for row in range(len(st)):
        tilted_col = len(st) - 1
        for col in range(len(st[0]) - 1, -1, -1):
            if st[row][col] == '#':
                tilted_col = col - 1
            elif st[row][col] == 'O':
                if col != tilted_col:
                    grid[row][tilted_col] = 'O'
                    grid[row][col] = '.'
                tilted_col -= 1


seen = {}
reverse = {}

i = 0
while True:
    roll(st)
    i += 1

    encoded = '\n'.join(list(map(lambda line: ''.join(line), st)))
    if encoded in seen:
        # This is probably overcomplicated
        multiples = (1000000000 - seen[encoded]) // (i - seen[encoded])
        extra = 1000000000 - seen[encoded] - multiples * (i - seen[encoded])
        final = reverse[seen[encoded] + extra]
        break

    seen[encoded] = i
    reverse[i] = encoded

final = final.splitlines()

load = 0
for col in range(len(final[0])):
        for row in range(len(final)):
            if final[row][col] == 'O':
                load += len(final) - row

print(load)
