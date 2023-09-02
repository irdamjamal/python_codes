def outer():
    y=444
    def inner():
        nonlocal y
        y=555
        print("value of y inside the inner func:",y)
        return
    print("before calling value of y inside the inner function:",y)
    inner()
    print("after calling value of y inside outer func:",y)
    return
outer()
