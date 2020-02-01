import numpy as np
import copy


def flip_adjacent(board,i,j):
    #right
    i_r = i+1
    if not i_r>3:
        board[i_r,j] = not (board[i_r,j])
    #left
    i_l = i-1
    if not i_l<0:
        board[i_l,j] = not (board[i_l,j])
    #top
    j_t = j-1
    if not j_t<0:
        board[i,j_t] = not (board[i,j_t])
    #down
    j_d = j+1
    if not j_d>3:
        board[i,j_d] = not (board[i,j_d])

    return board

def generate_next_moves(b,n):
    #row
    for i in range(n):
        #col
        for j in range(n):
            #make a shallow copy
            b_new = copy.copy(b)
            #flip the center piece
            b_new[i,j] = not (b_new[i,j])
            #flip adjascent
            b_new = flip_adjacent(b_new,i,j)

            ##we should save them in a datastructure and returnig it##
            print("moving(",i,", ",j,")")
            print(b,"\n\n",b_new)
            print("\n")

#to be deleted
def example_output():
    b = np.array([[1,1,1,0],
            [1,0,0,1],
            [1,1,0,0],
            [0,1,1,1]])
    print("the initial array is:\n",b)

    n = 4
    generate_next_moves(b,n)


if __name__== "__main__":
  example_output()

