from typing import List
import statistics
import numpy as np
from next_moves import generate_graph, flip_adjacent


def find_move(before: np.array, after: np.array) -> str:
    difference = abs(before - after)
    n = int(len(difference) ** (1 / 2))
    difference = np.split(difference, n)
    flipped_rows = []
    flipped_columns = []
    for row in range(0, n):
        for column in range(0, n):
            if difference[row][column] == 1:
                flipped_rows.append(row)
                flipped_columns.append(column)
                pass
            pass
        pass
    return get_letter(flipped_rows, n) + '' + str(statistics.mode(flipped_columns) + 1)

    pass


def get_letter(flipped_rows: List[int], n: int) -> chr:
    if len(flipped_rows) < 3:
        return chr(min(flipped_rows) + 65)
        pass
    else:
        return chr(int(statistics.median(flipped_rows)) + 65)
        pass
    pass


def DFS(graph, start, goal, explored, path_so_far):
    # Returns path from start to goal in graph as a string
    explored.append(start)
    # print(f'Visited State: {start}')
    # print(f'Closed List: {explored}')
    if start == goal:
        return path_so_far + find_move(np.fromstring(explored[-2], dtype=int, sep=' '), np.fromstring(start, dtype=int, sep=' ')) + "\t" + start
    if start in graph:
        for w in graph[start]:
            if str(w).strip('[]') not in explored:
                if (path_so_far is not ""):
                    p = DFS(graph, str(w).strip('[]'), goal, explored, path_so_far + find_move(np.fromstring(explored[-2], dtype=int, sep=' '), np.fromstring(start, dtype=int, sep=' ')) + "\t" + start + "\n")
                else:
                    p = DFS(graph, str(w).strip('[]'), goal, explored, "0\t" + start + "\n")
                if p:
                    return p
    return "no solution"


# graph = {
#     '0 1 0 1 1 1 0 1 0': [np.array([0,0,0,0,0,0,0,0,0]),np.array([0,0,0,1,0,1,1,0,1])],
#     '0 0 0 0 0 0 0 0 0': []
# }

b = [1, 1, 1, 0, 0, 1, 0, 1, 1]

graph = generate_graph(b, 7, 3)

dfs_solution = DFS(graph, '1 1 1 0 0 1 0 1 1', '0 0 0 0 0 0 0 0 0', [], "")
print(dfs_solution)
