p = '''2 5 20
1 3 12
2 4 10
3 5 8
1 4 6
5 7 19
6 8 17
4 7 9
8 10 16
3 9 11
10 12 15
2 11 13
12 14 20
13 15 18
11 14 16
9 15 17
7 16 18
14 17 19
6 18 20
1 13 19'''

cities = p.split("\n")#.split("\n")
cities = [ [int(x) for x in city.split(' ')] for city in cities]

start = [0]
visited = [False] * 21

def solution(n):
    cities.insert(0, [0,0,0])

    print cities
    start[0] = n
    print start
    
    print '---'
    dfs(n, [n])


def dfs(now, path = []):
    if now < 1 or now > 20:
        return raiseValueError()

    print now, ' -- ', path
    
    
    if len(path) == 20:
        if start[0] in cities[now]:
        # print '#path'
        # print start, cities[now], start in cities[now]
            print path

    for next_city in cities[now]: # 3 next_city
        if visited[next_city] ==  1:
            continue
        # it's a new city
        visited[now] = True
        dfs(next_city, path + [next_city])
        # backtracking
        visited[now] = False

    # all next cities are in the path, death end

    # shoule backtrack


print solution(5)
