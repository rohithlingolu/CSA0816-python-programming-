def delchar(s, c):
    if len(c) != 1:
        return s
    return s.replace(c, '')

# Test Cases
input_string = input("Enter the string: ")
char_to_remove = input("Enter a character to be deleted: ")
result = delchar(input_string, char_to_remove)
print("String after the character is removed:", result)
