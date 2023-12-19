def add_columns_at_end(dig_plan, n):
    for i in range(n):
        for line in dig_plan:
            line.append('.')


def add_columns_at_begin(dig_plan, n):
    for i in range(n):
        for line in dig_plan:
            line.insert(0, '.')


def add_lines_at_end(dig_plan, n):
    for i in range(n):
        dig_plan.append(['.' for i in range(len(dig_plan[0]))])


def add_lines_at_begin(dig_plan, n):
    for i in range(n):
        dig_plan.insert(0, ['.' for i in range(len(dig_plan[0]))])


def draw(dig_plan, i, j, length, direction):
    if direction == 'R':
        if j + length >= len(dig_plan[i]):
            add_columns_at_end(dig_plan, j + length - len(dig_plan[i]))
        for k in range(length):
            dig_plan[i][j + k] = '#'
        return i, j + (length - 1)

    elif direction == 'L':
        if j + 1 - length < 0:
            add_columns_at_begin(dig_plan, length - (j + 1))
            j += length - (j + 1)
        for k in range(length):
            dig_plan[i][j - k] = '#'
        return i, j - (length - 1)

    elif direction == 'U':
        if i + 1 - length < 0:
            add_lines_at_begin(dig_plan, length - (i + 1))
            i += length - (i + 1)
        for k in range(length):
            dig_plan[i - k][j] = '#'
        return i - (length - 1), j

    elif direction == 'D':
        if i + length >= len(dig_plan):
            add_lines_at_end(dig_plan, i + length - len(dig_plan))
        for k in range(length):
            dig_plan[i + k][j] = '#'
        return i + (length - 1), j


def print_dig_plan(dig_plan):
    f = open("data/debug", "w")
    for i in range(0, len(dig_plan)):
        for j in range(0, len(dig_plan[i])):
            f.write(dig_plan[i][j])
        f.write("\n")

    f.close()


def compute_out_neighbors(plan, i, j):
    neighbors = set()
    if i > 0:
        if plan[i - 1][j] != '#':
            neighbors.add((i - 1, j))
    if i < len(plan) - 1:
        if plan[i + 1][j] != '#':
            neighbors.add((i + 1, j))
    if j > 0:
        if plan[i][j - 1] != '#':
            neighbors.add((i, j - 1))
    if j < len(plan[i]) - 1:
        if plan[i][j + 1] != '#':
            neighbors.add((i, j + 1))

    return neighbors


def compute_out_points(dig_plan):
    out_points = set()
    new_neighbors = {(0, 0)}
    while len(new_neighbors) != 0:
        computed_neighbors = set()
        for new_neighbor in new_neighbors:
            computed_neighbors = computed_neighbors.union(compute_out_neighbors(dig_plan, *new_neighbor))

        out_points = out_points.union(new_neighbors)
        new_neighbors = computed_neighbors.difference(out_points)

    return len(out_points)


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    trenches = content.split("\n")

    dig_plan = [['.']]
    current_point = (0, 0)

    for trench in trenches:
        data = trench.split(' ')
        length = int(data[1]) + 1
        direction = data[0]
        current_point = draw(dig_plan, *current_point, length, direction)

    print_dig_plan(dig_plan)

    add_lines_at_begin(dig_plan, 1)
    add_lines_at_end(dig_plan, 1)
    add_columns_at_begin(dig_plan, 1)
    add_columns_at_end(dig_plan, 1)

    return len(dig_plan) * len(dig_plan[0]) - compute_out_points(dig_plan)


def convert_direction(direction):
    if direction == '0':
        return 'R'
    elif direction == '1':
        return 'D'
    elif direction == '2':
        return 'L'
    else:
        return 'U'


exterior_rotation = [('R','D'), ('D', 'L'), ('L', 'U'), ('U', 'R')]

def update_current_position(position, length, direction, next_direction, vertices):
    i,j = position

    if (direction, next_direction) in exterior_rotation:
        vertices_increase = length + 1
        vertices_decrease = length
    else:
        vertices_increase = length
        vertices_decrease = length - 1

    if direction == 'R':
        vertices.append((vertices[-1][0], j + vertices_increase))
        return i, j + length
    elif direction == 'L':
        vertices.append((vertices[-1][0], j - vertices_decrease))
        return i, j - length
    elif direction == 'U':
        vertices.append((i - vertices_decrease, vertices[-1][1]))
        return i - length, j

    elif direction == 'D':
        vertices.append((i + vertices_increase, vertices[-1][1]))
        return i + length, j


def shoelace_formula(vertices):
    n = len(vertices)
    area = 0

    for i in range(n - 1):
        area += vertices[i][0] * vertices[i + 1][1]
        area -= vertices[i + 1][0] * vertices[i][1]

    area += vertices[n - 1][0] * vertices[0][1]
    area -= vertices[0][0] * vertices[n - 1][1]

    area = abs(area) // 2

    return area


def part3(file_name):
    file = open(file_name, "r")
    content = file.read()
    trenches = content.split("\n")

    current_position = (0, 0)
    vertices = [(0, 0)] # depend on first and last directions


    for i in range(len(trenches) - 1):
        data = trenches[i].split('#')[1]
        length = int(data[:5], 16)
        direction = convert_direction(data[5])
        next_direction = convert_direction(trenches[i + 1].split('#')[1][5])

        current_position = update_current_position(current_position, length, direction, next_direction, vertices)
        print(current_position)

    print(vertices)

    return shoelace_formula(vertices)


