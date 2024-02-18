input_list = [item.strip("\n").split(" ") for item in open("input2", "r").readlines()]
print(input_list)
win_dict = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
draw_dict = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
loss_dict = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

mstr_dict = {
    "win": win_dict,
    "draw": draw_dict,
    "loss": loss_dict
}

score_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
# do different dictionaries for win/draw/loss and score.

def part_one(input, mstr_dict, score_dict):
    score = 0
    for pair in input:
        score += 6 * (mstr_dict["win"][pair[0]] == pair[1]) + 3 * (mstr_dict["draw"][pair[0]] == pair[1])
        score += score_dict[pair[1]]

    return score

def part_two(input, mstr_dict, score_dict):
    action_dict = {
        "X": "loss",
        "Y": "draw",
        "Z": "win"
    }
    score = 0
    for pair in input:
        action = action_dict[pair[1]]
        pick_dict = mstr_dict[action]
        pick = pick_dict[pair[0]]
        score += score_dict[pick]

        score += 6 * (mstr_dict["win"][pair[0]] == pick) + 3 * (mstr_dict["draw"][pair[0]] == pick)

    return score

if __name__ == "__main__":
    print(part_one(input_list, mstr_dict, score_dict))
    print(part_two(input_list, mstr_dict, score_dict))

