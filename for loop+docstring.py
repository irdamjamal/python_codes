def multiple(n):
    '''this program prints multiples of 5'''
    for i in range(0,n+1,5):
        print(i,end=',')
a=int(input("enter a no."))
multiple(a)
print("\n",multiple.__doc__)
