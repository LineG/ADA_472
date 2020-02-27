# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178


from typing import List
import statistics
import numpy as np
from next_moves import generate_graph, flip_adjacent
from next_moves import generate_graph, flip_adjacent, generate_next_moves
import copy

#we stop of max_l is reached

class Node:

    def __init__(self, parent=None, board=None, depth=0):
        self.board = board
        self.parent = parent

        self.h = getNodeVal(board)
        self.g = depth
        self.f = self.h + self.g

    def __eq__(self, other):
        return self.board == other.board

    def generate_children(self):
        children = []
        next_moves = generate_next_moves(self.board,4)
        for move in next_moves:
            children.append(Node(self,move,(self.g+1)))
        return children


def astar(start_board,end_board):
    depth = 0
    open_list = []
    closed_list = []

    start = Node(None,start_board,depth)
    open_list.append(start)
    current = start

    while len(open_list) > 0:

        #set the index of the current node to 0
        index = 0
        current = open_list[index]

        i = 0
        #find the node from the open list with the lowest f
        for n in open_list:
            #find the node with the lowest f in the open list
            #set it as current node
            if n.f < current.f:
                current = n
                index = i
            i += 1

        #now the current node should be place last in the closed list
        open_list.pop(index)
        closed_list.append(current)
        # print(current.board)

        #if current is goal stop
        if current.board == end_board:
            path = []
            current_node = current
            while current_node is not None:
                path.append(current_node.board)
                print(current_node.f)
                current_node = current_node.parent
            return path[::-1],len(path)

        #generate the childre of the current node
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

# for row in range(len(node)):
	# 	val += base * node[row] * (16 - (row + 1))

#heuristics h(n)
def getNodeVal(node) -> int:
    val = 0
    base = 1
    cluster = 0
    max_cluster = 0
    cluster_count = 0
    for row in range(len(node)):
        val += base * node[row]
        # if node[row] == 1:
        #     cluster += 1
        # else:
        #     if (cluster > max_cluster) & (cluster > 2):
        #         max_cluster == cluster
        #         cluster_count += 1
    return val + max_cluster + cluster_count


start_node = [1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0]
goal_node = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(astar(start_node,goal_node))
