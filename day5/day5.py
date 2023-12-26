#!/usr/bin/python3

import re

with open('day5/data/data2', 'r') as f:
    read_data = f.read()
extracted_lines = read_data.split("\n") # Extract each line

seeds = extracted_lines[0].split(":")[1] # Seeds are always on 1st line
seeds = re.findall(r'\d+', seeds)# Convert to int

def convert_str_to_int(list):
    for line in range(0, len(list)):
        list[line] = seeds = re.findall(r'\d+', list[line])
    return list

def compute_number(seed, soil_map):
    index = 0
    number = seed
    source = []
    destination = []
    range = []
    for map in soil_map:
        source.append(int(map[1]))
        destination.append(int(map[0]))
        range.append(int(map[2]))

    for each_source in source:
        if seed >= each_source and seed <= each_source + range[index]:
            diff = seed - each_source
            number = destination[index] + diff
            break
        index += 1
    return number

def compute_location(initial_seed):
    soil = compute_number(int(seed), seed_to_soil)
    fertilizer = compute_number(soil, soil_to_fertilizer)
    water = compute_number(fertilizer, fertilizer_to_water)
    light = compute_number(water, water_to_light)
    temperature = compute_number(light, light_to_temperature)
    humidity = compute_number(temperature, temperature_to_humidity)
    location = compute_number(humidity, humidity_to_location)

    return location


# Extract data
index_seed_to_soil = extracted_lines.index('seed-to-soil map:')
index_soil_to_fertilizer = extracted_lines.index('soil-to-fertilizer map:')
index_fertilizer_to_water = extracted_lines.index('fertilizer-to-water map:')
index_water_to_light = extracted_lines.index('water-to-light map:')
index_light_to_temperature = extracted_lines.index('light-to-temperature map:')
index_temperature_to_humidity = extracted_lines.index('temperature-to-humidity map:')
index_humidity_to_location = extracted_lines.index('humidity-to-location map:')

seed_to_soil = extracted_lines[index_seed_to_soil+1:index_soil_to_fertilizer-1]
soil_to_fertilizer = extracted_lines[index_soil_to_fertilizer+1:index_fertilizer_to_water-1]
fertilizer_to_water = extracted_lines[index_fertilizer_to_water+1:index_water_to_light-1]
water_to_light = extracted_lines[index_water_to_light+1:index_light_to_temperature-1]
light_to_temperature = extracted_lines[index_light_to_temperature+1:index_temperature_to_humidity-1]
temperature_to_humidity = extracted_lines[index_temperature_to_humidity+1:index_humidity_to_location-1]
humidity_to_location = extracted_lines[index_humidity_to_location+1:-1]

seed_to_soil = convert_str_to_int(seed_to_soil)
soil_to_fertilizer = convert_str_to_int(soil_to_fertilizer)
fertilizer_to_water = convert_str_to_int(fertilizer_to_water)
water_to_light = convert_str_to_int(water_to_light)
light_to_temperature = convert_str_to_int(light_to_temperature)
temperature_to_humidity = convert_str_to_int(temperature_to_humidity)
humidity_to_location = convert_str_to_int(humidity_to_location)

# -- PART 1 --
location_list = []

for seed in seeds:
    location = compute_location(seed)
    location_list.append(location)

location_list = sorted(location_list)

print(f"Lowest location for part 1 is {location_list[0]}")

# -- PART 2 --
location_list = []
for index_seed in range(0,len(seeds),2):
    initial_seed = int(seeds[index_seed])
    last_seed = int(seeds[index_seed+1])

    for seed in range(initial_seed,initial_seed+last_seed):
        location = compute_location(seed)

        # if len(location_list) > 0:
        #     if location-1 == location_list[-1:][0]:
        #         break
        location_list.append(location)

        print(f"Compute seed {seed}...")
    location_list = sorted(location_list)
    print(f"Lowest location for seed {initial_seed} is {location_list[0]} at seed {seed}")
    location_list = []
