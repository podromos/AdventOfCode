WEST = 0
EAST = 1
NORTH = 2
SOUTH = 3
OTHER = 4

import sys


def compute_next_cities1(plan, i, j, direction, straight_line, cost):
    next_cities = []

    if i > 0 and direction != SOUTH and not (direction == NORTH and straight_line == 3):
        if direction == NORTH:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i - 1, j, NORTH, new_straight_line), cost + plan[i - 1][j]))

    if i + 1 < len(plan) and direction != NORTH and not (direction == SOUTH and straight_line == 3):
        if direction == SOUTH:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i + 1, j, SOUTH, new_straight_line), cost + plan[i + 1][j]))

    if j > 0 and direction != EAST and not (direction == WEST and straight_line == 3):
        if direction == WEST:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i, j - 1, WEST, new_straight_line), cost + plan[i][j - 1]))

    if j + 1 < len(plan[0]) and direction != WEST and not (direction == EAST and straight_line == 3):
        if direction == EAST:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i, j + 1, EAST, new_straight_line), cost + plan[i][j + 1]))

    return next_cities

def destination_cost(plan, next_cities):
    destination = len(plan) - 1, len(plan[0]) - 1

    for k in next_cities.keys():
        if k[0:2] == destination:
            return next_cities[k]

    return -1


def min_cost_city(next_cities):
    min_key = None
    min_val = sys.maxsize

    for key, val in next_cities.items():
        if val < min_val:
            min_val = val
            min_key = key

    return min_key, min_val


def merge_cities(next_cities, computed_cities, computed_next_cities):
    for computed_city in computed_next_cities:
        if computed_city[0] not in computed_cities:
            if computed_city[0] in next_cities:
                next_cities[computed_city[0]] = min(computed_city[1], next_cities[computed_city[0]])
            else:
                next_cities[computed_city[0]] = computed_city[1]


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()

    plan = list(map(lambda line: list(map(int, line)), content.split("\n")))

    next_cities = {(0, 0, OTHER, 0): 0}
    computed_cities = set()

    while destination_cost(plan, next_cities) == -1:
        city, cost = min_cost_city(next_cities)
        print(cost)
        computed_cities.add(city)
        next_cities.pop(city)

        merge_cities(next_cities, computed_cities, compute_next_cities1(plan, *city, cost))

    return destination_cost(plan, next_cities)

def destination_cost2(plan, next_cities):
    destination = len(plan) - 1, len(plan[0]) - 1

    for k in next_cities.keys():
        if k[0:2] == destination and k[3] >= 4:
            return next_cities[k]

    return -1

def compute_next_cities2(plan, i, j, direction, straight_line, cost):
    next_cities = []

    if (i > 0 and direction != SOUTH
            and not (direction == NORTH and straight_line == 10)
            and not (direction in (WEST, EAST) and straight_line < 4)):
        if direction == NORTH:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i - 1, j, NORTH, new_straight_line), cost + plan[i - 1][j]))

    if (i + 1 < len(plan) and direction != NORTH
            and not (direction == SOUTH and straight_line == 10)
            and not (direction in (WEST, EAST) and straight_line < 4)):
        if direction == SOUTH:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i + 1, j, SOUTH, new_straight_line), cost + plan[i + 1][j]))

    if (j > 0 and direction != EAST
            and not (direction == WEST and straight_line == 10)
            and not (direction in (SOUTH, NORTH) and straight_line < 4)):
        if direction == WEST:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i, j - 1, WEST, new_straight_line), cost + plan[i][j - 1]))

    if (j + 1 < len(plan[0]) and direction != WEST
            and not (direction == EAST and straight_line == 10)
            and not (direction in (SOUTH, NORTH) and straight_line < 4)):
        if direction == EAST:
            new_straight_line = straight_line + 1
        else:
            new_straight_line = 1
        next_cities.append(((i, j + 1, EAST, new_straight_line), cost + plan[i][j + 1]))


    return next_cities


def part2(file_name):
    file = open(file_name, "r")
    content = file.read()

    plan = list(map(lambda line: list(map(int, line)), content.split("\n")))

    next_cities = {(0, 0, EAST, 1): 0, (0, 0, SOUTH, 1): 0}
    computed_cities = set()

    while destination_cost2(plan, next_cities) == -1:
        city, cost = min_cost_city(next_cities)
        print(cost)

        computed_cities.add(city)
        next_cities.pop(city)

        merge_cities(next_cities, computed_cities, compute_next_cities2(plan, *city, cost))

    return destination_cost(plan, next_cities)
