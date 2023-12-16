import itertools

EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4


def move(contraption, i, j, direction):
    if direction == WEST:
        if j > 0:
            return [(i, j - 1, WEST)]
    elif direction == NORTH:
        if i > 0:
            return [(i - 1, j, NORTH)]
    elif direction == EAST:
        if j + 1 < len(contraption[0]):
            return [(i, j + 1, EAST)]
    elif direction == SOUTH:
        if i + 1 < len(contraption):
            return [(i + 1, j, SOUTH)]

    return []


def compute_beams(contraption, i, j, direction):
    beams = []

    if contraption[i][j] == '.':
        beams += move(contraption, i, j, direction)
    elif contraption[i][j] == '-':
        if direction in [EAST, WEST]:
            beams += move(contraption, i, j, direction)
        else:
            beams += move(contraption, i, j, EAST) + move(contraption, i, j, WEST)
    elif contraption[i][j] == '|':
        if direction in [SOUTH, NORTH]:
            beams += move(contraption, i, j, direction)
        else:
            beams += move(contraption, i, j, NORTH) + move(contraption, i, j, SOUTH)
    elif contraption[i][j] == '\\':
        if direction == NORTH:
            beams += move(contraption, i, j, WEST)
        elif direction == SOUTH:
            beams += move(contraption, i, j, EAST)
        elif direction == WEST:
            beams += move(contraption, i, j, NORTH)
        else:
            beams += move(contraption, i, j, SOUTH)
    else:
        if direction == NORTH:
            beams += move(contraption, i, j, EAST)
        elif direction == SOUTH:
            beams += move(contraption, i, j, WEST)
        elif direction == WEST:
            beams += move(contraption, i, j, SOUTH)
        else:
            beams += move(contraption, i, j, NORTH)

    return beams


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    contraption = content.split("\n")

    record = []
    starts = ([(i, 0, EAST) for i in range(len(contraption))] +
              [(i, len(contraption[0])-1, WEST) for i in range(len(contraption))] +
              [(0, j, SOUTH) for j in range(len(contraption[0]))] +
              [(len(contraption)-1, j, NORTH) for j in range(len(contraption[0]))])

    for start in starts:
        prev_energized_titles_len = 0
        energized_titles = {start}
        beams = {start}

        while len(energized_titles) > prev_energized_titles_len:
            beams = map(lambda p: compute_beams(contraption, *p), beams)
            beams = set(itertools.chain.from_iterable(beams))

            prev_energized_titles_len = len(energized_titles)
            beams = beams.difference(energized_titles)
            energized_titles = energized_titles.union(set(beams))

        record.append(len(set(map(lambda p: (p[0], p[1]), energized_titles))))
        print(start)

    return max(record)
