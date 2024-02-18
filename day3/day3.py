bags_in = open("input3", "r").read().split("\n")

sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")


def find_dupe(bag):
    front_set = set(bag[:len(bag)//2])
    back_set = set(bag[len(bag)//2:])

    inter = front_set & back_set
    return inter.pop()


def find_badge(group_bags):
    group_sets = [set(bag) for bag in group_bags]

    inter = group_sets[0] & group_sets[1] & group_sets[2]

    return inter.pop()


def get_priority(char):
    if char.isupper():
        priority = ord(char) - 38
    else:
        priority = ord(char) - 96
    return priority


def main_one(bags):
    prio_sum = 0
    for bag in bags:
        prio_sum += get_priority(find_dupe(bag))

    return prio_sum

def main_two(bags):
    prio_sum = 0
    for i in range(0, len(bags), 3):
        badge = find_badge([bags[i], bags[i+1], bags[i+2]])
        prio_sum += get_priority(badge)

    return prio_sum


if __name__ == '__main__':
    print(main_one(bags_in))
    print(main_two(bags_in))
