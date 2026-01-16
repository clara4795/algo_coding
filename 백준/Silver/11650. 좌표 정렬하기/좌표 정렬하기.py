import sys

n = int(input())
res = []
for i in range(n):
    key, value = map(int, sys.stdin.readline().split())
    res.append([key, value])
for i in sorted(res, key = lambda x: (x[0], x[1])):
    print(i[0], i[1])
    
    