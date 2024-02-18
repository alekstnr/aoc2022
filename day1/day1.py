import numpy as np

# This is disgusting, please ignore.

input = open("input1", "r")

# silly part 1
# def silly_one(input1):
#     max = np.max(np.array([np.sum(np.array(list(map(int, sublist.split("\n"))))) for sublist in input1.read().split("\n\n")]))
#
#     return max

# part 1

def one(input):
    outer_arr = np.array(input.read().split("\n\n"))
    inner_arr = [list(map(int, inv.split("\n"))) for inv in outer_arr]
    sum_arr = [np.sum(inner) for inner in inner_arr]
    sort_arr = np.sort(sum_arr)
    print(sort_arr[-3:])
    max_3 = np.sum(sort_arr[-3:])
    print(max_3)

    maxer = np.max(sum_arr)

    return maxer

# part 2

def two(input):
    outer_arr = np.array(input.read().split("\n\n"))
    inner_arr = [list(map(int, inv.split("\n"))) for inv in outer_arr]
    sum_arr = [np.sum(inner) for inner in inner_arr]

    #print(sort_arr)

    max_3 = np.sum(sort_arr)

    return max_3


if __name__ == "__main__":
    print(one(input))
    #print(two(input1))

