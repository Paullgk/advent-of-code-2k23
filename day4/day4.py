#!/usr/bin/python3

import re

def compute_winning_numbers(winning_numbers, numbers_you_have):
    # Convert number into int
    int_winning_numbers = re.findall(r'\d+', winning_numbers)
    int_numbers_you_have = re.findall(r'\d+', numbers_you_have)
    score = 0

    for number in int_winning_numbers:
        if number in int_numbers_you_have:
            
            if score == 0:
                score += 1
            elif score > 0: # Second match
                score *= 2
    return score

with open('day4/data/data1', 'r') as f:
    read_data = f.read()
extracted_cards = read_data.split("\n") # Extract each line

# -- PART 1 --
index = 0
total_score = 0
for card in extracted_cards:
    numbers = card.split(':')[1]
    winning_numbers = numbers.split('|')[0]
    numbers_you_have = numbers.split('|')[1]

    score = compute_winning_numbers(winning_numbers, numbers_you_have)
    total_score = score + total_score
    index += 1
print(f"Total score for part 1 is {total_score}")