def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_primes(A, B):
    for num in range(A, B + 1):
        if not is_prime(num):
            print(num)

# Replace A and B with your desired range
A = 10
B = 30
print_non_primes(A, B)
