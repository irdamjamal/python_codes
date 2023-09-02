def reverse(string):
    string = string[::-1]
    return string
str = "guides"
print("the original string is: ",end=" ")
print(str)
print("the reversed string is: ",end=" ")
print(reverse(str))
