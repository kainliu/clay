def solution(N):
    # write your code in Python 2.7
    binary = bin(N).replace('0b','')
    print binary
    max_gap = 0
    last_peak = 0
    for index, byte in enumerate(binary):
        # print index, "hihi, ", byte
        if byte == "1":
            # it's a peak
            # print index
            this_gap = index - last_peak - 1
            max_gap = max(this_gap, max_gap)
            last_peak = index
    return max_gap

solution(-2)

print bin(-2).replace('0b','')