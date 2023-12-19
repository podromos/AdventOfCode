import copy
import itertools


class Rule:
    def __init__(self, line):
        data = line.split('{')
        self.name = data[0]
        self.conditions = []
        conditions = data[1][:-1].split(',')
        for condition in conditions[:-1]:
            data = condition.split(':')
            attr = data[0][0]
            comparator = data[0][1]
            value = int(data[0][2:])
            next_rule = data[1]
            self.conditions.append((attr, comparator, value, next_rule))


        self.else_rule = conditions[-1]


    def process_part(self, part):
        for condition in self.conditions:
            if condition[0] == 'x':
                if condition[1] == '<' and part.x < condition[2]:
                    return condition[3]
                elif condition[1] == '>' and part.x > condition[2]:
                    return condition[3]
            elif condition[0] == 'm':
                if condition[1] == '<' and part.m < condition[2]:
                    return condition[3]
                elif condition[1] == '>' and part.m > condition[2]:
                    return condition[3]
            elif condition[0] == 'a':
                if condition[1] == '<' and part.a < condition[2]:
                    return condition[3]
                elif condition[1] == '>' and part.a > condition[2]:
                    return condition[3]
            else: #s
                if condition[1] == '<' and part.s < condition[2]:
                    return condition[3]
                elif condition[1] == '>' and part.s > condition[2]:
                    return condition[3]

        return self.else_rule

    def process_part_range(self, part_range):
        output = []
        current_part = part_range
        for condition in self.conditions:
            if condition[0] == 'x':
                if condition[1] == '<':
                    if current_part.x[0] < condition[2] <= current_part.x[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.x = [current_part.x[0], condition[2]-1]
                        output.append((part_computed, condition[3]))
                        current_part.x = [condition[2], current_part.x[1]]
                    elif current_part.x[1] < condition[2]:
                        output.append((current_part, condition[3]))
                        break

                elif condition[1] == '>':
                    if current_part.x[0] <= condition[2] < current_part.x[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.x = [condition[2]+1, current_part.x[1]]
                        output.append((part_computed, condition[3]))
                        current_part.x = [current_part.x[0], condition[2]]
                    elif current_part.x[1] > condition[2]:
                        output.append((current_part, condition[3]))
                        return output

            elif condition[0] == 'm':
                if condition[1] == '<':
                    if current_part.m[0] < condition[2] <= current_part.m[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.m = [current_part.m[0], condition[2] - 1]
                        output.append((part_computed, condition[3]))
                        current_part.m = [condition[2], current_part.m[1]]
                    elif current_part.m[1] < condition[2]:
                        output.append((current_part, condition[3]))
                        break

                elif condition[1] == '>':
                    if current_part.m[0] <= condition[2] < current_part.m[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.m = [condition[2] + 1, current_part.m[1]]
                        output.append((part_computed, condition[3]))
                        current_part.m = [current_part.m[0], condition[2]]
                    elif current_part.m[1] > condition[2]:
                        output.append((current_part, condition[3]))
                        return output

            elif condition[0] == 'a':
                if condition[1] == '<':
                    if current_part.a[0] < condition[2] <= current_part.a[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.a = [current_part.a[0], condition[2] - 1]
                        output.append((part_computed, condition[3]))
                        current_part.a = [condition[2], current_part.a[1]]
                    elif current_part.a[1] < condition[2]:
                        output.append((current_part, condition[3]))
                        break

                elif condition[1] == '>':
                    if current_part.a[0] <= condition[2] < current_part.a[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.a = [condition[2] + 1, current_part.a[1]]
                        output.append((part_computed, condition[3]))
                        current_part.a = [current_part.a[0], condition[2]]
                    elif current_part.a[1] > condition[2]:
                        output.append((current_part, condition[3]))
                        return output
            else: #s
                if condition[1] == '<':
                    if current_part.s[0] < condition[2] <= current_part.s[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.s = [current_part.s[0], condition[2] - 1]
                        output.append((part_computed, condition[3]))
                        current_part.s = [condition[2], current_part.s[1]]
                    elif current_part.s[1] < condition[2]:
                        output.append((current_part, condition[3]))
                        break

                elif condition[1] == '>' :
                    if current_part.s[0] <= condition[2] < current_part.s[1]:
                        part_computed = copy.copy(current_part)
                        part_computed.s = [condition[2] + 1, current_part.s[1]]
                        output.append((part_computed, condition[3]))
                        current_part.s = [current_part.s[0], condition[2]]
                    elif current_part.s[1] > condition[2]:
                        output.append((current_part, condition[3]))
                        return output

        output.append((current_part, self.else_rule))
        return output

class PartRange():
    def __init__(self):
        self.x = [1, 4000]
        self.m = [1, 4000]
        self.a = [1, 4000]
        self.s = [1, 4000]

    def compute(self):
        return (self.x[1] - self.x[0] + 1) * (self.m[1] - self.m[0] + 1) * (self.a[1] - self.a[0] + 1) * (self.s[1] - self.s[0] + 1)


class Part:
    def __init__(self, line):
        data = line[1:-1].split(',')
        self.x = int(data[0].split('=')[1])
        self.m = int(data[1].split('=')[1])
        self.a = int(data[2].split('=')[1])
        self.s = int(data[3].split('=')[1])

    def isAccepted(self, rules):
        rule = "in"
        while rule not in ('R', 'A'):
            rule = rules[rule].process_part(self)

        return rule == 'A'


def part1(file_name):
    file = open(file_name, "r")
    content = file.read()
    data = content.split("\n\n")

    rules_str = data[0].split('\n')
    rules = {}
    for rule_str in rules_str:
        rule = Rule(rule_str)
        rules[rule.name] = rule

    parts_str = data[1].split('\n')
    sum = 0
    for part_str in parts_str:
        part = Part(part_str)
        if part.isAccepted(rules):
           sum += part.x + part.a + part.m + part.s


    return sum

def part2(file_name):
    file = open(file_name, "r")
    content = file.read()
    data = content.split("\n\n")

    rules_str = data[0].split('\n')
    rules = {}
    for rule_str in rules_str:
        rule = Rule(rule_str)
        rules[rule.name] = rule

    part_range = PartRange()

    sum = 0
    ranges_computed = [(part_range, 'in')]
    while len(ranges_computed) > 0:
        ranges_computed = list(itertools.chain.from_iterable(map(lambda rc: rules[rc[1]].process_part_range(rc[0]), ranges_computed)))

        k = 0
        while k < len(ranges_computed):
            if ranges_computed[k][1] == 'A':
                sum += ranges_computed[k][0].compute()
                ranges_computed.pop(k)
            elif ranges_computed[k][1] == 'R':
                ranges_computed.pop(k)
            else:
                k+=1


    return sum

