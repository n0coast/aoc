import data

input_url = 'https://adventofcode.com/2021/day/1/input'
data_file = 'data/day01_p1'

data.get_data(data_file, input_url)

with open(data_file, 'r') as file:
    count, line_no = 0, 0
    lines = [int(line) for line in file]
    while line_no + 1 < len(lines):
        if lines[line_no] < lines[line_no + 1]:
            count += 1
        line_no += 1
    print(count)
