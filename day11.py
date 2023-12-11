


def expand_universe(universe, size):
    i = 0
    while i < len(universe):
        universe[i] = list(universe[i])
        if "#" not in universe[i]:
            for k in range(size):
                universe.insert(i, ['.'] * len(universe[i]))
            i += size

        i += 1

    j = 0
    while j < len(universe[0]):
        if "#" not in (row[j] for row in universe):
            for k in range(size):
                for line in universe:
                    line.insert(j, ".")
            j += size

        j += 1

    return universe


def print_universe(universe):
    f = open("data/debug", "w")
    for i in range(0, len(universe)):
        for j in range(0, len(universe[i])):
            f.write(universe[i][j])
        f.write("\n")

    f.close()

def find_galaxy(universe):
    galaxies = []

    for i in range(0, len(universe)):
        for j in range(0, len(universe[i])):
            if universe[i][j] == '#':
                galaxies.append((i, j))

    return galaxies

def compute_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def part1(file_name):
    file = open(file_name, "r")
    content = file.read()

    universe = expand_universe(content.split("\n"), 1)

    galaxies = find_galaxy(universe)

    res = 0

    for i in range(0, len(galaxies)-1):
        distances = map(lambda g: compute_distance(g, galaxies[i]), galaxies[i+1:])
        res += sum(distances)

    return res


def find_empty_rows(universe):
    empty_rows = set()
    for i in range(len(universe)):
        if "#" not in universe[i]:
            empty_rows.add(i)

    return empty_rows

def find_empty_columns(universe):
    empty_columns = set()
    for j in range(len(universe[0])):
        if "#" not in (row[j] for row in universe):
            empty_columns.add(j)

    return empty_columns


def compute_expanded_distance(g1, g2, empty_rows, empty_columns):
    expanded_rows = set(range(min(g1[0], g2[0]), max(g1[0], g2[0]))).intersection(empty_rows)
    expanded_columns = set(range(min(g1[1], g2[1]), max(g1[1], g2[1]))).intersection(empty_columns)

    return abs(g1[0] - g2[0]) + len(expanded_rows) * 999999 + abs(g1[1] - g2[1]) + len(expanded_columns) * 999999

def part2(file_name):
    file = open(file_name, "r")
    content = file.read()
    universe = content.split("\n")

    galaxies = find_galaxy(universe)
    empty_columns = find_empty_columns(universe)
    empty_rows = find_empty_rows(universe)

    res = 0

    for i in range(0, len(galaxies) - 1):
        distances = map(lambda g: compute_expanded_distance(g, galaxies[i], empty_rows, empty_columns), galaxies[i + 1:])
        res += sum(distances)

    return res

