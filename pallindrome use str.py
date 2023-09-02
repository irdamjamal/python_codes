def palindrome(str):
   rev=str[::-1]
   if str==rev:
       print(str,"is a pallindrome")
   else:
       print(str,"is not a pallindrome")
str=input("enter your string: ")
str=str.lower()
palindrome(str)
       
