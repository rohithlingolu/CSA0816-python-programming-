def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_st = {}
    mapping_ts = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_st:
            if mapping_st[char_s] != char_t:
                return False
        else:
            mapping_st[char_s] = char_t

        if char_t in mapping_ts:
            if mapping_ts[char_t] != char_s:
                return False
        else:
            mapping_ts[char_t] = char_s

    return True

s1 = input("Enter string s: ")
t1 = input("Enter string t: ")
print(isIsomorphic(s1, t1))
