# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    # first step find peaks
    length = len(A)
    peaks = length * [0]
    peak_index = []
    distances = []
    for i,num in enumerate(A):
        if i > 0 and i < length - 1:
            if A[i-1] < A[i] > A[i+1]:
                peaks[i] = 1
                peak_index.append(i)
                if len(peak_index) > 1:
                    distances.append(peak_index[-1] - i)
    print peaks
    # print peak_index
    # print distances
    # worst time complexity is O(N)
    
    # one peak, one flag
    # or no peak not only 
    if len(peak_index) <= 1:
        return len(peak_index)

    max_flags_upper = len(peak_index)
    max_flags = 1
    for x in range(2, max_flags_upper+1):
        if check(x, peaks):
            max_flags = x

    return max_flags

def check(x, peaks):
    N = len(peaks)
    flags = x
    pos = 0 
    while pos < N and flags > 0:
        if peaks[pos] == 1:
            flags -= 1
            pos += x
        else:
            pos += 1
    return flags == 0


print solution([1,4,3,2,4,3,2])







