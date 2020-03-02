# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178
from typing import List


# heuristic h(n)
# count the number of 0's with 2 or more 1's around it
def heuristic(node: List[List[int]]) -> int:
    """Function that estimates the cost of a certain node (number of moves to goal state).
	Ex: [[0,1,0],[1,1,1],[0,1,0]] -> 1

	Args:
			node: The node to have it's cost estimated.

	Returns:
			The return value. Integer representing the cost of a node.
	"""
    cost = 0
    for i in range(0, len(node)):
        for j in range(0, len(node)):
            # skip if you're a 1
            if node[i][j] != 0:
                continue
            one_count = 0

            # there's a neighbour to your right
            if 0 < j < len(node) - 1:
                if node[i][j + 1] == 1:
                    one_count += 1
                    pass
                pass

            # neighbour to your left
            if 1 < j <= len(node) - 1:
                if node[i][j - 1] == 1:
                    one_count += 1
                    pass
                pass

            # neighbour above you
            if 0 < i <= len(node) - 1:
                if node[i - 1][j] == 1:
                    one_count += 1
                    pass
                pass

            # neighbour below you
            if i < len(node) - 1:
                if node[i + 1][j] == 1:
                    one_count += 1
                    pass
                pass
            if one_count >= 2:
                cost += 1
            pass
        pass
    return int(cost / 2)


# used to test the heuristic
# print(heuristic([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
