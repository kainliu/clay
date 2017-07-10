'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''

N = 3

# board = [ [0]*N ]*N
board = [ [0 for x in range(0, N)] for y in range(0, N)]


def solution(n):
    # all queens placed
    if n == 0:
        # print board
        return True
    for i in xrange(0, N):
        for j in xrange(0, N):
            # if it's not okay to put queen in current block
            if is_attacked(i, j, board):
                continue 
            board[i][j] = 1
            # find any first solution
            if solution(n-1):
                return True

            # or find all solutions
            # solution(n-1)    
            board[i][j] = 0
    return False
    

def is_attacked(r, c, board):
    # check row
    for i in xrange(0, N):
        for j in xrange(0, N):
            if i == r or j == c or j-i == c-r or j+i == c+r :
                if board[i][j] == 1:
                    # print 'attacked', r,c 
                    return True
    return False
    
print solution(N)
print board