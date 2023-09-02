n=int(input("enter the year: "))
if (n%100!=0) and (n%400==0) or (n%4==0):
    print(n,"it is a leap year")
else:
    print(n,"not a leap year")
    
