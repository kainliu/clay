arr = [0,1,3,5,8,12,17,20]

def bisectInteration(arr, x, lo = 0, hi = None):
    if lo < 0:
        raise ValueError("lo should be no less than 0")
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            # in left half
            hi = mid
        else:
            lo = mid + 1
        print "lo:", lo, " hi:", hi
    return lo


def bisectRecursion(arr, x, lo = 0, hi = None):
    if lo < 0:
        raise ValueError("lo should be no less than 0")
    if hi is None:
        hi = len(arr)

    # if low and high pointers the same element
    if lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
        print "lo:", lo, " hi:", hi
        return bisectRecursion(arr, x, lo, hi)
    else:
        return lo



# print bisect(arr, 0.5)
print arr
arr.insert(bisectInteration(arr, 13), 13)
print arr
arr.insert(bisectRecursion(arr, 7), 7)
print arr



