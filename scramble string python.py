def isScramble(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False

    if s1 == s2:
        return True

    length = len(s1)

    for i in range(1, length):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[length-i:]) and isScramble(s1[i:], s2[:length-i])):
            return True

    return False

# Test case
s1 = "great"
s2 = "eatgr"
result = isScramble(s1, s2)
print(f"Input: s1 = \"{s1}\", s2 = \"{s2}\", Output: {result}")
