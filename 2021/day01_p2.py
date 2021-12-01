import requests
import os.path
import config

input_url = 'https://adventofcode.com/2021/day/1/input'
data_file = 'data/day01_p2'

if not os.path.exists(data_file):
    cookies = dict(session=config.session_cookie)
    r = requests.get(input_url, cookies=cookies)
    with open(data_file, 'w+') as file:
        file.write(r.text)

with open(data_file, 'r') as file:
    count = 0
    lines = [int(line) for line in file]
    for line_no, line in enumerate(lines):
        if line_no > len(lines) - 4:
            break
        sweep_a = sum(lines[line_no: line_no + 3])
        sweep_b = sum(lines[line_no + 1: line_no + 4])
        if sweep_b > sweep_a:
            count += 1
print(count)
