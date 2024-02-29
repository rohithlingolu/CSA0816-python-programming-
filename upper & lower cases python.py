lowercase_count = 0
uppercase_count = 0

while True:
    char = input("Enter any character: ")
    
    if char == '*':
        break
    
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1

print("Total count of lower case:", lowercase_count)
print("Total count of upper case:", uppercase_count)
  
