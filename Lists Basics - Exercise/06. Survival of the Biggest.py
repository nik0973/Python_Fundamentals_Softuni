numbers = input().split()
rem_num = int(input())
num_digit = []
for num in range(len(numbers)):
    num_digit.append(int(numbers[num]))
for rem_numbers in range(rem_num):
    current_number = min(num_digit)
    num_digit.remove(current_number)
print(*num_digit, sep=', ')