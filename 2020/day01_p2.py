import requests
import os.path
import config
import itertools

input_url = 'https://adventofcode.com/2020/day/1/input'
data_file = 'data/day01_p1'

if not os.path.exists(data_file):
    cookies = dict(session=config.session_cookie)
    r = requests.get(input_url, cookies=cookies)
    with open(data_file, 'w+') as file:
        file.write(r.text)


def two_entries():
    with open(data_file, 'r') as file:
        lines = [int(line) for line in file]
        zipped_lines = list(itertools.product(lines, lines, lines))
        return (x * y * z for x, y, z in zipped_lines if (x + y + z) == 2020)


print(next(two_entries()))
