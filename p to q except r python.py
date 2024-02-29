def print_numbers_except_digit(P, Q, R):
    result = []
    for num in range(P, Q + 1):
        if str(R) not in str(num):
            result.append(str(num))

    print("Numbers are =", ", ".join(result))


print_numbers_except_digit(60, 70, 3)

