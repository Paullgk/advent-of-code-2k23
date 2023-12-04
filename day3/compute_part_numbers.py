#!/usr/bin/python3
import re

def search_adjacent_char(extracted_lines, index_char, index_line,
column_size, line_size):
# Return adjacent char in a list
    char_matrix = ['','','','','','','','']

    if (index_char < column_size): # Char on direct right
        char_matrix[0] = extracted_lines[index_line][index_char+1]

        if (index_line > 0): # Char on direct top right
            char_matrix[1] = extracted_lines[index_line-1][index_char+1]

        if (index_line < line_size): # Char on direct bot right
            char_matrix[2] = extracted_lines[index_line+1][index_char+1]

    if (index_char > 0): # Char on direct left
        char_matrix[3] = extracted_lines[index_line][index_char-1]

        if (index_line > 0): # Char on direct top left and top
            char_matrix[4] = extracted_lines[index_line-1][index_char-1]

        if (index_line < line_size): # Char on direct bot left
            char_matrix[5] = extracted_lines[index_line+1][index_char-1]

    if (index_line < line_size): # Char on direct bot
        char_matrix[6] = extracted_lines[index_line+1][index_char]

    if (index_line > 0): # Char on direct top
        char_matrix[7] = extracted_lines[index_line-1][index_char]

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
