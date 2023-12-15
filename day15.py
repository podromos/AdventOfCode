
def compute_hash(str):
    hash = 0
    for c in str:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash


def part1(file_name):
    file = open(file_name, "r")
    steps = file.read().split(",")

    sum = 0

    for step in steps:
        sum += compute_hash(step)

    return sum

def part2(file_name):
    file = open(file_name, "r")
    steps = file.read().split(",")

    boxes = [[] for _ in range(256)]

    for step in steps:
        if step[-1] == '-':
            operation = '-'
            label = step[:-1]
            boxId = compute_hash(label)
            for i in range(len(boxes[boxId])):
                if boxes[boxId][i][0] == label:
                    boxes[boxId].pop(i)
                    break
        else:
            operation = '='
            label, length_str = step.split('=')
            length = int(length_str)
            boxId = compute_hash(label)
            label_found = False
            for i in range(len(boxes[boxId])):
                if boxes[boxId][i][0] == label:
                    boxes[boxId][i] = (label, length)
                    label_found = True

            if not label_found:
                boxes[boxId].append((label, length))


    sum = 0

    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            sum += (i+1) * (j+1) * boxes[i][j][1]


    return sum
