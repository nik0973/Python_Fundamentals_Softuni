string_1 = input().split(', ')
string_2 = input().split(', ')
string_new = []
for first in string_1:
    for second in string_2:
        if first in second:
            string_new.append(first)
            break
print(string_new)