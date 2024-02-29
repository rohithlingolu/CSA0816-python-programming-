import re

def is_valid_number(s):
    
    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
    

    return bool(pattern.match(s.strip()))

def main():
    test_cases = ["0", "e", " ", ".", "%", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    
    for s in test_cases:
        result = is_valid_number(s)
        print(f"Input: {s}, Output: {result}")

if __name__ == "__main__":
    main()
