import string

import numpy


def compute_number_len(lines, i, j):
    length = 0
    while j < len(lines[i]):
        if lines[i][j] in string.digits:
            length += 1
        else:
            break
        j += 1
    return length


def compute_part_value(lines, i, j):
    length = compute_number_len(lines, i, j)
    compute_part = 0

    left = j > 0
    right = (j + length) < len(lines[i])
    up = i > 0
    down = i < len(lines) - 1

    if left:
        left_bound = j - 1
    else:
        left_bound = j

    if right:
        right_bound = j + length + 1
    else:
        right_bound = j + length

    if left:
        if not lines[i][j - 1] in string.digits and lines[i][j - 1] != '.':
            compute_part = int(lines[i][j:j + length])

    if right:
        if not lines[i][j + length] in string.digits and lines[i][j + length] != '.':
            compute_part = int(lines[i][j:j + length])

    if up:
        for k in range(left_bound, right_bound):
            if not lines[i - 1][k] in string.digits and lines[i - 1][k] != '.':
                compute_part = int(lines[i][j:j + length])
                break

    if down:
        for k in range(left_bound, right_bound):
            if not lines[i + 1][k] in string.digits and lines[i + 1][k] != '.':
                compute_part = int(lines[i][j:j + length])
                break

    return length, compute_part


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")

    sum = 0

    for i in range(0, len(lines)):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] in string.digits:
                length, part_value = compute_part_value(lines, i, j)
                sum += part_value
                j += length
            else:
                j += 1

    return sum


def compute_part_number(lines, i, j):
    while j >= 0 and lines[i][j] in string.digits:
        j -= 1
    j = j + 1

    length = compute_number_len(lines, i, j)

    return int(lines[i][j: j + length])


def compute_gear_ratio(lines, i, j):
    left = j > 0
    right = (j + 1) < len(lines[i])
    up = i > 0
    down = (i + 1) < len(lines)

    adjacent_number = []
    if left and lines[i][j - 1] in string.digits:
        adjacent_number.append(compute_part_number(lines, i, j - 1))

    if right and lines[i][j + 1] in string.digits:
        adjacent_number.append(compute_part_number(lines, i, j + 1))

    if up:
        if lines[i - 1][j] in string.digits:
            adjacent_number.append(compute_part_number(lines, i - 1, j))
        else:
            if left and lines[i - 1][j - 1] in string.digits:
                adjacent_number.append(compute_part_number(lines, i - 1, j - 1))
            if right and lines[i - 1][j + 1] in string.digits:
                adjacent_number.append(compute_part_number(lines, i - 1, j + 1))
    if down:
        if lines[i + 1][j] in string.digits:
            adjacent_number.append(compute_part_number(lines, i + 1, j))
        else:
            if left and lines[i + 1][j - 1] in string.digits:
                adjacent_number.append(compute_part_number(lines, i + 1, j - 1))
            if right and lines[i + 1][j + 1] in string.digits:
                adjacent_number.append(compute_part_number(lines, i + 1, j + 1))

    if len(adjacent_number) == 2:
        return numpy.prod(adjacent_number)
    else:
        return 0


def part2(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")

    sum = 0

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == '*':
                sum += compute_gear_ratio(lines, i, j)

    return sum
