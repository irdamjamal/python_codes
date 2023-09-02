a=int(input("enter a num: "))
if a>0:
    for i in range(1,a):
        a=a*i
        i=i-1
    print(a)
else:
    print("enter + num")
