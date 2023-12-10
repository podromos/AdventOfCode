
class Race:
    def __init__(self, time, distance):
        self.distance = distance
        self.time = time

    def count_ways_to_win(self):
        count = 0

        for t in range(0, self.time):
            if self.distance < t * (self.time - t):
                count += 1

        return count

def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")
    times_str = lines[0].split(": ")[1]
    distance_str = lines[1].split(": ")[1]

    times = list(map(int, filter(lambda n: n != "", times_str.split(' '))))
    distances = list(map(int, filter(lambda n: n != "", distance_str.split(' '))))

    prod = 1

    for i in range(0, len(times)):
        race = Race(times[i], distances[i])
        prod *= race.count_ways_to_win()

    return prod

def part2(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")
    times_str = lines[0].split(": ")[1]
    distance_str = lines[1].split(": ")[1]

    time = int(''.join(filter(lambda n: n != ' ', times_str)))
    distance = int(''.join((filter(lambda n: n != ' ', distance_str))))

    race = Race(time, distance)
    return race.count_ways_to_win()
