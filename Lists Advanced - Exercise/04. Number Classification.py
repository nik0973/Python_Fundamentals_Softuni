def positive_num(num_list):
    return ', '.join([n for n in num_list if int(n) >= 0])

def negative_num(num_list):
    return ', '.join([n for n in num_list if int(n) < 0])

def even_num(num_list):
    return ', '.join([n for n in num_list if int(n) % 2 == 0])

def odd_num(num_list):
    return ', '.join([n for n in num_list if int(n) % 2 != 0])

list_numbers = input().split(", ")
print(f"Positive: {positive_num(list_numbers)}")
print(f"Negative: {negative_num(list_numbers)}")
print(f"Even: {even_num(list_numbers)}")
print(f"Odd: {odd_num(list_numbers)}")