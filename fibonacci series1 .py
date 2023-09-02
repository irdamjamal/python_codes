def fib(n):
    a,b,c=0,1,0
    sum=0
    for i in range(2,n+1):
        a=b
        b=s
        s=a+b
        sum=sum+s
        return sum
n=int(input("enter a num of terms: "))
print("sum of series is: ",fib(n))
