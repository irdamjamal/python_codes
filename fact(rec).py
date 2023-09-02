def fac(a):
    if a==1:
        return 1
    else:
        return a*fac(a-1)
n=int(input("enter a no."))
print("factorial is:",fac(n))
    

