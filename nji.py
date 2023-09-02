n=int(input("enter a num: "))
sum=0
a=n
while a>0:
    d = a % 10
    sum = sum + d*d*d
    a = a//10
    
if n == sum:
    print(n,"arm")
else:
    print(n,"not arm")
