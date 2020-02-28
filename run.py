# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178


from dfs import start_dfs
from bfs import bfs
import numpy as np


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
    print('\n')

def run_bfs(tokens, i):
    n, max_l = int(tokens[0]), int(tokens[2])
    search = open(f'{i}_dfs_search.txt', 'w+')
    solution = open(f'{i}_dfs_solution.txt', 'w+')
    start_ints = [int(i) for i in tokens[3].strip()]
    starting_board = [start_ints[i:i+n] for i in range(0, len(start_ints), n)]
    bfs(starting_board, [[0 for i in range(0, n)] for i in range(0, n)], max_l)


def main():
    with open('puzzles.txt') as f:
        puzzles = f.readlines()
    pass

    for i in range(len(puzzles)):
    #    run_dfs(puzzles[i].split(" "), i)
        run_bfs(puzzles[i].split(" "), i)

    pass


if __name__ == '__main__':
    main()
    pass