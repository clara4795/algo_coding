import sys

n = int(input())
res = []
for i in range(n):
    key, value = sys.stdin.readline().split()
    res.append([int(key), value])
for i in sorted(res, key = lambda x: x[0]):
    print(i[0], i[1])
