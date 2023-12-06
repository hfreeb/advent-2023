import aoc

st = open(0).read().strip().splitlines()

result = 1

times = aoc.ints(st[0])
distances = aoc.ints(st[1])
for i in range(len(times)):
    time = times[i]
    record = distances[i]

    beaten = 0
    for held in range(time):
        displacement = held * (time - held)
        if displacement > record:
            beaten += 1
        elif beaten > 0:
            break

    result *= beaten

print(result)
