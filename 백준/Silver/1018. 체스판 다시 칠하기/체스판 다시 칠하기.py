import sys

n, m = map(int, input().split())
board = []
for i in range (n):
    board.append(input())
cnt = []
for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k+h)%2 == 0:
                    if board[k][h] != "W":
                        white += 1
                    else:
                        black += 1
                else:
                    if board[k][h] != "W":
                        black += 1
                    else:
                        white += 1
        cnt.append(white)
        cnt.append(black)
print(min(cnt))