import sys

n = int(input())
for i in range(n):
    cnt = 0
    galho = sys.stdin.readline().strip()
    for j in galho:
        if j == "(": cnt += 1
        else: cnt -= 1
        if cnt<0 : break
    if cnt == 0: print("YES")
    else: print("NO")