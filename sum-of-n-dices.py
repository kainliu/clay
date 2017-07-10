
'''
@param: Int. number of dices
@return: {Int: Int}. count of all possbile permutations
'''
def dices(n):
    
    def roll(target_sum, k):
        '''
        in order to get target_sum with k dices
        @return Int. possible permutations.
        '''
        counter = 0
        if k == 1:
            # we can only get 1 - 6
            if 1 <= target_sum <= 6 : 
                return 1
            else:
                return 0  # no way
        else:
            for v in xrange(1, 7):
                counter += roll(target_sum - v, k - 1)

        return counter

    # possible outcome
    _min, _max = [n, 6 * n]
    # symmetry, only looking at left half
    _mid = (_min + _max) // 2 

    results = {}
    for x in range(_min, _mid + 1):
        results[x] = roll(x, n)
    
    for x in range(_mid + 1, _max + 1):
        results[x] = results[_max + _min - x]

    return results


n = 2
results = dices(6)

print results
y = 0
z = 0
for x in range(26, 37):
    if x in results:
        y += results[x]

print y

for x in results:
    z += results[x]

print z
print y/ (z * 1.0)
