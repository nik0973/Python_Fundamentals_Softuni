def sort_digit(number):
    even_digit = []
    for digit in number:
        even_digit.append(int(digit))
    return sorted(even_digit)
number_inp = input().split()
print(sort_digit(number_inp))