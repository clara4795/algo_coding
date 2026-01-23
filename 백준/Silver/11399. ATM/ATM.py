import sys

n = int(input())
time = map(int, sys.stdin.readline().split())
res = 0
sum = 0
for i in sorted(time):
    res += (i + sum)
    sum += i
print(res)