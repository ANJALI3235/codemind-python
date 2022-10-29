n=int(input())
lst=list(map(int,input().split()))
even=0
odd=0
for i in range(len(lst)):
    if i%2==0:
        even+=lst[i]
    else:
        odd+=lst[i]
print(abs(even-odd))