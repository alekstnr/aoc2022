import copy
from collections import deque
import re

def read_stacks(in_stacks, stack_names):
    """
    Reads unparsed stacks and returns a list of deque stack objects for each input stack.
    :param in_stacks: unparsed input stacks from input file.
    :param stack_names: stack names.
    :return: list of deque objects.
    """
    # Split up into boxes, 3 char sep by space, empty is valid
    split_stacks = [re.findall("....?", line) for line in in_stacks]
    trim_stacks = [[box[1] for box in line] for line in split_stacks]
    # Transpose the lists
    t_stacks = [list(stack) for stack in zip(*trim_stacks)]
    # Fix orientation and remove empty boxes (in place
    for line in t_stacks:
        line.reverse()
        line[:] = [box for box in line if box != " "]

    return [deque(line) for line in t_stacks]


def read_commands(raw_commands):
    # Extract numbers
    commands = [[int(num) for num in line.split() if num.isdigit()] for line in raw_commands]

    return commands


def move(stacks, amt, source, dest):
    # Perform amt number of operations
    for idx in range(amt):
        stacks[dest-1].append(stacks[source-1].pop())

def new_move(stacks, amt, source, dest):
    stacks[dest-1].extend(reversed([stacks[source-1].pop() for idx in range(amt)]))

def operate(stacks, commands):
    for line in commands:
        move(stacks, line[0], line[1], line[2])

def new_operate(stacks, commands):
    for line in commands:
        new_move(stacks, line[0], line[1], line[2])

def get_top_box(stacks):
    top_boxes = "".join([stack.pop() for stack in stacks])
    return top_boxes

if __name__ == '__main__':
    with open("input5", "r") as in_file:
        all_lines = in_file.readlines()
        # pad stacks to correct length
        in_stacks = [line.strip("\n").ljust(35, " ") for line in all_lines[:8]]
        stack_names = [line.strip("\n") for line in all_lines[8]]
        stack_names = [name for name in stack_names if not ((name != " ") ^ (name != ""))]
        commands = [line.strip("\n") for line in all_lines[10:]]

    stacks = read_stacks(in_stacks, stack_names)
    stacks2 = copy.deepcopy(stacks)
    command_list = read_commands(commands)

    operate(stacks, command_list)
    new_operate(stacks2, command_list)

    print(get_top_box(stacks))
    print(get_top_box(stacks2))
