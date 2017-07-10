# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math
def solution(K, M, A):
    # write your code in Python 2.7
    # binary search
    
    sum_all = sum(A)
    max_element = max(A)
    expected_min = int(math.ceil(sum_all / float(K)))
    
    # print max(expected_min, max(A))
    
    # with a expected min value, try greedy algorithm
    lower_bound = expected_min
    upper_bound = max(lower_bound + max_element, lower_bound + 1)
    result = 0
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        # print result
        if check(A,K,mid) == False:
            # blocks overflow, shall increase the range
            lower_bound = mid + 1
        else:
            # blocks underflow or just match, keep result
            upper_bound = mid - 1
            result = max(mid,max_element)

    # find nothing 
    return result

def check(A,K,block_max):
    l = len(A)
    sum_block = [0] * K
    block_i = 0

    for i in xrange(0, l):
        if sum_block[block_i] + A[i] <= block_max:
            sum_block[block_i] += A[i]
        else:
            # go to next block
            block_i += 1

            if block_i >= K:
                return False
            else:
                sum_block[block_i] += A[i]

        # print "block_i", block_i
        # print sum_block
        # print A[i]
        
    return True

    # if block_i >= k:
    # fails, let's increase the expected min

    # if block_i < K
    # use too few blocks, decrease
    

print solution(3,0,[0,0,0])
print solution(3,5,[2,1,5,1,2,2,2])
print solution(4,5,[2,1,5,1,2,2,2])
print solution(5,5,[2,1,3,1,2,2,2])

