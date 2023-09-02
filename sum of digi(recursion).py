def rec_sum(n):
    if n==0:
        return 0
    else:
        return (n%10 + rec_sum(n//10))
n=int(input("enter a no."))
print(rec_sum(n))
