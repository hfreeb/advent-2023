import aoc

lines = open(0).read().strip().split("\n\n")

result = 0

seeds = aoc.ints(lines[0])
seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

maps = []
for section in lines[1:]:
    ranges = []
    for line in section.splitlines():
        ints = aoc.ints(line)
        if len(ints) > 0:
            ranges.append(ints)
    maps.append(ranges)

m = None

def solve(seed_start, seed_len, stage):
    if stage == 7:
        return seed_start

    min_dist = None
    for dest, source, length in maps[stage]:
        l = max(seed_start, source)
        r = min(seed_start+seed_len-1, source+length-1)
        if l > r:
            continue

        delta = l - source

        dist = solve(dest+delta, r-l-1, stage+1)
        if min_dist is None or dist is not None and dist < min_dist:
            min_dist = dist

    if min_dist is None:
        return solve(seed_start, seed_len, stage+1)

    return min_dist

result = None

for seed_start, seed_len in seed_ranges:
    dist = solve(seed_start, seed_len, 0)
    if result is None or dist<result:
        result = dist

print(result)
