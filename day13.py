


def check_vertical_reflection(lines, i):
    colomns_to_compare = min(i, len(lines[0]) - i )

    for line in lines:
        for j in range(colomns_to_compare):
            if line[i - j - 1] != line[i + j]:
                return False

    return True

def check_horizontal_reflection(lines, i):
    colomns_to_compare = min(i, len(lines) - i)

    for k in range(len(lines[0])):
        for j in range(colomns_to_compare):
            if lines[i - j - 1][k] != lines[i + j][k]:
                return False

    return True

def part1(file_name):
    file = open(file_name, "r")
    patterns = file.read().split("\n\n")

    sum = 0

    for pattern in patterns:
        found = False
        lines = pattern.split("\n")
        for i in range(1, len(lines)):
            if check_horizontal_reflection(lines, i):
                sum += i * 100
                found = True
                break

        if not found:
            for i in range(1, len(lines[0])):
                if check_vertical_reflection(lines, i):
                    sum += i
                    break

    return sum


def find_reflection(pattern, exclude):
    for i in range(1, len(pattern)):
        if check_horizontal_reflection(pattern, i) and i*100 != exclude:
            return i * 100

    for i in range(1, len(pattern[0])):
        if check_vertical_reflection(pattern, i) and i != exclude:
            return i

    return 0


def toggle_symbol(a):
    if a=='.':
        return '#'
    else :
        return '.'

class Pattern:
    def __init__(self, lines):
        self.pattern = []
        for line in lines:
            self.pattern.append(list(line))

    def find_reflection2(self):
        old_reflection = find_reflection(self.pattern, 0)

        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[0])):
                self.pattern[i][j] = toggle_symbol(self.pattern[i][j])

                reflection = find_reflection(self.pattern, old_reflection)
                if reflection != 0 and old_reflection != reflection:
                    return reflection

                self.pattern[i][j] = toggle_symbol(self.pattern[i][j])


def part2(file_name):
    file = open(file_name, "r")
    patterns = file.read().split("\n\n")

    sum = 0

    for pattern_str in patterns:
        pattern = Pattern(pattern_str.split('\n'))
        print(sum)
        sum += pattern.find_reflection2()

    return sum
