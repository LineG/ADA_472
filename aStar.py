# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178

from next_moves import generate_next_moves
from dfs import find_move
from bfs import get_solution_path, find_first_white_token
from heuristics import heuristic
import numpy as np

# we stop of max_l is reached


class Node:

    def __init__(self, parent=None, board=None, depth=0):
        self.board = board
        self.parent = parent
        self.n = int(len(board) ** (1 / 2))
        self.h = heuristic([board[i: i + self.n] for i in range(0, self.n)])
        self.g = depth
        self.f = self.h + self.g

    def __eq__(self, other):
        self_board = self.board
        if isinstance(self.board, np.ndarray):
            self_board = self.board.tolist()

        other_board = other.board
        if isinstance(other.board, np.ndarray):
            other_board = self.board.tolist()

        return self_board == other_board

    def generate_children(self):
        children = []
        next_moves = generate_next_moves(np.array(self.board), int(len(self.board) ** (1 / 2)), False)
        for move in next_moves:
            g = self.g
            child_g = g + 1
            children.append(Node(self, move, (child_g)))
        return children


def get_search_path(closed_list):
    search_path = ''
    for node in closed_list:
        search_path += str(node.f) + ' ' + str(node.h) + ' ' + str(node.g) + '\t' + str(node.board).replace(", ", "").replace("[", "").replace("]", "").replace(" ", "") + '\n'
    return search_path
    pass


def astar(start_board, end_board, max_l):
    open_list = []
    closed_list = []

    start = Node(None, start_board, 1)
    open_list.append(start)

    while len(open_list) > 0 and len(closed_list) < max_l:
        open_list.sort(key=lambda node: (node.f, find_first_white_token([node.board[i: i + node.n] for i in range(0, node.n)])))
        # now the current node should be place last in the closed list
        current = open_list.pop(0)
        closed_list.append(current)
        # print(current.board)

        # if current is goal stop
        try:
            if current.board == end_board:
                return get_search_path(closed_list), get_solution_path([np.array(x) for x in find_path(current)[0]])
        except ValueError:
            if current.board.tolist() == end_board:
                return get_search_path(closed_list), get_solution_path([np.array(x) for x in find_path(current)[0]])

        # generate the children of the current node
        children = current.generate_children()

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            for node in open_list:
                if child == node:
                    if child.g > node.g:
                        continue
            open_list.append(child)

    return get_search_path(closed_list), 'no solution'


def find_path(current):
    path = []
    current_node = current
    while current_node is not None:
        path.append(current_node.board)
        current_node = current_node.parent
    return path[::-1], len(path)


