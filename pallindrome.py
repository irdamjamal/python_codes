a=int(input("enter a no.")) #Input le re hai 123
p=a                         #a change hora hai loop m so ye variable assign kia h  p=123
rev=0
while a>0:
    d=a%10                  #d=3, d = 2, d=1
    rev=rev*10+d            # rev = 0 tha pehele, but yaha 0 * 10+3= 3 .... 2nd bri m 32.... 3rd bri m 321
    a=a//10                 # 123//10 a =12 ,a= 1, 1//10... 0
if p==rev:
    print(p,"is pallindrome no")
else:
    print(p,"is not a pallindrome no")

    
