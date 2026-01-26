import sys

t = int(input())
for j in range(t):
    inp = int(sys.stdin.readline())
    cnt0 = [1, 0, 1]
    cnt1 = [0, 1, 1]
    for i in range(3, inp+1):
        cnt0.append(cnt1[i-1]) 
        cnt1.append(cnt1[i-1]+cnt1[i-2])
    print(cnt0[inp], cnt1[inp])
