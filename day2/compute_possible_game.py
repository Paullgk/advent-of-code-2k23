#!/usr/bin/python3

def check_bag(bag, input_line):

    if input_line == '':
        return 0
    cubes = [0,0,0] # RGB format
    input_line = input_line.replace(' ', '')
    game_id = input_line.split(':')[0]
    game_id = int(game_id.replace("Game",""))
    game_content = input_line.split(':')[1]
    game_content = game_content.split(';')

    for set in game_content:
        # Retrieve each number of cubes of the set
        for color in set.split(','):
            if color.find('red') != -1:
                    red_cubes = color.split('red')[0]
                    cubes[0] = int(red_cubes)

            elif color.find('green') != -1:
                green_cubes = color.split('green')[0]
                cubes[1] = int(green_cubes)

            elif color.find('blue') != -1:
                blue_cubes = color.split('blue')[0]
                cubes[2] = int(blue_cubes)

        index = 0
        for cube in cubes:
            if cube > bag[index]:
                return 0
            index+=1
        cubes = [0,0,0]
    return game_id


bag = [12,13,14] # RGB format

with open('day2/data/data1', 'r') as f:
    read_data = f.read()
extracted_lines = read_data.split("\n") # Extract each line

sum = 0
for line in extracted_lines:
    game_id = check_bag(bag, line)
    sum = sum + game_id
print(f"Total sum is {sum}")
