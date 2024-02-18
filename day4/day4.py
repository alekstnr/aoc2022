def parse_input(in_file):
    """
    Parses input file and returns a list of list of sets for all of the task numbers.
    :param in_file: input file name
    :return: list of list of sets of tasks
    """
    task_pairs = [line.strip("\n") for line in open(in_file, "r").readlines()]
    split_pairs = [pair.split(",") for pair in task_pairs]
    task_sets = [[expand_tasks(task_range) for task_range in pair] for pair in split_pairs]

    return task_sets


def expand_tasks(task_range):
    """
    Expands tasks and returns a set with all tasks
    :param task_range: task range as string
    :return: set with all tasks
    """
    start, stop = map(int, task_range.split("-"))

    return set(range(start, stop+1))

def find_encompass(in_list):
    count = 0
    for pair in in_list:
        # Will add one if one or the other are True.
        count += 1 * (pair[0].issubset(pair[1])) or (pair[1].issubset(pair[0]))

    return count

def find_overlaps(in_list):
    count = 0
    for pair in in_list:
        count += 1 * bool(pair[0] & pair[1])

    return count


def main_one(in_list):
    return find_encompass(in_list)


if __name__ == '__main__':
    print(main_one(parse_input("input4")))
    print("Part two: ", find_overlaps(parse_input("input4")))