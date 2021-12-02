import data

input_url = 'https://adventofcode.com/2021/day/1/input'
data_file = 'data/day01_p2'

data.get_data(data_file, input_url)

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


