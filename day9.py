
class History:
    def __init__(self, line):
        self.values = list(map(int, line.split(" ")))

    def next(self):

        diffs = [self.values]

        while not all(d == 0 for d in diffs[-1]):
            diff = []
            for i in range(0, len(diffs[-1]) - 1):
                diff.append(diffs[-1][i+1] - diffs[-1][i])

            diffs.append(diff)

        diffs[-1].append(0)
        for i in range(len(diffs)-2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i+1][-1])

        return diffs[0][-1]

    def prev(self):
        diffs = [self.values]

        while not all(d == 0 for d in diffs[-1]):
            diff = []
            for i in range(0, len(diffs[-1]) - 1):
                diff.append(diffs[-1][i + 1] - diffs[-1][i])

            diffs.append(diff)

        diffs[-1].insert(0, 0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

        return diffs[0][0]


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()

    lines = content.split("\n")

    sum = 0

    for line in lines:
        history = History(line)
        sum += history.next()

    return sum

def part2(file_name):
    file = open(file_name, "r")
    content = file.read()

    lines = content.split("\n")

    sum = 0

    for line in lines:
        history = History(line)
        sum += history.prev()

    return sum