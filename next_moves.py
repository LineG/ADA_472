import numpy as np
import copy

# 1 --> black side
# 0 --> white side

#takes 2 boards and the size of the board
def white_at(b,r,N):
    count  = 0
    for i in range(N):
        if (b[i] == 0 ):
            count = count+1
            if (count == r):
                return i
    return N+1


#takes 2 boards and the size of the boards
def compare_2_boards(b1,b2,N):
    r = 1
    while r < N :
        val1 = white_at(b1,r,N)
        val2  = white_at(b2,r,N)
        print("val1 is ",val1)
        print("val2 is ",val2)
        #b2 has priority
        if val1 > val2:
            return False
        #b1 has priority (or the 2 have the exact same set up)
        elif val2 > val1:
            return True
        else:
            r = r+1
            print(r)
    print("eq")
    return True

def flip_adjacent(board,i,n):
    #right
    i_r = i+1
    if not i_r>n:
        board[i_r] = not (board[i_r])
    #left
    i_l = i-1
    if not i_l<0:
        board[i_l] = not (board[i_l])
    #top
    i_t = i-n
    if not i_t<0:
        board[i_t] = not (board[i_t])
    #down
    i_d = i+n
    if not i_d>n:
        board[i_d] = not (board[i_d])

    return board

def generate_next_moves(b,n):
    out = []
    N = n*n
    #row
    for i in range(N):
        #make a shallow copy
        b_new = copy.copy(b)
        #flip the center piece
        b_new[i] = not (b_new[i])
        #flip adjascent
        b_new = flip_adjacent(b_new,i,n)
        out.append(b_new)
    #return a list
    return out

#to be deleted
def example_output():
    b = np.array([1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1])
    print("the initial array is:\n",b)

    n = 4
    return generate_next_moves(b,n)


if __name__== "__main__":
    # out = example_output()
    # for b in range(len(out)):
    #     print("child number ",b+1)
    #     print(out[b])

    b1 = np.array([1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    b2 = np.array([1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0])
    b = compare_2_boards(b1,b2,16)
    print(b1)
    print(b2)
    print(b)

