import numpy as np
from typing import List
import copy

# 1 --> black side
# 0 --> white side

#takes 2 boards and the size of the board
def white_at(b,r,N):
    count  = 0
    for i in range(N):
        if (b[i] == 0 ):
            count = count+1
            if (count == r):
                return i
    return N+1


#takes 2 boards and the size of the boards
def compare_2_boards(b1,b2,N):
    r = 1
    while r < N :
        val1 = white_at(b1,r,N)
        val2  = white_at(b2,r,N)
        #b2 has priority
        if val1 > val2:
            return False
        #b1 has priority (or the 2 have the exact same set up)
        elif val2 > val1:
            return True
        else:
            r = r+1
    #they are the same give priority to the first board
    return True


def sort_children(children: List[np.array], low: int, high: int) -> None:
    pivot = find_median_pivot(low, high, children)
    left_point = low
    right_point = high

    while left_point <= right_point:
        while compare_2_boards(children[left_point], children[pivot], 16):
            left_point += 1

        while not compare_2_boards(children[right_point], children[pivot], 16):
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

    if compare_2_boards(median[0], median[1], 16):
        median[0], median[1] = median[1], median[0]

    if compare_2_boards(median[1], median[2], 16):
        median[1], median[2] = median[2], median[1]

    if compare_2_boards(median[0], median[1], 16):
        median[0], median[1] = median[1], median[0]

    pivot = 0
    for i in range(0, len(children)):
        if np.array_equal(median[1], children[i]):
            pivot = i

    return pivot
    pass


def flip_adjacent(board,i,n):
    b_new = copy.copy(board)
    N = n*n
    #right
    i_r = i+1
    if not i_r>N-1:
        b_new[i_r] = not (board[i_r])
    #left
    i_l = i-1
    if not i_l<0:
        b_new[i_l] = not (board[i_l])
    #top
    i_t = i-n
    if not i_t<0:
        b_new[i_t] = not (board[i_t])
    #down
    i_d = i+n
    if not i_d>N-1:
        b_new[i_d] = not (board[i_d])

    return b_new

def generate_graph(board,max_d,n):
    graph = {}
    board = [board]

    for d in range(max_d-1):
        c = 0
        for b in board:
            children = []
            if not c == 0:
                children = generate_next_moves(b,n)
                board = board + children
            else:
                children = generate_next_moves(b,n)
                board = children
            c = c+len(children)
            graph[str(b).strip('[]')] = children
    return graph

def generate_next_moves(b,n):
    next_moves = []
    N = n*n
    #row
    for i in range(N):
        #make a shallow copy
        b_new = copy.copy(b)
        #flip the center piece
        b_new[i] = not (b_new[i])
        #flip adjascent
        b_new = flip_adjacent(b_new,i,n)
        next_moves.append(b_new)
    #return a list
    return next_moves

#to be deleted
def example_output():
    b = np.array([0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0])

    print("the initial array is:\n",b)

    n = 4
    max_d = 3
    return generate_graph(b,max_d,n)


if __name__== "__main__":
    # print(out)
    b1 = np.array([1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    b2 = np.array([1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0])
    b3 = np.array([0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1])
    b4 = np.array([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    board_list = [b1, b2, b3, b4]
    print('nodes before sorting\n' + board_list.__str__())
    sort_children(board_list, 0, len(board_list)-1)
    print('nodes after sorting\n' + board_list.__str__())
    # b = compare_2_boards(b1,b2,16)
    # print(b1)
    # print(b2)
    # print(b)

