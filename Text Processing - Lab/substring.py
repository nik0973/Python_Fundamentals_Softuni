f_string = input()
s_string = input()
while f_string in s_string:
    s_string = s_string.replace(f_string, '')
print(s_string)