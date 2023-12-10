SOUTH = 1
NORTH = 2
EAST = 3
WEST = 4


def find_start(plan):
    for i in range(0, len(plan)):
        for j in range(0, len(plan[i])):
            if plan[i][j] == "S":
                return i, j


def find_first_pipe(plan, i, j):
    if j + 1 < len(plan[i]) and plan[i][j + 1] in ('-', '7', 'J'):
        return i, j + 1, WEST
    elif j - 1 >= 0 and plan[i][j - 1] in ('-', 'F', 'L'):
        return i, j - 1, EAST
    elif i + 1 < len(plan) and plan[i + 1][j] in ('|', 'J', 'L'):
        return i + 1, j, NORTH
    elif i - 1 >= 0 and plan[i - 1][j] in ('|', 'F', '7'):
        return i - 1, j, SOUTH


def next(plan, i, j, direction_in):
    if plan[i][j] == "-":
        if direction_in == WEST:
            return i, j + 1, WEST
        else:
            return i, j - 1, EAST
    elif plan[i][j] == "|":
        if direction_in == NORTH:
            return i + 1, j, NORTH
        else:
            return i - 1, j, SOUTH
    elif plan[i][j] == "L":
        if direction_in == NORTH:
            return i, j + 1, WEST
        else:
            return i - 1, j, SOUTH
    elif plan[i][j] == "J":
        if direction_in == NORTH:
            return i, j - 1, EAST
        else:
            return i - 1, j, SOUTH
    elif plan[i][j] == "7":
        if direction_in == SOUTH:
            return i, j - 1, EAST
        else:
            return i + 1, j, NORTH
    elif plan[i][j] == "F":
        if direction_in == SOUTH:
            return i, j + 1, WEST
        else:
            return i + 1, j, NORTH


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()

    plan = content.split("\n")

    count = 1
    i, j, direction_in = find_first_pipe(plan, *find_start(plan))

    while plan[i][j] != "S":
        i, j, direction_in = next(plan, i, j, direction_in)
        count += 1

    return count // 2


def compute_out_neighbors(plan, i, j):
    neighbors = set()
    if i > 0:
        if plan[i - 1][j] != 'X':
            neighbors.add((i - 1, j))
    if i < len(plan) - 1:
        if plan[i + 1][j] != 'X':
            neighbors.add((i + 1, j))
    if j > 0:
        if plan[i][j - 1] != 'X':
            neighbors.add((i, j - 1))
    if j < len(plan[i]) - 1:
        if plan[i][j + 1] != 'X':
            neighbors.add((i, j + 1))

    return neighbors


def print_points(plan, out_points):
    f = open("data/debug", "w")

    for i in range(0, len(plan)):
        for j in range(0, len(plan[i])):
            if (i, j) in out_points:
                f.write("+")
            else:
                f.write(plan[i][j])
        f.write("\n")
    f.close()


def print_plan(plan):
    f = open("data/debug", "w")
    for i in range(0, len(plan)):
        for j in range(0, len(plan[i])):
            f.write(plan[i][j])
        f.write("\n")

    f.close()


def reformat(plan, pipes):
    # add additional lines and columns
    for i in range(0, len(plan)):
        plan[i] = list(plan[i])
        for j in range(0, len(plan[i])):
            plan[i].insert(j * 2, '.')
        plan[i].append('.')

    for i in range(0, len(plan)):
        plan.insert(i * 2, ['.'] * len(plan[0]))
    plan.append(['.'] * len(plan[0]))

    # recompute pipes positions
    pipes = list(map(lambda p: (p[0] * 2 + 1, p[1] * 2 + 1, p[2]), pipes))

    # replace all loop pipes by X
    for k in range(0, len(pipes)):
        i, j, direction_in = pipes[k]
        if direction_in == EAST:
            plan[i][j + 1] = 'X'
        elif direction_in == WEST:
            plan[i][j - 1] = 'X'
        elif direction_in == NORTH:
            plan[i - 1][j] = 'X'
        elif direction_in == SOUTH:
            plan[i + 1][j] = 'X'
        plan[i][j] = 'X'

    # replace unused pipes by .
    for i in range(0, len(plan)):
        plan[i] = list(map(lambda p: p if p == 'X' else '.', plan[i]))

    return plan


def part2(file_name):
    file = open(file_name, "r")
    content = file.read()

    plan = content.split("\n")
    real_points_count = len(plan) * len(plan[0])

    pipes = []

    i, j, direction_in = find_first_pipe(plan, *find_start(plan))
    pipes.append((i, j, direction_in))

    while plan[i][j] != "S":
        i, j, direction_in = next(plan, i, j, direction_in)
        pipes.append((i, j, direction_in))

    plan = reformat(plan, pipes)

    out_points = set()
    new_neighbors = {(0, 0)}

    while len(new_neighbors) != 0:
        computed_neighbors = set()
        for new_neighbor in new_neighbors:
            computed_neighbors = computed_neighbors.union(compute_out_neighbors(plan, *new_neighbor))

        out_points = out_points.union(new_neighbors)
        new_neighbors = computed_neighbors.difference(out_points)

    real_out_points = list((i, j) for (i, j) in out_points if i % 2 == 1 and j % 2 == 1)

    return real_points_count - len(pipes) - len(real_out_points)
