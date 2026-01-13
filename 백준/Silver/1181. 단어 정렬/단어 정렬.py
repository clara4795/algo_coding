n = int(input())
word = []
for i in range(n):
    word.append(input())
res = sorted(set(word), key=lambda x: (len(x), x))
for i in res: print(i)