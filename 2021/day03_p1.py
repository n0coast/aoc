import data

input_url = 'https://adventofcode.com/2021/day/3/input'
data_file = 'data/day03_p1'

data.get_data(data_file, input_url)


def column_count(data_file):
    with open(data_file, 'r') as file:
        nums = []
        # generator for lines in the file
        rows = (str(row) for row in file)
        nums = [int(i) for i in next(rows).strip()]
        for row_count, row in enumerate(rows, start=1):
            for count, i in enumerate(row.strip()):
                nums[count] += int(i)

    return nums, row_count


def list_to_bin(nums, row_count):
    bin = ''
    for num in nums:
        if num / row_count > .5:
            bin += '1'
            continue
        bin += '0'
    return bin


def reverse_bin(bin):
    reversed_bin = ''
    for i in bin:
        if i == '1':
            reversed_bin += '0'
            continue
        reversed_bin += '1'
    return reversed_bin


def string_to_bin(bin):
    return int(bin, 2)

nums, row_count = column_count(data_file)
bin = list_to_bin(nums, row_count)
reversed_bin = reverse_bin(bin)
gamma = string_to_bin(bin)
epsilon = string_to_bin(reversed_bin)
print(f'gamma: {gamma}')
print(f'epsilon: {epsilon}')
print(f'power consumption: {gamma * epsilon}')
