
def solution(A):
    min = float("inf")
    start = 0
    for i in xrange(0, len(A) - 1): 
        avg = (A[i] + A[i+1])/float(2) # math problem
        if avg < min:
            # update min
            print "min:", min, "avg:", avg
            min = avg
            start = i
        # avg == min, we are looking for the first start
        # avg > min, do nothing
    return start


print solution([4,2,2,5,1,5,8])
print solution([-4,-2,-2,-5,-1,-5,-8])
print solution([-3, -5, -8, -4, -10])



# def solution(A):
#     min = float("inf")
#     start = 0
#     for i in xrange(0, len(A) - 1):
#         avg = (A[i] + A[i+1])/float(2)
#         if avg < min:
#             # update min
#             # print "min:", min, "avg:", avg
#             min = avg
#             start = i
#         # avg == min, we are looking for the first start
#         # avg > min, do nothing
#     return start