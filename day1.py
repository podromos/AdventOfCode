import string
import sys


def part1(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    sum = 0

    for line in lines:
        digits_found = []

        for char in line:
            if char in string.digits:
                digits_found.append(char)

        sum += 10 * int(digits_found[0]) + int(digits_found[-1])

    return sum


digit_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def find_first_digit(line):
    first_digit = None
    first_digit_index = sys.maxsize

    for key in digit_map.keys():
        index = line.find(key)
        if -1 < index < first_digit_index:
            first_digit_index = index
            first_digit = digit_map[key]

    return first_digit


def find_last_digit(line):
    last_digit = None
    last_digit_index = -1

    for key in digit_map.keys():
        index = line.rfind(key)
        if index > last_digit_index:
            last_digit_index = index
            last_digit = digit_map[key]

    return last_digit


def part2(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    sum = 0

    for line in lines:
        sum += find_first_digit(line) * 10 + find_last_digit(line)

    return sum