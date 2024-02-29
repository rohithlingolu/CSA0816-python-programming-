def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

user_input = input("Enter a string: ")

reversed_result = reverse_string(user_input)

print("Reversed string:", reversed_result)
