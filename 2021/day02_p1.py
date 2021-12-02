import data

input_url = 'https://adventofcode.com/2021/day/2/input'
data_file = 'data/day02_p1'


def calculate_location(coord_gen):
    # store coordinates in a simple dictionary
    coord_dict = {'x': 0, 'y': 0}
    # submarine location mapped in 2d grid
    # 'forward' increases x
    # 'backward' decreases x
    # 'down' increases y
    # 'up' decreases y
    for directions in coord_gen:
        direction, amount = directions.split()
        if direction == 'forward':
            coord_dict['x'] += int(amount)
        elif direction == 'backward':
            coord_dict['x'] -= int(amount)
        elif direction == 'down':
            coord_dict['y'] += int(amount)
        elif direction == 'up':
            coord_dict['y'] -= int(amount)

    return coord_dict


# get input data if it doesn't yet exist
data.get_data(data_file, input_url)

# generator expression to get each row out of of data_file
coord_gen = (row for row in open(data_file))

coords = calculate_location(coord_gen)

print(f'Multiplied coordinates: {coords["x"] * coords["y"]}')

