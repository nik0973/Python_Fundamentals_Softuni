def sum_numbers(first, second):
    return first + second

def substract(result, third):
    return result - third

def add_and_substract(first, second, third):
    return_sum = sum_numbers(first, second)
    final_result = substract(return_sum, third)
    return final_result

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_substract(first_number, second_number, third_number))