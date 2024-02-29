def is_perfect_square(num):
    return num > 0 and (int(num**0.5))**2 == num

def sum_of_digits_less_than_10(num):
    return sum(int(digit) for digit in str(num)) < 10

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

result_list = [i for i in range(lower_range, upper_range + 1) if is_perfect_square(i) and sum_of_digits_less_than_10(i)]
print(result_list)
