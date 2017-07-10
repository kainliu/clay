arr = [1, 23, 12, 9, 30, 2, 50] 


def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

# 1 -> 32
def mergesort(arr):
    l = len(arr)
    if l <= 1:
        print '0-1',l, arr
        return arr
    elif l == 2:
        print '2', arr
        if arr[0] > arr[1]:
            swap(arr, 0, 1)
        print '2', arr
        return arr
    else:
        # cut into half
        left = arr[0: l // 2]
        print 'left', left
        left = mergesort(left)
        print 'left', left
        right = arr[l // 2: l]
        print 'right', right
        right = mergesort(right)
        print 'right', right
        # 
        result = []
        while left and right:
            # from back to front
            if left[-1] > right[-1]:
                result.insert(0,left.pop())
            else:
                result.insert(0,right.pop())
        # remaining are put in the front
        result = left + right + result
        # print 'remaining', left, right
        print 'result', result
        print '---'
        return result

# recursion, sub
print mergesort(arr)