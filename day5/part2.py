from part1 import Part1

class Part2(Part1):
    pass

    def compute_location(self, initial_seed, max_seed):
        soil = self.compute_number(int(initial_seed), self.seed_to_soil)
        fertilizer = self.compute_number(soil, self.soil_to_fertilizer)
        water = self.compute_number(fertilizer, self.fertilizer_to_water)
        light = self.compute_number(water, self.water_to_light)
        temperature = self.compute_number(light, self.light_to_temperature)
        humidity = self.compute_number(temperature, self.temperature_to_humidity)
        location = self.compute_number(humidity, self.humidity_to_location)
        return location
