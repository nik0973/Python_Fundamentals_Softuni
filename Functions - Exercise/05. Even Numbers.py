def number_as_digit(number):
    even_digit = []
    for digit in number:
        if int(digit) % 2 == 0:
            even_digit.append(int(digit))
    return even_digit
number_inp = input().split()
print(number_as_digit(number_inp))