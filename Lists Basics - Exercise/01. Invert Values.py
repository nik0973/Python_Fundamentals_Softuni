string = input().split()
opposite_string = []
for number in string:
    current_number = -int(number)
    opposite_string.append(current_number)
print(opposite_string)