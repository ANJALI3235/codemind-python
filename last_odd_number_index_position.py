n=int(input())
lst=list(map(int,input().split()))
for i in range(n-1,0,-1):
    if lst[i]%2!=0:
        print(i)
        break
    