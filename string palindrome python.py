def is_palindrome(s):
    s = s.lower()  
    s = ''.join(c for c in s if c.isalnum())  
    return s == s[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
