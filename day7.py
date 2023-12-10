

cards1 = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

cards2 = {
    "J": -1,
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "Q": 10,
    "K": 11,
    "A": 12,
}

hand_types = {
    "none": 0,
    "pair": 1,
    "dpair": 2,
    "three": 3,
    "full": 4,
    "four": 5,
    "five": 6,
}


def compute_type1(hand):
    max_count1 = 0
    max_count2 = 0

    for card in cards1.keys():
        count = hand.count(card)

        if count > max_count1:
            max_count2 = max_count1
            max_count1 = count
        elif count > max_count2:
            max_count2 = count

    if max_count1 == 5:
        return "five"
    if max_count1 == 4:
        return "four"
    if max_count1 == 3 and max_count2 == 2:
        return "full"
    if max_count1 == 3:
        return  "three"
    if max_count1 == 2 and max_count2 == 2:
        return "dpair"
    if max_count1 == 2:
        return "pair"

    return "none"

class Hand1:
    def __init__(self, line):
        data = line.split(" ")
        self.hand = data[0]
        self.bid = int(data[1])
        self.type = compute_type1(self.hand)
        self.key = (hand_types[self.type], cards1[self.hand[0]], cards1[self.hand[1]], cards1[self.hand[2]],
                    cards1[self.hand[3]], cards1[self.hand[4]])

def part1(file_name):

    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")

    hands = []

    for line in lines:
         hands.append(Hand1(line))

    hands.sort(key=lambda h: h.key)

    sum = 0
    for i in range(0,len(hands)):
        sum += (i+1) * hands[i].bid

    return sum

def compute_type2(hand):
    max_count1 = 0
    max_count2 = 0

    normal_keys = list(cards2.keys())
    normal_keys.remove("J")

    for card in normal_keys:
        count = hand.count(card)

        if count > max_count1:
            max_count2 = max_count1
            max_count1 = count
        elif count > max_count2:
            max_count2 = count

    jcount = hand.count("J")

    if jcount > 0:
        max_count1 = max_count1 + jcount

    if max_count1 == 5:
        return "five"
    if max_count1 == 4:
        return "four"
    if max_count1 == 3 and max_count2 == 2:
        return "full"
    if max_count1 == 3:
        return  "three"
    if max_count1 == 2 and max_count2 == 2:
        return "dpair"
    if max_count1 == 2:
        return "pair"

    return "none"

class Hand2:
    def __init__(self, line):
        data = line.split(" ")
        self.hand = data[0]
        self.bid = int(data[1])
        self.type = compute_type2(self.hand)
        self.key = (hand_types[self.type], cards2[self.hand[0]], cards2[self.hand[1]], cards2[self.hand[2]],
                    cards2[self.hand[3]], cards2[self.hand[4]])



def part2(file_name):

    file = open(file_name, "r")
    content = file.read()
    lines = content.split("\n")


    hands = []

    for line in lines:
         hands.append(Hand2(line))

    hands.sort(key=lambda h: h.key)

    sum = 0
    for i in range(0,len(hands)):
        sum += (i+1) * hands[i].bid

    return sum