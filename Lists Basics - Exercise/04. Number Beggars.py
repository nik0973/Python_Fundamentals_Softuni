amount = input().split(', ')
beggars = int(input())
amount_digits = []
for current_amount in amount:
    amount_digits.append(int(current_amount))
final_sum = []
start_index = 0
while start_index < beggars:
    current_sum = 0
    for current_index in range(start_index, len(amount_digits), beggars):
        current_sum += amount_digits[current_index]
    final_sum.append(current_sum)
    start_index += 1
print(final_sum)

