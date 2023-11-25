number = int(input())
list = []
i = 0
while number > 0:
    i += 1
    max_e_in_shell = 2*i**2
    if number >= max_e_in_shell:
        list.append(max_e_in_shell)
        number -= max_e_in_shell
    else:
        list.append(number)
        number = 0
print(list)