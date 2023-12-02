st = open(0).read().strip()

result = 0

for line in st.splitlines():
    colon = line.index(':')
    game_id = int(line[5:colon])

    possible = True

    minimum = {
            'red': 0,
            'green': 0,
            'blue': 0,
    }

    cube_sets =  line[colon+2:].split('; ')
    for cube_set in cube_sets:
        cubes = cube_set.split(', ')
        for cube in cubes:
            amount_str, colour = cube.split(' ')
            amount = int(amount_str)

            if amount > minimum[colour]:
                minimum[colour] = amount

    result += minimum['red'] * minimum['green'] * minimum['blue']

print(result)
