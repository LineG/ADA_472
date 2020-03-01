# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178

from next_moves import generate_next_moves
from heuristics import heuristic


# we stop of max_l is reached


class Node:

    def __init__(self, parent=None, board=None, depth=0):
        self.board = board
        self.parent = parent
        n = int(len(board) ** (1 / 2))
        self.h = heuristic([board[i: i + n] for i in range(0, n)])
        self.g = depth
        self.f = self.h + self.g

    def __eq__(self, other):
        return self.board == other.board

    def generate_children(self):
        children = []
        next_moves = generate_next_moves(self.board, 4)
        for move in next_moves:
            g = self.g
            child_g = g + 1
            children.append(Node(self, move, (child_g)))
        return children


def a_star(start_board, end_board, max_l):
    open_list = []
    closed_list = []

    current_l = 1

    start = Node(None, start_board, 1)
    open_list.append(start)
    current = start

    while len(open_list) > 0:

        # set the index of the current node to 0
        index = 0
        current = open_list[index]

        i = 0
        # find the node from the open list with the lowest f
        for n in open_list:
            # find the node with the lowest f in the open list
            # set it as current node
            if n.f < current.f:
                current = n
                index = i
            i += 1

        # now the current node should be place last in the closed list
        open_list.pop(index)
        closed_list.append(current)
        # print(current.board)

        # if current is goal stop
        if current.board == end_board:
            return find_path(current), "result"

        # generate the childre of the current node
        children = current.generate_children()

        current_d = current.g
        for child in children:

            current_l += 1
            if max_l < current_l:
                return find_path(current), "no result"

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            for node in open_list:
                if child == node:
                    if child.g > node.g:
                        continue

            open_list.append(child)


def find_path(current):
    path = []
    current_node = current
    while current_node is not None:
        path.append(current_node.board)
        current_node = current_node.parent
    return path[::-1], len(path)


start_node = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
goal_node = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a_star(start_node, goal_node, 11000))
