#python3
n=list(map(int,input().split()))
List1=list(map(int,input().split()))
max=List1[0]
max2=0
for num in List1[1:]:
    if num>max:
        max2=max
        max=num
    elif max2==0 or num>max2:
        max2=num
print(max*max2)
