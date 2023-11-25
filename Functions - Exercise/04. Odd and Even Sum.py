def odd_and_even(num: list):
    odd_sum = 0
    even_sum = 0
    for number in num:
        v = int(number)
        if v % 2 != 0:
            odd_sum += v
        else:
            even_sum += v
    return odd_sum, even_sum
number = input()
sum_of_odd, sum_of_even = odd_and_even(number)
print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")