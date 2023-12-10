
class Node:
    def __init__(self, line):
        equal_split = line.split(" = (")

        self.id = equal_split[0]

        comma_split = equal_split[1].split(", ")
        self.left = comma_split[0]
        self.right = comma_split[1]

    def next(self, instruction):
        if instruction == "L":
            return self.left
        else:
            return self.right

def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    content = content.split("\n\n")

    instructions = content[0]
    lines = content[1].split(")\n")

    nodes = {}

    for line in lines:
        node = Node(line)
        nodes[node.id] = node

    count = 0
    current_node = nodes["AAA"]

    while True:
        for instruction in instructions:
            current_node = nodes[current_node.next(instruction)]
            count += 1

            if current_node.id == "ZZZ":
                return count


def find_loop(node, nodes, instructions):
    nodes_visited = {}

    znodes = []

    current_node = node

    it = 0

    while True:
        for i in range(0, len(instructions)):
            if current_node.id in nodes_visited:
                if (it - nodes_visited[current_node.id]) % len(instructions) == 0:
                    return it, (it - nodes_visited[current_node.id]) // len(instructions), znodes

            if current_node.id[2] == "Z":
                znodes.append(it)

            nodes_visited[current_node.id] = it
            current_node = nodes[current_node.next(instructions[i])]
            it += 1


def znodes(node, nodes, instructions):
    it = 0
    current_node = node

    while True:
        for instruction in instructions:
            current_node = nodes[current_node.next(instruction)]
            it += 1
            if current_node.id[2] == "Z":
                print(it)


def part2(file_name):

    file = open(file_name, "r")
    content = file.read()
    content = content.split("\n\n")

    instructions = content[0]
    lines = content[1].split(")\n")

    nodes = {}
    current_nodes = []

    for line in lines[:-1]:
        node = Node(line)
        nodes[node.id] = node
        if node.id[2] == 'A':
            current_nodes.append(node)


    loop = find_loop(current_nodes[4], nodes, instructions)
    znode = znodes(current_nodes[5], nodes, instructions)

    print(loop)
    return loop[0] - (loop[1] * len(instructions))

    count = 0

    while True:
        print(count)
        for instruction in instructions:
            current_nodes = list(map(lambda n : nodes[n.next(instruction)], current_nodes))
            count += 1
            # print(list(map(lambda n : n.id, current_nodes)))

            if all(n.id[2] == 'Z' for n in current_nodes):
                return count
