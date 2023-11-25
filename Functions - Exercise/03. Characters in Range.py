def between_char(first: str, second: str):
    char_list = []
    for current_digit in range(ord(first) + 1, ord(second)):
        char_list.append(chr(current_digit))
    return(char_list)
first_char = input()
second_char = input()
final_result = between_char(first_char, second_char)
print(" ".join(final_result))