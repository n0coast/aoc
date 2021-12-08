import data
from statistics import mode, multimode
from collections import Counter

input_url = 'https://adventofcode.com/2021/day/3/input'
data_file = 'data/day03_p2'

data.get_data(data_file, input_url)


def get_common_bit(rows, position, most=True):
    bits = Counter([row[position] for row in rows])
    if most:
        if bits['0'] == bits['1']:
            return 1
        return Counter(bits).most_common()[0][0]
    else:
        if bits['0'] == bits['1']:
            return 0
        return Counter(bits).most_common()[-1][0]


def string_to_bin(bin):
    return int(bin, 2)


def get_rating(rows, most):
    row_length = len(rows[0])
    for i in range(row_length):
        bit = get_common_bit(rows, i, most)
        rows = [row for row in rows if row[i] == str(bit)]

    return rows


# list comprehension for all rows
rows = [row.strip() for row in open(data_file, 'r')]

oxygen_generator_rating = get_rating(rows, most=True)[0]
co2_scrubber_rating = get_rating(rows, most=False)[0]

oxygen_decimal = string_to_bin(oxygen_generator_rating)
co2_decimal = string_to_bin(co2_scrubber_rating)

print(f'Life support rating: {oxygen_decimal * co2_decimal}')