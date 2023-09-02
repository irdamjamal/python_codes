def pallindrome(n):
    '''this function is to check pallindrome or not'''
    rev=0
    while n>0:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
a=int(input("enter a no."))
reverse = pallindrome(a)
if reverse==a:
    print(a,"is pallindrome no.")
else:
    print(a,"is not a pallindrome no.")
print(pallindrome.__doc__)


    
