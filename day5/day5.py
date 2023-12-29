#!/usr/bin/python3

import re
from part1 import Part1
from part2 import Part2



with open('day5/data/data2', 'r') as f:
    read_data = f.read()
extracted_lines = read_data.split("\n") # Extract each line

seeds = extracted_lines[0].split(":")[1] # Seeds are always on 1st line
seeds = re.findall(r'\d+', seeds)# Convert to int

part_1 = Part1(seeds, extracted_lines)
part_2 = Part2(seeds, extracted_lines)

# -- PART 1 --
location_list = []

for seed in seeds:
    location = part_1.compute_location(seed)
    location_list.append(location)

location_list = sorted(location_list)

print(f"Lowest location for part 1 is {location_list[0]}")

# -- PART 2 --
location_list = []
seed = 0
for index_seed in range(0,len(seeds),2):
    initial_seed = int(seeds[index_seed])
    last_seed = int(seeds[index_seed+1])
    max_seed = initial_seed+last_seed
    for seed in range(initial_seed,max_seed):
        location = part_2.compute_location(seed,max_seed)

        # if len(location_list) > 0:
        #     if location-1 == location_list[-1:][0]:
        #         break
        location_list.append(location)

        print(f"Compute seed {seed}...")
    location_list = sorted(location_list)
    print(f"Lowest location for seed {initial_seed} is {location_list[0]} at seed {seed}")
    location_list = []
