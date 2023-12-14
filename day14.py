class Platform:
    def __init__(self, lines):
        self.platform = []
        for line in lines:
            self.platform.append(list(line))

    def tilt_line_north(self, i):
        if i > 0:
            for k in range(len(self.platform[i])):
                if self.platform[i][k] == 'O' and self.platform[i - 1][k] == '.':
                    self.platform[i][k] = '.'
                    self.platform[i - 1][k] = 'O'

    def tilt_line_to_the_north(self, i):
        for k in range(i, 0, -1):
            self.tilt_line_north(k)

    def tilt_to_the_north(self):
        for i in range(len(self.platform)):
            self.tilt_line_to_the_north(i)

    def tilt_column_west(self, i):
        if i > 0:
            for k in range(len(self.platform)):
                if self.platform[k][i] == 'O' and self.platform[k][i - 1] == '.':
                    self.platform[k][i] = '.'
                    self.platform[k][i - 1] = 'O'

    def tilt_columns_to_the_west(self, i):
        for k in range(i, 0, -1):
            self.tilt_column_west(k)

    def tilt_to_the_west(self):
        for i in range(len(self.platform[0])):
            self.tilt_columns_to_the_west(i)


    def tilt_line_south(self, i):
        if i < len(self.platform) - 1:
            for k in range(len(self.platform[i])):
                if self.platform[i][k] == 'O' and self.platform[i + 1][k] == '.':
                    self.platform[i][k] = '.'
                    self.platform[i + 1][k] = 'O'

    def tilt_line_to_the_south(self, i):
        for k in range(i, len(self.platform)):
            self.tilt_line_south(k)

    def tilt_to_the_south(self):
        for i in range(len(self.platform) - 1, -1, -1):
            self.tilt_line_to_the_south(i)

    def tilt_column_east(self, i):
        if i < len(self.platform[0]) - 1:
            for k in range(len(self.platform)):
                if self.platform[k][i] == 'O' and self.platform[k][i + 1] == '.':
                    self.platform[k][i] = '.'
                    self.platform[k][i + 1] = 'O'

    def tilt_column_to_the_east(self, i):
        for k in range(i, len(self.platform[0])):
            self.tilt_column_east(k)

    def tilt_to_the_east(self):
        for i in range(len(self.platform[0]) - 1, -1, -1):
            self.tilt_column_to_the_east(i)

    def compute_load(self):
        sum = 0

        for i in range(len(self.platform)):
            for c in self.platform[i]:
                if c == 'O':
                    sum += len(self.platform) - i

        return sum

    def __hash__(self):
        return hash(str(self.platform))

    def rotate(self):
        self.tilt_to_the_north()
        self.tilt_to_the_west()
        self.tilt_to_the_south()
        self.tilt_to_the_east()

    def print(self):
        f = open("data/debug", "w")
        for i in range(0, len(self.platform)):
            for j in range(0, len((self.platform[i]))):
                f.write(self.platform[i][j])
            f.write("\n")

        f.close()


def part1(file_name):
    file = open(file_name, "r")
    lines = file.read().split("\n")

    platform = Platform(lines)

    # h0 = hash(platform)
    # platform.rotate()
    # h1 = hash(platform)
    # i = 0
    # while h1 != h0:
    #     print(i)
    #     i += 1
    #     h0 = h1
    #     platform.rotate()
    #     h1 = hash(platform)

    platform.rotate()
    hash_map = {}
    h = hash(platform)
    i = 1

    while not h in hash_map:
        hash_map[h] = (i, platform.compute_load())
        i += 1
        platform.rotate()
        h = hash(platform)

    start_cycle = hash_map[h][0]
    cycle_length = i - hash_map[h][0]


    billion_iteration = start_cycle + ((1000000000 - start_cycle) % cycle_length)

    for k, load in hash_map.values():
        if k == billion_iteration:
            return load

    return 0
