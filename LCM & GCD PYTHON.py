import math

def find_lcm(numbers):
    lcm = 1
    for number in numbers:
        lcm = lcm * number // math.gcd(lcm, number)
    return lcm

def find_gcd(numbers):
    gcd = numbers[0]
    for number in numbers[1:]:
        gcd = math.gcd(gcd, number)
    return gcd



numbers = list(map(int, input("Enter space-separated numbers: ").split()))


print("LCM:", find_lcm(numbers))
print("GCD:", find_gcd(numbers))
