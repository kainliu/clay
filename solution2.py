#https://codility.com/programmers/lessons/8-leader/equi_leader/

def solution(A):
    # at least 2 elements

    if len(A) < 2:
        return 0
    # if the leader is the same in left-part and right-part
    # (more than half)
    # then, there exists a global leader in the whole array
    dict = {}
    max = 0
    maxValue = None
    for i in A:
        dict[i] = dict.get(i, 0) + 1
        if dict[i] > max:
            max = dict[i]
            maxValue = i

    # if double the max count still counts no more than the
    # who length, save the time, there is no such leader
    if 2 * max <= len(A) or maxValue == None:
        return 0



    count_left_sequence = 0
    count_equi_leader = 0
    for i in range(0, len(A)):
        if A[i] == maxValue:
            count_left_sequence += 1
        print i , A[i], count_left_sequence
        if 2 * count_left_sequence > (i+1) and \
            2 * (max - count_left_sequence) > (len(A) - i - 1):
            print "leader:", i
            count_equi_leader += 1

    return count_equi_leader

print solution([4,3,4,4,4,2])

