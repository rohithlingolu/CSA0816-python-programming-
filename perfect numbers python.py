def factors(num, m):
    factor_list = [i for i in range(1, num+1) if num % i == 0][:m]
    return factor_list

def is_perfect(num):
    return num == sum(factors(num, -1))

N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

perfect_count = 0
num = 1

while perfect_count < N:
    if is_perfect(num):
        factor_list = factors(num, M)
        print(f"First {M} factors of {num} are: {', '.join(map(str, factor_list))}")
        perfect_count += 1
    num += 1
