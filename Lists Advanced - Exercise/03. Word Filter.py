some_str = input().split()
new_str = [n for n in some_str if len(n) % 2 == 0]
print('\n'.join(new_str))