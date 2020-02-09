import numpy as np
from next_moves import generate_graph, flip_adjacent,generate_next_moves
import copy

MAX_D = 7
NN= 3


# b = np.array([0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1])
# goal ='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'

b = np.array([1,1,1,0,0,1,0,1,1])
goal ='0 0 0 0 0 0 0 0 0'


def children_node(graph,b):
    children = np.array([])

    children = generate_next_moves(b,NN)
    board = children

    graph[str(b).strip('[]')] = children

    for child in children:
        if not (str(child).strip('[]') in graph):
            graph[str(child).strip('[]')] = []


def DFS(graph, start, goal, explored, path_so_far,level):
    # Returns path from start to goal in graph as a string
    if not level > MAX_D:
        children_node(graph,start)
        print("generating nodes on level ", level)
    start = str(start).strip('[]')
    explored.append(start)

    if level > MAX_D:
        return ""

    if start == goal:
        return path_so_far + ' -> level ' + f'{level+1}'+' -- '+start

    if start in graph:
      for w in graph[start]:
          str_w = str(w).strip('[]')
          if str_w not in explored:
              if(path_so_far is not ""):
                p = DFS(graph, w, goal, explored,f'{path_so_far} -> level {level+1} -- {start}',level+1)
              else:
                p = DFS(graph, w, goal, explored, start,level)
              if p:
                return p

    return ""

def start_DFS(b, goal):
    g = {}
    p = DFS(g,b,goal,[],"",1)
    return p



dfs_solution = start_DFS(b,goal)


f = open("test.txt","w+")

f.write(dfs_solution)
f.close()