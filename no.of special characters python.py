given_statement = input("Given statement: ")
special_characters = sum(1 for char in given_statement if not char.isalnum() and char != ' ')
print(f"Number of special characters: {special_characters}")
