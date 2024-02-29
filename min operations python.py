def min_operations(word1, word2):
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

def main():
    test_cases = [
        ("horse", "ros"),
        ("intention", "execution"),
        ("sunday", "saturday"),
        ("cat", "cut"),
        ("girl", "grill")
    ]

    for word1, word2 in test_cases:
        result = min_operations(word1, word2)
        print(f"Input: word1 = \"{word1}\", word2 = \"{word2}\", Output: {result}")

if __name__ == "__main__":
    main()
