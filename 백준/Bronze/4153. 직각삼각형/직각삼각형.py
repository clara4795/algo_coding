while True:
    a, b, c = map(int, input().split())
    
    if a*b*c == 0:
        break
    
    m = sorted([a, b, c])
    if m[2]**2 == (m[1]**2 + m[0]**2): print("right")
    else: print("wrong")