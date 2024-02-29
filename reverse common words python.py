def remove_common_words(S1, S2):
    words_S1 = set(S1.split())
    words_S2 = set(S2.split())

    common_words = words_S1.intersection(words_S2)

    new_S1 = ' '.join(word for word in S1.split() if word not in common_words)
    new_S2 = ' '.join(word for word in S2.split() if word not in common_words)

    return new_S1, new_S2

def main():
    test_cases = [
        ("sky is blue in color", "Raj likes sky blue color"),
        ("learn python", "python is easy to learn"),
        ("raju likes apple", "apple is red in color"),
        ("sita likes orange", "orange is rich in anti-oxidents"),
        ("raj is travelling to Chennai in train", "the rain will reach Chennai at 8 pm")
    ]

    for S1, S2 in test_cases:
        result_S1, result_S2 = remove_common_words(S1, S2)
        print(f"Input: S1 = \"{S1}\", S2 = \"{S2}\"")
        print(f"Output: {result_S1}\n        {result_S2}")
        print()

if __name__ == "__main__":
    main()
