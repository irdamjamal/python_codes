a=int(input("enter a no."))
p=a
rev=0
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
if p==rev:
    print(p,"is pallindrome no")
else:
    print(p,"is not a pallindrome no")

    
