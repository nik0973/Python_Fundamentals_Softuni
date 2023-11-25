string1 = input()
string2 = input()
last_printed_string = string1
for character in range(len(string1)):
    left_part = string2[:character + 1]
    right_part = string1[character + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string