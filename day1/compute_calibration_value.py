#!/usr/bin/python3

# Solutions for both parts of day 1 of AOC 2023. Make sure you put your data in data folder.

import re

def extract_digit(input_line):
    list_numbers = re.findall(r'\d+', input_line)

    if list_numbers != []:
        begin = list_numbers[0]
        end = list_numbers[-1]
        digit = []

        if begin.isdigit():
            digit.append(begin[0])

        if end.isdigit():
            digit.append(end[-1])

        final_digit = digit[0] + digit[-1]
        return final_digit
    return 0

def extract_digit_letters(input_line):
    digit_letters_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    list_numbers = []
    digit_letter = ''

    for char in input_line:
        digit_letter = digit_letter + char # Building each digit word
        
        if char.isdigit(): # If it is a real digit
            list_numbers.append(char)
            digit_letter = ''

        for key in digit_letters_dict:
            position = digit_letter.find(key) # Lets find if our built word is in the dict
            if position != -1: # If so, get position of the word and insert it in result list
                digit_letter = digit_letter[position:]
                list_numbers.append(digit_letters_dict[key])
                digit_letter = digit_letter[-1] # To cover the case of "eightree", grab previous letter
    return list_numbers


with open('day1/data/data1', 'r') as f:
    read_data = f.read()
extracted_lines = read_data.split("\n") # Extract each line 

digit = 0
sum = 0

# First part
for line in extracted_lines: # For each line, extract number 
    digit = extract_digit(line)
    sum = sum + int(digit)

print(f'Total sum for first part is {sum}')

digit = 0
sum = 0

# Second part
for line in extracted_lines: # For each line, extract number 
    digit = extract_digit_letters(line)
    begin = str(digit[0])
    end = str(digit[-1])

    digit = begin + end
    sum = sum + int(digit)
print(f'Total sum for second part is {sum}') 
