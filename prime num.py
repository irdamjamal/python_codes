n=int(input("enter a num"))
c=1
for i in range(2,n):
    if n%i==0:
        c=0
if c==1:
    print("num is prime")
else:
    print("num is not prime")
