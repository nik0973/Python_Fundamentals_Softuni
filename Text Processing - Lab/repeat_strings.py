command = input().split()
repeat_text = [t * len(t) for t in command]
print(''.join(repeat_text))