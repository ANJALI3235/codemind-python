n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in lst:
    sum+=i
    average=sum/n
print("{:.2f}".format(average))