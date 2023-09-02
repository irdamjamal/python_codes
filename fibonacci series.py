def fib(n):
    if n<0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter a num: "))
for i in range(1,n+1):
    print(fib(i),end=" ")
    
