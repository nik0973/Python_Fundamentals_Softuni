def sort_list(sors_list):
    for digit in sors_list:
        # digit_str = str(digit[::1])
        reverse_number = str(digit[::-1])
        rev_dig_number = int(reverse_number)
        if int(digit) == rev_dig_number:
            print(True)
        else:
            print(False)
num_list = input().split(',')
sort_list(num_list)