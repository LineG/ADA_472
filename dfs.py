import numpy as np
from next_moves import generate_graph,flip_adjacent

def DFS(graph, start, goal, explored, path_so_far):
    # Returns path from start to goal in graph as a string
    explored.append(start)
    # print(f'Visited State: {start}')
    # print(f'Closed List: {explored}')
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
    return "no solution"


# graph = {
#     '0 1 0 1 1 1 0 1 0': [np.array([0,0,0,0,0,0,0,0,0]),np.array([0,0,0,1,0,1,1,0,1])],
#     '0 0 0 0 0 0 0 0 0': []
# }

b = [1,1,1,1,1,0,1,1,0]


graph = generate_graph(b,3,3)
for c in graph:
    print(c)
    print(graph[c])


dfs_solution = DFS(graph,'1 1 1 1 1 0 1 1 0','0 0 0 0 0 0 0 0 0',[],"")
print(dfs_solution)