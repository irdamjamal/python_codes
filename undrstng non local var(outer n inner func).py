def outer():
    y=100                #local for outer function
    def inner():
        y=200            #once we define inside a function it becomes local
        print("value of y inside inner function is:",y)
        return
    inner()
    print("value of y inside outer function is:",y)
                         #non local variable cannot be modified directly in inner function
    return
outer()
