n, m = map(int, input().split())

def get_gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

gcd = get_gcd(n,m)
lcm = (n*m) // gcd

print(gcd)
print(lcm)