N = int(input())
max=0
for i in range(N):
    d = N%10
    if max<d:
        max=d
    N = N//10
print(max)
