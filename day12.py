

def list_equal(l1, l2):
    if(len(l1) != len(l2)):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True

class Record:
    def __init__(self, line):
        content = line.split(" ")
        self.groups = list(map(int, content[1].split(",")))
        self.record = list(content[0])
        self.unkown_count = self.record.count("?")


    def count_possible_arrangement(self):
        count = 0
        for i in range(pow(2, self.unkown_count)):
            j = 0
            arrangement = []
            for s in self.record:
                if s != "?":
                    arrangement.append(s)
                else:
                    if i & (1 << j) > 0:
                        arrangement.append(".")
                    else:
                        arrangement.append("#")
                    j += 1

            if self.is_possible(arrangement):
                count += 1

        return count

    def is_possible(self, arrangement):
        blocks = []
        current_count = 0
        for spring in arrangement:
            if spring == '#':
                current_count += 1
            elif current_count > 0:
                blocks.append(current_count)
                current_count = 0

        if current_count > 0:
            blocks.append(current_count)


        return list_equal(blocks, self.groups)




def part1(file_name):
    file = open(file_name, "r")
    lines = file.read().split("\n")

    count = 0
    for line in lines :
        record = Record(line)
        count += record.count_possible_arrangement()

    return count



class Record2:
    def __init__(self, line):
        content = line.split(" ")
        self.groups = list(map(int, content[1].split(",")))*5
        self.record = list(content[0])
        self.record += (["?"] + self.record)*4
        self.computed = {}

    def compute_possible(self, record, groups):
        if len(groups) == 0:
            if all(s != "#" for s in record):
                return 1
            else:
                return 0
        else:
            group = groups[0]
            count = 0
            j = 0
            while j + group - 1 < len(record):
                if all(s != "." for s in record[j:j + group]):
                    if j + group < len(record):
                        if record[j + group] != "#":
                            s = ''.join(record[j + group + 1:]) + ''.join(str(x) for x in groups[1:])
                            if not s in self.computed:
                                tmp = self.compute_possible(record[j + group + 1:], groups[1:])
                                self.computed[s] = tmp
                                count += tmp
                            else:
                                count += self.computed[s]
                    elif len(groups) == 1:
                        count += 1

                if record[j] == "#":
                    break
                j += 1

            return count


def part2(file_name):
    file = open(file_name, "r")
    lines = file.read().split("\n")

    count = 0

    for i in range(len(lines)):
        record = Record2(lines[i])
        count += record.compute_possible(record.record, record.groups)
        print(i)

    return count