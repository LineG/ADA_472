import numpy as np
from typing import List
import copy


# 1 --> black side
# 0 --> white side

# used to sort the list
def first_white_token_count(board: np.array) -> int:
    flat_board = [arr for arr in board.tolist()]
    count = 0
    for token in flat_board:
        if token == 0:
            count += 1
        if token == 1:
            break
    return count
    pass


# performs a median-of-three quicksort on the child nodes given, orders them by amount of white tokens in the
def sort_children(children: List[np.array], low: int, high: int) -> None:
    pivot = find_median_pivot(low, high, children)
    left_point = low
    right_point = high

    while left_point <= right_point:
        while first_white_token_count(children[left_point]) > first_white_token_count(children[pivot]):
            left_point += 1

        while first_white_token_count(children[right_point]) < first_white_token_count(children[pivot]):
            right_point -= 1

        if left_point <= right_point:
            children[left_point], children[right_point] = children[right_point], children[left_point]
            left_point += 1
            right_point -= 1

    if low < right_point:
        sort_children(children, low, right_point)

    if high > left_point:
        sort_children(children, left_point, high)
    pass


def find_median_pivot(low: int, high: int, children: List[np.array]) -> int:
    first = children[low]
    last = children[high]
    middle = children[int((high + low) / 2)]

    median = [first, middle, last]

    if first_white_token_count(median[0]) > first_white_token_count(median[1]):
        median[0], median[1] = median[1], median[0]

    if first_white_token_count(median[1]) > first_white_token_count(median[2]):
        median[1], median[2] = median[2], median[1]

    if first_white_token_count(median[0]) > first_white_token_count(median[1]):
        median[0], median[1] = median[1], median[0]

    pivot = 0
    for i in range(0, len(children)):
        if np.array_equiv(median[1], children[i]):
            pivot = i

    return pivot
    pass


def flip_adjacent(board: np.array, i: int, n: int) -> np.array:
    b_new = copy.copy(board)
    N = n * n
    # right
    i_r = i + 1
    if not i_r > N - 1:
        b_new[i_r] = not (board[i_r])
    # left
    i_l = i - 1
    if not i_l < 0:
        b_new[i_l] = not (board[i_l])
    # top
    i_t = i - n
    if not i_t < 0:
        b_new[i_t] = not (board[i_t])
    # down
    i_d = i + n
    if not i_d > N - 1:
        b_new[i_d] = not (board[i_d])

    return b_new


def generate_graph(board: np.array, max_d: int, n: int) -> List[np.array]:
    graph = {}
    board = [board]

    for d in range(max_d - 1):
        c = 0
        for b in board:
            children = []
            if not c == 0:
                children = generate_next_moves(b, n)
                board = board + children
            else:
                children = generate_next_moves(b, n)
                board = children
            c = c + len(children)
            graph[str(b).strip('[]')] = children
    return graph


def generate_next_moves(b: np.array, n: int) -> List[np.array]:
    next_moves = []
    N = n * n
    # row
    for i in range(N):
        # make a shallow copy
        b_new = copy.copy(b)
        # flip the center piece
        b_new[i] = not (b_new[i])
        # flip adjacent
        b_new = flip_adjacent(b_new, i, n)
        next_moves.append(b_new)
    # return a list
    return next_moves


if __name__ == "__main__":
    b1 = np.array([1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    c1 = generate_next_moves(b1, 4)
    print('initial array\n' + str(c1))
    sort_children(c1, 0, len(c1) - 1)
    print("sorted array")
    print(c1)
    # b2 = [1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0]
    # b3 = [0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1]
    # b4 = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # board_list = [b1, b2, b3, b4]
    # print('nodes before sorting\n' + board_list.__str__())
    # sort_children(board_list, 0, len(board_list)-1)
    # print('nodes after sorting\n' + board_list.__str__())
