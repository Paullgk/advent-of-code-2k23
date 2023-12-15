#!/usr/bin/python3
import re

def search_adjacent_char(extracted_lines, index_char, index_line,
column_size, line_size):
# Return adjacent char in a list [TOP LEFT;TOP;TOP RIGHT;LEFT;RIGHT;BOT LEFT;BOT;BOT RIGHT]
    char_matrix = ['','','','','','','','']

    if (index_char < column_size-1): # Char on direct right
        char_matrix[4] = extracted_lines[index_line][index_char+1]

        if (index_line > 0): # Char on direct top right
            char_matrix[2] = extracted_lines[index_line-1][index_char+1]

        if (index_line < line_size): # Char on direct bot right
            char_matrix[7] = extracted_lines[index_line+1][index_char+1]

    if (index_char > 0): # Char on direct left
        char_matrix[3] = extracted_lines[index_line][index_char-1]

        if (index_line > 0): # Char on direct top left
            char_matrix[0] = extracted_lines[index_line-1][index_char-1]

        if (index_line < line_size): # Char on direct bot left
            char_matrix[5] = extracted_lines[index_line+1][index_char-1]

    if (index_line < line_size): # Char on direct bot
        char_matrix[6] = extracted_lines[index_line+1][index_char]

    if (index_line > 0): # Char on direct top
        char_matrix[1] = extracted_lines[index_line-1][index_char]

    return char_matrix



with open('day3/data/data1', 'r') as f:
    read_data = f.read()
extracted_lines = read_data.split("\n") # Extract each line

index_line = 0
index_char = 0
index_number = 0
line_size = len(extracted_lines[0]) - 1
column_size = len(extracted_lines) - 1
symbol_detected = False
number = ''
char_matrix = []
part_number_sum = 0

# -- PART 1 --
for line in extracted_lines:
    extracted_numbers =  re.findall(r'\d+', line)
    for char in line:

        if char.isdigit(): # For each digit, look around if a symbol is there
            number = number + char
            char_matrix = search_adjacent_char(extracted_lines, index_char, index_line, column_size, line_size)
            r = re.compile(r"[^\d.]")
            symbol_occurrence = list(filter(r.match, char_matrix))

            if symbol_occurrence != [] and symbol_detected != True: # For current number, check if already detected an adjacent symbol
                symbol_detected = True
            char_matrix = []
        else:
            if symbol_detected == True:
                part_number_sum = part_number_sum + int(number)
            number = ''
            symbol_detected = False

        index_char += 1

    index_char = 0
    index_line += 1

print(f"PART 1: Sum of all adjacent part number is {part_number_sum}")

# -- PART 2 --
def get_number(extracted_lines, index_line, index_char,direction):
    i = 2
    if direction == 0: # TOP LEFT
        top_line = extracted_lines[index_line-1]
        number_part = top_line[index_char-1:index_char]

        while top_line[index_char-i:index_char].isdigit():
            number_part = top_line[index_char-i:index_char]

            if index_char+i == len(top_line):
                break
            i+=1
    if direction == 2:  # TOP RIGHT
        top_line = extracted_lines[index_line-1]
        number_part = top_line[index_char+1:-1]
        while top_line[index_char+1:index_char+i].isdigit():
            number_part = top_line[index_char+1:index_char+i]

            if index_char+i == len(top_line):
                break
            i+=1

    if direction == 3:  # LEFT
        current_line = extracted_lines[index_line]
        number_part = current_line[index_char-1]
        while current_line[index_char-i:index_char].isdigit():
            number_part = current_line[index_char-i:index_char]

            if index_char+i == len(current_line):
                break
            i+=1

    if direction == 4:  # RIGHT
        current_line = extracted_lines[index_line]
        number_part = current_line[index_char]
        while current_line[index_char+1:index_char+i].isdigit():
            number_part = current_line[index_char+1:index_char+i]
            if index_char+i == len(current_line):
                break
            i+=1
        pass

    if direction == 5:  # BOTTOM LEFT
        bot_line = extracted_lines[index_line+1]
        number_part = bot_line[index_char-1:index_char]
        while bot_line[index_char-i:index_char].isdigit():
            number_part = bot_line[index_char-i:index_char]

            if index_char+i == len(bot_line):
                break
            i+=1
    if direction == 7:  # BOTTOM RIGHT
        bot_line = extracted_lines[index_line+1]
        number_part = bot_line[index_char+1:-1]
        while bot_line[index_char+1:index_char+i].isdigit():
            number_part = bot_line[index_char+1:index_char+i]

            if index_char+i == len(bot_line):
                break
            i+=1

    return number_part

def search_adjacent_number(extracted_lines, index_line, index_char, symbol, char_matrix): #[TOP LEFT;TOP;TOP RIGHT;LEFT;RIGHT;BOT LEFT;BOT;BOT RIGHT]
    pn_counter = 0
    number = ''
    adjacent_number = []
    limit_position = [0,2,3,4,5,7]

    for matrix_element in range(0,3):
        if char_matrix[matrix_element].isdigit():
            if matrix_element in limit_position:
                extracted_number = get_number(extracted_lines, index_line, index_char, matrix_element)

                if matrix_element == 0:
                    number = extracted_number + number
                if matrix_element == 2:
                    number = number + extracted_number

            else:
                number = number + char_matrix[matrix_element]
        elif number != '':
            adjacent_number.append(int(number))
            pn_counter += 1
            number = ''
    if number != '':
        adjacent_number.append(int(number))
        pn_counter += 1
        number = ''

    for matrix_element in range(3,5):
        if char_matrix[matrix_element].isdigit():
            if matrix_element in limit_position:
                extracted_number = get_number(extracted_lines, index_line, index_char, matrix_element)
                number = extracted_number + number
                adjacent_number.append(int(number))
                pn_counter += 1
                number = ''

    for matrix_element in range(5,8):
        if char_matrix[matrix_element].isdigit():
            if matrix_element in limit_position:
                extracted_number = get_number(extracted_lines, index_line, index_char, matrix_element)

                if matrix_element == 5:
                    number = extracted_number + number
                if matrix_element == 7:
                    number = number + extracted_number

            else:
                number = number + char_matrix[matrix_element]
        elif number != '':
            adjacent_number.append(int(number))
            pn_counter += 1
            number = ''
    if number != '':
        adjacent_number.append(int(number))
        pn_counter += 1
        number = ''
    if pn_counter == 2:
        return adjacent_number[0] * adjacent_number[1]
    else:
        return 0

symbol = ''
number = ''
index_char = 0
index_line = 0
part_number_sum = 0
result = 0
for line in extracted_lines:
    extracted_numbers =  re.findall(r'\d+', line)
    for char in line:
        char_matrix = search_adjacent_char(extracted_lines, index_char, index_line, column_size, line_size)
        symbol = re.findall(r"[^\d.]", char) # Searching if char is a symbol

        if symbol != []:
            result = search_adjacent_number(extracted_lines, index_line, index_char,symbol[0], char_matrix)
            part_number_sum = part_number_sum + result
        index_char += 1

    index_char = 0
    index_line += 1
print(f"PART 2: Sum of all adjacent part number is {part_number_sum}")
