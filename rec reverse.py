def rec_rev(n):
    if n>0:
        return 0
    else:
        d=n%10
        n=n/10
        return rev=(rec_rev)*10+d
n=int(input("enetr a no."))
print(rec_rev(n))
