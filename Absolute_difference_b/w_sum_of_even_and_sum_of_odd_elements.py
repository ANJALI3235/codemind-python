n=int(input())
lst=list(map(int,input().split()))
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(abs(even-odd))