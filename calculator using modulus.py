#creating calculator by importing arithmatic.py

from arithmatic import *

print("press + for addition:")
print("prerss - for subtraction:")
print("press * for multiplication:")
print("press // for floor division:")
print("press % for modulus:")
print("press ** for exponent:")
print("press / for true division:")

op=input("enter operation of your choice:")

if op=='+':
    print("sum=",add())
elif op=='-':
    print("sub=",sub())
elif op=='*':
    print("sub=",mul())
elif op=='//':
    print("floor div=",fdiv())
elif op=='%':
    print("modulus=",mod())
elif op=='**':
    print("exponent=",exp())
elif op=='/':
    print("true division=",tdiv())
    
