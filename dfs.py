# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178


from typing import List
import statistics
import numpy as np
from next_moves import generate_graph, flip_adjacent
from next_moves import generate_graph, flip_adjacent, generate_next_moves
import copy


def find_move(before: np.array, after: np.array, is_goal: bool = False) -> str:
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


def children_node(graph, b):
    children = np.array([])

    children = generate_next_moves(b, N)
    board = children

    graph[str(b).strip('[]').replace('\n', '')] = children
    for child in children:
        if not (str(child).strip('[]') in graph):
            graph[str(child).strip('[]').replace('\n','')] = []


def get_search_path(explored: List[str]) -> str:
    search_path = ''
    for node in explored:
        search_path += '0 0 0\t' + node + '\n'
    return search_path
    pass


def dfs(graph, start, goal, explored, path_so_far, level):
    # Returns path from start to goal in graph as a string
    if not level > MAX_D:
        children_node(graph, start)
    print("generating nodes on level ", level)
    start = str(start).strip('[]').replace('\n', '')
    explored.append(start)

    if level > MAX_D:
        return "", get_search_path(explored)

    if start == goal:
        if len(explored) < 2:
            return '0\t' + start, get_search_path(explored)
        else:
            return path_so_far + find_move(np.fromstring(start, dtype=int, sep=' '), np.fromstring(explored[-2], dtype=int, sep=' ')) + '\t' + start + '\n', get_search_path(explored)

    if start in graph:
        for w in graph[start]:
            str_w = str(w).strip('[]').replace('\n', '')
            if str_w not in explored:
                if path_so_far is not "":
                    p,s = dfs(graph, w, goal, explored,
                            path_so_far + find_move(np.fromstring(path_so_far[-N**2*2:], dtype=int, sep=' '), np.fromstring(start, dtype=int, sep=' ')) + '\t' + start + '\n',
                            level + 1)
                else:
                    p, s = dfs(graph, w, goal, explored, '0\t' + start + '\n', level)
                if p:
                    return p, s
    if start == goal:
        return path_so_far, get_search_path(explored)
    else:
        return "", get_search_path(explored)


def start_dfs(b, goal, max_d, n):
    g = {}
    # graph(g,b)
    global MAX_D
    MAX_D = max_d
    global N
    N = n
    p = dfs(g, b, goal, [], "", 1)
    return p
