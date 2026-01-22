import sys

m = int(input())
res = set()

for i in range(m):
    inp = sys.stdin.readline().split()
    if len(inp) == 1:
        if inp[0] == "all":
            res = set([i+1 for i in range(20)])
        else:
            res = set()

    else:
        se = int(inp[1])
        if inp[0] == "add":
            res.add(se)
        elif inp[0] == "remove":
            res.discard(se)
        elif inp[0] == "check":
            if se in res: print(1)
            else: print(0)
        else:
            if se in res: res.discard(se)
            else: res.add(se)