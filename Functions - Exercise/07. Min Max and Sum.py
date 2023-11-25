def sort_digit(number):
    sum_digit = []
    for digit in number:
        sum_digit.append(int(digit))
    return min(sum_digit), max(sum_digit), sum(sum_digit)
number_inp = input().split()
min_number, max_number, sum_number = sort_digit(number_inp)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_number}")