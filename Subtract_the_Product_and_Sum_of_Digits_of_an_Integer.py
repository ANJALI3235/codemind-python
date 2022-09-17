n = int(input())
sum = 0
product = 1
temp = n
while n>0:
    r = n%10
    sum = sum+r
    product = product*r
    n = n//10
print(product-sum)