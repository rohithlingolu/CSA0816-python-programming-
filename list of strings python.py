from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

def main():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["banana"],
        ["12345"]
    ]

    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"Input: {strs}")
        print(f"Output: {result}")
        print()

if __name__ == "__main__":
    main()
