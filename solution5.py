# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# 36%
# peaks

def solution(A):
    # write your code in Python 2.7
    
    # first step find peaks
    length = len(A)
    peaks = length * [0]
    peak_index = []
    for i,num in enumerate(A):
        if i > 0 and i < length - 1:
            if A[i-1] < A[i] > A[i+1]:
                peaks[i] = 1
                peak_index.append(i)
    print peaks
    print peak_index
    # worst time complexity is O(N)

    blocks = 0
    # how many blocks? from 1,2,3...floor(N/2)
    #
    # PROBLEMS HERE, the upper boundary is not correct
    # 2. use binary search to find maximum
    for i in xrange(1, int(length ** 0.5 + 1)):
        # 15 % 1 => 15
        # 15 % 2 => 1, can not be split into 2 parts
        # 15 % 3 => 0
        # 15 % 4 => 3

        if length % i :
            continue
    
        lower = [x for x in range(0, length, length/i)]
        upper = [x for x in range(length/i -1, length, length/i)]
        print lower, upper
        success = [0] * len(lower)
        for j in xrange(0, len(lower)):
            
            for k in peak_index:
                if lower[j] <= k <= upper[j]:
                    success[j] = 1

        if min(success) == 0:
        # it's not sucessful, we should stop
            break
        else:
            blocks = i

    print blocks




solution([3,2,1,2,3,1,2,1])

solution([1,2,3,4,3,4,1,2,3,4,6,2])