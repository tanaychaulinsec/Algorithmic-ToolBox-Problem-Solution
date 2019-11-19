# Python3

a, b = [int(i) for i in input().split()]

def  gcd(a, b):
    if b == 0:
        return a
    elif a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a )

print(a*b//gcd(a,b))