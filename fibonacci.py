from timeit import default_timer as timer


k = 20
_times = [0, 0]

def fib(n):
    _times[0] += 1

    if n <= 1: return 1
    # if n == 2: return 1
    
    return fib(n-1) + fib(n-2)

start = timer()
print fib(k)
end = timer()
time1 = end - start

def fib_cache(n, _cache = {}):
    """ Fibonacci calculator with cache """

    if n in _cache:
        return _cache[n]      # Return cache results

    if n <= 1: 
        result = 1
    else:
        result = fib_cache(n-1) + fib_cache(n-2)
        # Callers will never provide a second parameter for this function.

    _cache[n] = result        # Store results
    return result
    
start = timer()
print fib_cache(k)
print _times
end = timer()
time2 = end - start



print '%6f / %6f = %d' % (time1, time2, time1 / time2)

