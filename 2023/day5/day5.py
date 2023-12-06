from __future__ import annotations
import time 
from dataclasses import dataclass

@dataclass
class SeedRange: 
    start: int 
    end: int 

    def calc_new_ranges(self, map: MapRange):
        new_ranges = []
        # left overlap 
        if (map.source_start <= self.start and map.source_end >= self.start and map.source_end < self.end): 
            new_ranges.append(SeedRange(map.destination(self.start), map.destination(map.source_end)))
            new_ranges.append(SeedRange(map.source_end + 1, self.end))
        # right overlap
        if (map.source_start > self.start and map.source_start <= self.end and map.source_end >= self.end): 
            new_ranges.append(SeedRange(self.start, map.source_start - 1))
            new_ranges.append(SeedRange(map.destination_start, map.destination(self.end)))
        # completely to destination 
        if (map.source_start <= self.start and map.source_end >= self.end): 
            new_ranges.append(SeedRange(map.destination(self.start), map.destination(self.end)))
        # fully contained
        if (map.source_start > self.start and map.source_end < self.end):
            new_ranges.append(SeedRange(self.start, map.source_start - 1))
            new_ranges.append(SeedRange(map.destination_start, map.destination_end))
            new_ranges.append(SeedRange(map.source_end + 1, self.end))
        return new_ranges
    
    def split_range(self, range_maps:list[MapRange]):
        if len(range_maps) == 0: return [self] 
        non_overlap_range = self
        found_ranges = []
        for i, range_map in enumerate(range_maps): 
            new_ranges = non_overlap_range.calc_new_ranges(range_map)
            if i >= len(range_maps) - 1: 
                found_ranges += new_ranges
            else: 
                found_ranges = found_ranges + new_ranges[:-1]
                non_overlap_range = new_ranges[-1]
        return found_ranges

@dataclass
class MapRange:
    source_cat: str
    source_start: int
    source_end: int 

    destination_cat: str
    destination_start: int 
    destination_end: int 
    
    maprange: int

    def destination(self, source) -> int: 
        return self.destination_start + (source - self.source_start)

    def overlap(self, seed_range: SeedRange) -> bool: 
        return not (self.source_end < seed_range.start or self.source_start > seed_range.end)

def get_input(): 
    with open('./2023/day5/input.txt') as f: 
        lines = f.readlines() 
        return lines 

def process_as_points(input): 
    lines = input 

    # process seeds 
    seeds = [int(number) for number in lines[0].strip().split(" ")[1: ]]

    # process category maps 
    maps = []
    mapping = []
    for line in lines[2:]: 
        # found newline so new category block found 
        if (line == '\n'): 
            maps.append(mapping.copy())
            mapping = [] 
        # found title line so save category (does nothing for now)
        elif (not line[0].isnumeric()): 
            cat_to = line.split(" ")[0].split("-")
            category = [cat_to[0], cat_to[2]]
        # numeric line with map ranges 
        else: 
            mapping.append([int(number) for number in line.strip().split(" ")])
    maps.append(mapping)
    return seeds, maps

def process_as_ranges(input): 
    lines = input 

    # process seeds 
    seeds = [int(number) for number in lines[0].strip().split(" ")[1: ]]
    seed_ranges = []
    for i in range(0,len(seeds), 2): 
        seed_ranges.append(SeedRange(seeds[i], (seeds[i] + (seeds[i+1] - 1))))
    
    # process category maps 
    category_maps = []
    category = ['', '']
    category_map = []
    for line in lines[2:]: 
        # found newline so new category block found 
        if (line == '\n'): 
            category_maps.append(category_map.copy())
            category_map = []
        # found title line so save category 
        elif (not line[0].isnumeric()): 
            cat_to = line.split(" ")[0].split("-")
            category = [cat_to[0], cat_to[2]]
        # numeric line with map ranges 
        else: 
            map_range = [int(number) for number in line.strip().split(' ')]
            category_map.append(MapRange(
                source_cat=category[0], 
                source_start=map_range[1], 
                source_end=map_range[1] + map_range[2] - 1, 
                destination_cat=category[1], 
                destination_start=map_range[0], 
                destination_end=map_range[0] + map_range[2] - 1, 
                maprange=map_range[2]
            ))
    #AHHHHHH dom dom dom dit vergeten... 
    category_maps.append(category_map.copy())

    # sort the maps by origin starting point 
    for i, category_map in enumerate(category_maps): 
        category_maps[i] = sorted(category_map, key=lambda cat_map: cat_map.source_start)
    return seed_ranges, category_maps

def part1(input): 
    seeds, maps = process_as_points(input)
    seed_map = [[seed] for seed in seeds]
    for field in maps: 
        checked = []
        for mapping in field: 
            destination = mapping[0]
            source = mapping[1]
            dist = mapping[2]
            for i, seed in enumerate(seed_map): 
                if i in checked: continue 
                last_seed = seed[-1]  
                if (last_seed >= source and last_seed < (source + dist)): 
                    new_seed = (last_seed - source) + destination
                    seed.append(new_seed)
                    checked.append(i)
    locations = []
    for seed in seed_map:
        locations.append(seed[-1])

    return min(locations)

def part2(input): 
    seed_ranges, category_maps = process_as_ranges(input)

    for category in category_maps: 
        new_seed_ranges = []
        for seed_range in seed_ranges: 
            overlap = []
            for map_range in category: 
                if map_range.overlap(seed_range): 
                    overlap.append(map_range)
            split_ranges = seed_range.split_range(overlap)
            new_seed_ranges = new_seed_ranges + split_ranges
        seed_ranges = new_seed_ranges.copy()
        
    small_seeds = [sr.start for sr in seed_ranges]
    return min(small_seeds) 

def main(): 
    input = get_input()
    time_start = time.time() 
    answer = part1(input)
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(input)
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
