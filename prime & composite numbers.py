def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

composite_count = 0
prime_count = 0

try:
    num_list = list(map(float, input("Enter the numbers separated by space: ").split()))
    for num in num_list:
        if num.is_integer() and num > 0:
            if is_prime(int(num)):
                prime_count += 1
            else:
                composite_count += 1
except ValueError:
    print("Invalid input. Please enter valid numbers.")

print(f"Composite number: {composite_count} Prime number: {prime_count}")
