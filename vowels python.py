def count_vowels(sentence):
    vowels = "AEIOUaeiou"
    vowel_count=0

    for char in sentence:
        if char in vowels:
            vowel_count+= 1

    return vowel_count
sentence=(input("Enter a sentence: "))
result = count_vowels(sentence)
print(f"The number of vowels in the given sentence is: {result}")
