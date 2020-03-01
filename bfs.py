# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178

import time


from heuristics import heuristic
from typing import List, Dict, Tuple
from collections import deque
from dfs import find_move


# the function used to break the ties between nodes with equal heuristics
# combined with python list.sort() as a 2nd sorting key function
# return (i, j) of location of first white or (n, n) if no white tokens are present

def find_first_white_token(node: List[List[int]]) -> Tuple[int, int]:
    for i in range(0, len(node)):
        for j in range(0, len(node)):
            if node[i][j] == 0:
                return i, j
            pass
        pass
    return len(node), len(node)
    pass


def getNodeVal(node: List[List[int]]) -> int:
    """Function that converts a node to an integer.
	Ex: [[0,0,0],[1,0,1],[0,1,0]] -> 1*0 + 2*0 + 4*0 + 8*1 + 16*0 + 32*1 + 64*0 + 128*1 + 256*0 -> 168

	Args:
			node: The node to be converted to a value.

	Returns:
			The return value. Integer representation of node.
	"""
    val = 0
    base = 1
    for row in range(len(node)):
        for col in range(len(node[0])):
            val += base * node[row][col]
            base = base * 2
    return val


def toggle_bit(bit) -> int:
    """Function that inverts bits.

	Args:
			bit: The bit to be inverted.

	Returns:
			The return value. 0 if bit was 1 and 1 if bit was 0.
	"""
    return 1 if bit == 0 else 0


def toggle(node, row, col) -> "child":
    """Function that toggles a node at a certain row and col and returns child.

	Args:
			node: The node to be toggled.
			row, col:	The row and col pair to toggle.

	Returns:
			The child of the node.
	"""
    new_node = []
    for r in node:
        new_node.append([c for c in r])

    new_node[row][col] = toggle_bit(new_node[row][col])
    if row + 1 < len(node):
        new_node[row + 1][col] = toggle_bit(new_node[row + 1][col])
    if row - 1 >= 0:
        new_node[row - 1][col] = toggle_bit(new_node[row - 1][col])
    if col + 1 < len(node[0]):
        new_node[row][col + 1] = toggle_bit(new_node[row][col + 1])
    if col - 1 >= 0:
        new_node[row][col - 1] = toggle_bit(new_node[row][col - 1])

    return new_node


# gets the solution path by comparing the boards before and after the moves
def get_solution_path(node_path: List) -> str:
    solution = '0\t' + str(node_path[0]).replace(",", "").replace("[", "").replace("]", "") + '\n'
    for i in range(0, len(node_path) - 1):
        solution += find_move(node_path[i], node_path[i + 1]) + '\t' + str(node_path[i + 1]).replace(",", "").replace(
            "[", "").replace("]", "") + '\n'
    return solution


# gets the search path from the closed list.
# the tuples in the dictionary contain (heuristic, game board) pairs
def get_search_path(nodes_explored: Dict[int, Tuple[int, List[List[int]]]]):
    search_path = ''
    for val in nodes_explored.keys():
        search_path += str(nodes_explored[val][0]) + ' ' + str(nodes_explored[val][0]) + ' 0\t' + str(nodes_explored[val][1]).replace(", ", "").replace("[", "").replace("]", "") + '\n'
    return search_path

def bfs(start_node: List[List[int]], goal_node: List[List[int]], max_depth: int) -> "solution path":
    """Breadth-first search (BFS) function.

	Args:
			start_node: The beginning node.
			goal_node: The node to try and reach.

	Returns:
			The path (list) taken to reach the node if any.
	"""
    d = deque([start_node, []])
    explored = {}
    level = 0

    # Return empty path if start is equal to goal
    if start_node == goal_node:
        return '0\t' + str(goal_node).replace("[", ""). replace(",", "").replace("]", ""), get_search_path({getNodeVal(start_node): (heuristic(start_node), start_node)})

    # Keep exploring while the queue has nodes
    while len(d) > 0:
        path = d.popleft()

        if level == 0:
            node = path
        else:
            # To keep track of levels an empty node gets popped between levels which will cause an exception
            try:
                node = path[-1]
            except Exception:
                node = []
                pass

        if len(node) == 0:
            level += 1
            # Return empty list if max depth was reached
            if max_depth == level:
                return 'no solution', get_search_path(explored)
            d.append(node)

        else:
            val = getNodeVal(node)
            if val not in explored:

                # Mark node as explored
                explored[val] = (heuristic(node), node)
                all_moves = []
                for row in range(len(node)):
                    for col in range(len(node)):
                        child = toggle(node, row, col)
                        new_path = list(path) if level != 0 else list([path])
                        new_path.append(child)
                        all_moves.append(new_path)
                        if child == goal_node:
                            level += 1
                            # print(level)
                            return get_solution_path(new_path), get_search_path(explored)

                # sorts the list of possible moves and breaks ties with the helper function find_First_white_token
                all_moves.sort(key=lambda x: (heuristic(x[-1]), find_first_white_token(x[-1])))
                for path in all_moves: d.append(path)
    # No solution found
    return 'no solution', get_search_path(explored)


