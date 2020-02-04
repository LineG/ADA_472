import numpy as np
graph = {
    '0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 0': [np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]), np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])],
    '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0': []
}

def DFS(graph, start, goal, explored, path_so_far):
    # Returns path from start to goal in graph as a string
    explored.append(start)
    if start == goal:
        return path_so_far + ' -> ' + start
    if start in graph:
      for w in graph[start]:
          if str(w).strip('[]') not in explored:
              if(path_so_far is not ""):
                p = DFS(graph, str(w).strip('[]'), goal, explored, path_so_far + ' -> ' + start)
              else:
                p = DFS(graph, str(w).strip('[]'), goal, explored, start)
              if p:
                  return p
    return ""

dfs_solution = DFS(graph, '0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', [], "")
print(dfs_solution)
