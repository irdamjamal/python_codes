
from functools import reduce

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
                                             #input range
x=int(input("enter start point of range: "))
y=int(input("enter end point of range: "))
                                             #create list for given range
cs=list(range(x,y+1))
                                             #filter prime no.
prime_cs=list(filter(prime,cs))
print(prime_cs)
                                             #reduce prime no. into sum
sum_cs=reduce(lambda x,y:x+y,prime_cs)
print("sum of prime no. is: ",sum_cs)

                                              


    
            
