import aoc

st = open(0).read().strip()

result = 0

for line in st.splitlines():
    history = [aoc.ints(line)]
    while any(item != 0 for item in history[-1]):
        last = history[-1]
        differences = []
        
        for l, r in zip(last, last[1:]):
            differences.append(r-l)

        history.append(differences)

    for i in range(len(history) - 1, -1, -1):
        extrapolated = history[i][0]
        if i != len(history) - 1:
            extrapolated -= history[i+1][0]

        history[i].insert(0, extrapolated)

    result += history[0][0]


print(result)
