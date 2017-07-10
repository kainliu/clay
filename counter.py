from collections import Counter


arr = [(1,1), (2,2), (1,1), (1,1), (2,3)]

cnt = Counter(arr)

# print dir(cnt)
print cnt.most_common(1)
