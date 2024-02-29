def find_common_divisors(a, b):
    common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    return common_divisors

numbers = input("Enter the numbers separated by comma: ").split(',')
num1, num2 = int(numbers[0]), int(numbers[1])

common_divisors = find_common_divisors(num1, num2)
print(len(common_divisors))
