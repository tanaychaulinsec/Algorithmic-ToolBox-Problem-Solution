#python3
def fibonacci(n):
    a=[0,1]
    for i in range(1,n+1):
        a.insert(i,a[i-1]+a[i-2])
    return a[n]
n=int(input())
print(fibonacci(n))

