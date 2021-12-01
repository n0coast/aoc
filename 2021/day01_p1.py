import requests
import os.path
import config

input_url = 'https://adventofcode.com/2021/day/1/input'
data_file = '2021/data/day01_p1'

if not os.path.exists(data_file):
    cookies = dict(session=config.session_cookie)
    r = requests.get(input_url, cookies=cookies)
    with open(data_file, 'w+') as file:
        file.write(r.text)

with open(data_file, 'r') as file:
    count, line_no = 0, 0
    lines = [int(line) for line in file]
    while line_no + 1 < len(lines):
        if lines[line_no] < lines[line_no + 1]:
            count += 1
        line_no += 1
    print(count)
