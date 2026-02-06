import sys
from collections import deque

# dfs
def dfs(num):
    need_visited = [num]
    hap = [1, 2, 3]
    res = 0
    while need_visited:
        n = need_visited.pop()
        for i in hap:
            if n-i > 0: 
                need_visited.append(n-i)
            elif n-i == 0:
                res += 1
    return res

t = int(input())
for i in range(t):
    m = int(sys.stdin.readline())
    print(dfs(m))
