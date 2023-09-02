a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))
def greatest_no(a,b,c):
    if a>b and a>c:
      print(a,"is greatest")
    elif b>a and b>c:
      print(b,"is greatest")
    else:
      print(c,"is greatest")
 return(a,b,c)
