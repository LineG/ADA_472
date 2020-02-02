import numpy as np

graph = {
    '111 111 111': ['001 011 111'],
    '001 011 111': ['011 100 101', '010 010 111', '001 111 001', '001 010 100'],
    '011 100 101': [],
    '010 010 111': [],
    '001 111 001': [],
    '001 010 100': ['010 011 100'],
    '010 011 100': ['000 100 110'],
    '000 100 110': ['000 000 000'],
    '000 000 000': []
}

def DFS(graph, start, goal, explored, path_so_far):
    # Returns path from start to goal in graph as a string
    explored.add(start)
    if start == goal:
        return path_so_far + ' -> ' + start
    for w in graph[start]:
        if w not in explored:
            if(path_so_far is not ""):
              p = DFS(graph, w, goal, explored, path_so_far + ' -> ' + start)
            else:
              p = DFS(graph, w, goal, explored, start)
            if p:
                return p
    return ""

dfs_solution = DFS(graph, '111 111 111', '000 000 000', set(), "")
print(dfs_solution)
