import sys

n, m = map(int, input().split())
num = [i+1 for i in range(n)]
res = []
while True:
    if num:
        for i in range(m-1):
            num.append(num[0])
            num.pop(0)
        res.append(num.pop(0))
    else: break
for i in range(n):
    if i == 0: print("<", end="")
    if i == n-1: print(res[i], end=">")
    else: print(res[i], end=", ")