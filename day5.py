from functools import partial

max_int = 9223372036854775807 // 2


class Map:
    def __init__(self, map_str):
        lines = map_str.split("\n")
        self.name = lines[0]
        self.ranges = []
        for line in lines[1:]:
            numbers_str = line.split(" ")
            self.ranges.append((int(numbers_str[1]), int(numbers_str[0]), int(numbers_str[2])))

        self.ranges.sort(key=lambda r: r[0])

        if self.ranges[0][0] > 0:
            self.ranges = [(0, 0, self.ranges[0][0])] + self.ranges

        i = 1
        while i < len(self.ranges) - 1:
            if self.ranges[i][0] + self.ranges[i][2] < self.ranges[i + 1][0]:
                self.ranges.insert(i + 1, (self.ranges[i][0] + self.ranges[i][2],
                                           self.ranges[i][0] + self.ranges[i][2],
                                           self.ranges[i + 1][0] - (self.ranges[i][0] + self.ranges[i][2])))
                i += 2
            else:
                i += 1

        self.ranges.append((self.ranges[-1][0] + self.ranges[-1][2],
                                           self.ranges[-1][0] + self.ranges[i][2],
                                           max_int - (self.ranges[-1][0] + self.ranges[-1][2])))


    def convert_value(self, val):
        i = 0
        while i < len(self.ranges):
            if val < self.ranges[i][0]:
                return val
            elif self.ranges[i][0] <= val < self.ranges[i][0] + self.ranges[i][2]:
                return val - self.ranges[i][0] + self.ranges[i][1]
            else:
                i += 1

        return val

    def convert_value_to_index(self, val):
        idx = 0
        while val >= self.ranges[idx][0] + self.ranges[idx][2] and idx < len(self.ranges):
            idx += 1

        return idx, val - self.ranges[idx][0]

    def convert_range(self, _range):

        start = _range[0]
        offset = _range[1]

        start_idx, start_offset = self.convert_value_to_index(start)
        stop_idx, stop_offset = self.convert_value_to_index(start + offset)

        output_ranges = []

        if start_idx == stop_idx:
            output_ranges.append((self.ranges[start_idx][1] + start_offset, stop_offset - start_offset))
        else:
            output_ranges.append((self.ranges[start_idx][1] + start_offset, self.ranges[start_idx][2] - start_offset))

            for i in range(start_idx+1, stop_idx):
                output_ranges.append((self.ranges[i][1], self.ranges[i][2]))

            output_ranges.append((self.ranges[stop_idx][1], stop_offset))

        return output_ranges


def compute_location_from_map(maps, seed):
    location = seed
    for _map in maps:
        location = _map.convert_value(location)
    return location


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()

    map_str = content.split("\n\n")
    maps = list(map(Map, map_str[1:]))

    seeds_str = map_str[0].split(": ")[1].split(" ")
    seeds = list(map(int, seeds_str))

    compute_location = partial(compute_location_from_map, maps)

    return min(list(map(compute_location, seeds)))


def part2(file_name):
    file = open(file_name, "r")
    content = file.read()

    map_str = content.split("\n\n")
    maps = list(map(Map, map_str[1:]))

    seeds_str = map_str[0].split(": ")[1].split(" ")
    seeds_ranges = list(map(int, seeds_str))

    compute_location = partial(compute_location_from_map, maps)

    min_location = None

    for i in range(0, len(seeds_ranges) // 2):
        ranges = [(seeds_ranges[2 * i], seeds_ranges[2 * i + 1])]
        for _map in maps:
            tmp_ranges = []
            for _range in ranges:
                tmp_ranges += _map.convert_range(_range)
            ranges = tmp_ranges

        min_for_seed = min(map(lambda r : r[0], ranges))
        if min_location is None or min_for_seed < min_location :
            min_location = min_for_seed



    return min_location
