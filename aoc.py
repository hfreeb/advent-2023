import requests
from pathlib import Path
import re
import sys

year = 2023

def get_cookies():
    session_key = Path('.session').read_text().strip()
    return { "session": session_key }

def get_input(day):
    r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=get_cookies())
    assert r.status_code == 200

    return r.text

def submit(day, level, answer):
    r = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', data={'level': level, 'answer': answer}, cookies=get_cookies())
    assert r.status_code == 200

    # Lets parse HTML with regex :)
    matches = re.findall(r'<article>.+</article>', r.text)
    assert len(matches) == 1

    print(matches[0])

def ints(s):
    if re.findall(r'\d-\d', s):
        print('Found str matching \\d-\\d:', s)
        sys.exit()
    return list(map(int, re.findall(r'-?\d+', s)))
