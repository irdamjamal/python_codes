def multiplier(n):
    return lambda a:a*n
doubler=multiplier(2)
print(doubler(10))
print(doubler(5))

