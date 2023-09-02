def mul(a):                                                       #mul is a func
    '''check whether fuction is a multiple of 7 or not'''
    if a<0:
        return 0
    elif a%7==0:
        print(a," is a multiple of 7")
        return
    else:
        print(a,"is not a multiple of 7")
        return
n=int(input("enter a no."))
mul(n)                                                            #calling a func
print(mul.__doc__)
