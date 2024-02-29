def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            sign = 1
            num = 0
        elif char == '-':
            result += sign * num
            sign = -1
            num = 0
        elif char == '*':
            num = stack.pop() * num
        elif char == '/':
            num = int(stack.pop() / num)
        elif char == ' ':
            continue

    result += sign * num
    return result

# Test cases
print(calculate("3+2*2"))  # Output: 7
print(calculate(" 3/2 "))  # Output: 1
print(calculate(" 3+5 / 2 "))  # Output: 5
print(calculate("-1+5"))  # Output: 4
