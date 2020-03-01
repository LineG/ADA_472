# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178


from dfs import start_dfs
from bfs import bfs
from aStar import astar
import numpy as np
import time

def run_dfs(tokens, i):
    n, max_d = int(tokens[0]), int(tokens[1])
    search = open(f'{i}_dfs_search.txt', 'w+')
    solution = open(f'{i}_dfs_solution.txt', 'w+')
    dfs_results = start_dfs(np.array(list(tokens[3].strip('\n')), dtype=int), " ".join(n ** 2 * '0 '[:-1]), max_d, n)
    if dfs_results[0] == '':
        solution.write('no solution')
    else:
        solution.write(dfs_results[0])
    search.write(dfs_results[1])
    pass


def run_bfs(tokens, i):
    n, max_l = int(tokens[0]), int(tokens[2])
    search = open(f'{i}_bfs_search.txt', 'w+')
    solution = open(f'{i}_bfs_solution.txt', 'w+')
    start_ints = [int(i) for i in tokens[3].strip()]
    starting_board = [start_ints[i:i+n] for i in range(0, len(start_ints), n)]
    bfs_results = bfs(starting_board, [[0 for i in range(0, n)] for i in range(0, n)], max_l)
    search.write(bfs_results[1])
    solution.write(bfs_results[0])
    pass

def run_astar(tokens, i):
    n, max_l = int(tokens[0]), int(tokens[2])
    search = open(f'{i}_astar_search.txt', 'w+')
    solution = open(f'{i}_astar_solution.txt', 'w+')
    starting_board = [int(i) for i in tokens[3].strip()]
    astar_results = astar(starting_board, [0 for i in range(0, n ** 2)], max_l)
    search.write(astar_results[0])
    solution.write(astar_results[1])
    pass

def main():
    with open('puzzles.txt') as f:
        puzzles = f.readlines()
    pass

    for i in range(len(puzzles)):
        print("Starting DFS: " + str(i + 1) + "\n")
        curr_time = time.time()
        run_dfs(puzzles[i].split(" "), i)
        print("DFS: " + str(i + 1) + " completed in " + str(time.time() - curr_time) + " seconds\n")

        print("Starting BFS: " + str(i + 1) + "\n")
        curr_time = time.time()
        run_bfs(puzzles[i].split(" "), i)
        print("BFS: " + str(i + 1) + " completed in " + str(time.time() - curr_time) + " seconds\n")

        print("Starting A*: " + str(i + 1) + "\n")
        curr_time = time.time()
        run_astar(puzzles[i].split(" "), i)
        print("A*: " + str(i + 1) + " completed in " + str(time.time() - curr_time) + " seconds\n")

    pass


if __name__ == '__main__':
    main()
    pass