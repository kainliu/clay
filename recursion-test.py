times = 0
def run(k, k2=0):
    global times
    if k <= 0:
        return k2

    times += 1
    k2 = k // 2
    print times, ':k', k, 'k2', k2

    
    '''
    return value is kept, other value are the same in the scope
    '''
    

    root = run(k-1, k2) # recursion here

    print times, ':root', root, 'k', k, 'k2', k2
    # times += 1
    return root

print run(8, 888)

'''
1 :k 8 k2 888
2 :k 7 k2 888
3 :k 6 k2 888
4 :k 5 k2 888
5 :k 4 k2 888
6 :k 3 k2 888
7 :k 2 k2 888
8 :k 1 k2 888
8 :root 888 k 1 k2 0 # still remember last state 
                       --> iterate from inside to outside
9 :root 888 k 2 k2 1
10 :root 888 k 3 k2 1
11 :root 888 k 4 k2 2
12 :root 888 k 5 k2 2
13 :root 888 k 6 k2 3
14 :root 888 k 7 k2 3
15 :root 888 k 8 k2 4
888
[Finished in 0.1s]
'''