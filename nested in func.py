def outer():
    a=10
    def inner():
        a=100
        return a
    inner()
    print("value of outer func:",a)
    return
outer()
