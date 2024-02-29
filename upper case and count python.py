def count_spaces_and_convert_to_uppercase(input_string):

    uppercase_string = input_string.upper()
    
    
    space_count = uppercase_string.count(' ')
    
    return uppercase_string, space_count

input_string = input("Enter a string: ")
uppercase_string, space_count = count_spaces_and_convert_to_uppercase(input_string)
print("Uppercase String:", uppercase_string)
print("Number of spaces in the string:", space_count)
