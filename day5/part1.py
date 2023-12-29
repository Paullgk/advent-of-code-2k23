import re

class Part1:

    def __init__(self, seeds, extracted_lines):
        # Extract data
        self.index_seed_to_soil = extracted_lines.index('seed-to-soil map:')
        self.index_soil_to_fertilizer = extracted_lines.index('soil-to-fertilizer map:')
        self.index_fertilizer_to_water = extracted_lines.index('fertilizer-to-water map:')
        self.index_water_to_light = extracted_lines.index('water-to-light map:')
        self.index_light_to_temperature = extracted_lines.index('light-to-temperature map:')
        self.index_temperature_to_humidity = extracted_lines.index('temperature-to-humidity map:')
        self.index_humidity_to_location = extracted_lines.index('humidity-to-location map:')


        self.seed_to_soil = extracted_lines[self.index_seed_to_soil+1:self.index_soil_to_fertilizer-1]
        self.soil_to_fertilizer = extracted_lines[self.index_soil_to_fertilizer+1:self.index_fertilizer_to_water-1]
        self.fertilizer_to_water = extracted_lines[self.index_fertilizer_to_water+1:self.index_water_to_light-1]
        self.water_to_light = extracted_lines[self.index_water_to_light+1:self.index_light_to_temperature-1]
        self.light_to_temperature = extracted_lines[self.index_light_to_temperature+1:self.index_temperature_to_humidity-1]
        self.temperature_to_humidity = extracted_lines[self.index_temperature_to_humidity+1:self.index_humidity_to_location-1]
        self.humidity_to_location = extracted_lines[self.index_humidity_to_location+1:-1]

        self.seed_to_soil = self.convert_str_to_int(self.seed_to_soil)
        self.soil_to_fertilizer = self.convert_str_to_int(self.soil_to_fertilizer)
        self.fertilizer_to_water = self.convert_str_to_int(self.fertilizer_to_water)
        self.water_to_light = self.convert_str_to_int(self.water_to_light)
        self.light_to_temperature = self.convert_str_to_int(self.light_to_temperature)
        self.temperature_to_humidity = self.convert_str_to_int(self.temperature_to_humidity)
        self.humidity_to_location = self.convert_str_to_int(self.humidity_to_location)

    def convert_str_to_int(self, list):
        for line in range(0, len(list)):
            list[line] = seeds = re.findall(r'\d+', list[line])
        return list

    def compute_number(self, seed, soil_map):
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

    def compute_location(self, initial_seed):
        soil = self.compute_number(int(initial_seed), self.seed_to_soil)
        fertilizer = self.compute_number(soil, self.soil_to_fertilizer)
        water = self.compute_number(fertilizer, self.fertilizer_to_water)
        light = self.compute_number(water, self.water_to_light)
        temperature = self.compute_number(light, self.light_to_temperature)
        humidity = self.compute_number(temperature, self.temperature_to_humidity)
        location = self.compute_number(humidity, self.humidity_to_location)

        return location
