given_statement = input("Enter the statement: ")
vowels = sum(1 for char in given_statement if char.lower() in 'aeiou')
consonants = sum(1 for char in given_statement if char.isalpha() and char.lower() not in 'aeiou')

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

if vowels > consonants:
    print("Vowels are maximum.")
elif vowels < consonants:
    print("Consonants are maximum.")
else:
    print("Equal number of vowels and consonants.")
