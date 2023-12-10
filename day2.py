import numpy as np


class RevealedSet:
    def __init__(self, string):
        self.red = 0
        self.blue = 0
        self.green = 0

        ball_counts_str = string.split(',')
        for ball_count_str in ball_counts_str:
            red_index = ball_count_str.find("red")
            if red_index > -1:
                self.red = int(ball_count_str[0: red_index])
                continue

            blue_index = ball_count_str.find("blue")
            if blue_index > -1:
                self.blue = int(ball_count_str[0: blue_index])
                continue

            green_index = ball_count_str.find("green")
            if green_index > -1:
                self.green = int(ball_count_str[0: green_index])
                continue

    def is_possible(self, red, green, blue):
        return self.red <= red and self.green <= green and self.blue <= blue


class Game:
    def __init__(self, string):
        game_str, revealed_sets_str = string.split(":")

        self.id = int(game_str.split(" ")[1])
        self.revealed_sets = list(map(RevealedSet, revealed_sets_str.split(';')))

    def is_possible(self, red, green, blue):
        for revealed_set in self.revealed_sets:
            if not revealed_set.is_possible(red, green, blue):
                return False

        return True

    def min_possible(self):
        max_red = 0
        max_green = 0
        max_blue = 0

        for revealed_set in self.revealed_sets:
            max_red = max(revealed_set.red, max_red)
            max_green = max(revealed_set.green, max_green)
            max_blue = max(revealed_set.blue, max_blue)

        return max_red, max_green, max_blue


def part1(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    sum = 0

    for line in lines:
        game = Game(line)
        if game.is_possible(12, 13, 14):
            sum += game.id

    return sum


def part2(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    sum = 0

    for line in lines:
        game = Game(line)
        sum += np.prod(game.min_possible())

    return sum
