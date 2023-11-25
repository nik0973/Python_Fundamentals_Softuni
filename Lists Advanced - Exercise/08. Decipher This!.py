secret_messagge = input().split()
message = []
for word in secret_messagge:
    char_digit = ""
    char = ""
    for i in word:
        if i.isdigit():
            char_digit += i
        else:
            char += i

    letter_from_digit = chr(int(char_digit))
    if len(char) != 1:
        new_word = f"{char[-1]}{char[1:-1]}{char[0]}"
    else:
        new_word = char
    new_word = letter_from_digit + new_word
    message.append(new_word)

print(*message)