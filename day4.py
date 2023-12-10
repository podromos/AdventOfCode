class Card:
    def __init__(self, line):
        card_numbers = line.split(":")[1]
        numbers = card_numbers.split("|")

        winning_number_str = list(filter(lambda n: n != "", numbers[1].split(' ')))
        obtained_number_str = list(filter(lambda n: n != "", numbers[0].split(' ')))

        self.winning_number = list(map(int, winning_number_str))
        self.obtained_number = list(map(int, obtained_number_str))

    def compute_matching_numbers(self):
        matching_numbers = 0

        for n in self.obtained_number:
            if n in self.winning_number:
                matching_numbers += 1

        return matching_numbers

    def compute_point(self):
        matching_numbers = self.compute_matching_numbers()

        if matching_numbers > 0:
            return pow(2, matching_numbers - 1)
        else:
            return 0


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")

    sum = 0

    for line in lines:
        sum += Card(line).compute_point()

    return sum


def part2(file_name):
    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")

    copy = [0] * len(lines)

    for i in range(0, len(lines)):
        copy[i] += 1
        matching_numbers = Card(lines[i]).compute_matching_numbers()
        for j in range(1, matching_numbers + 1):
            copy[i + j] += copy[i]

    return sum(copy)
