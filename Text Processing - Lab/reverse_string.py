# while True:
#     command = input()
#     if command == 'end':
#         break
#     print(f'{command} = {command[::-1]}')
command = input()
while command != 'end':
    reversed_string = ''
    for ch in reversed(command):
        reversed_string += ch
    print(command + ' = ' + reversed_string)
    command = input()