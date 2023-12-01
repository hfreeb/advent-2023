import aoc
from pathlib import Path

st = Path('day1.in').read_text()

result = 0

spelling = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
}

for line in st.splitlines():
    first = None
    last = None
    for i in range(len(line)):
        for k, v in spelling.items():
            if line[i:].startswith(k):
                if first is None:
                    first = v
                last = v

        char = line[i]
        if char.isdigit():
            if first is None:
                first = int(char)
            last = int(char)

    result += first * 10 + last

print(result)
