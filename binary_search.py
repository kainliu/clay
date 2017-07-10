def bs(arr, target):
    # if len(arr) == 0:
    #     return None

    lower = 0
    upper = len(arr) - 1
    found = None
    while lower <= upper:

        mid = (lower + upper) // 2
        # print lower, upper, mid
        if arr[mid] == target:
            found = mid
            break
        else:
            if arr[mid] > target:
                # go left
                upper = mid - 1
            else:
                lower = mid + 1

    return found

print bs([1,2,3,4,5,6],3)
print bs([1,2,3,5,6],3)
print bs([1,2,5,6],3)
print bs([1,2,3,4],4)
print bs([4],4)
print bs([1],4)
print bs([],4)
print bs([1,2,3],4)
print bs([1,2,3],1)
