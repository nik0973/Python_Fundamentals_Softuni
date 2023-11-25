factor = int(input())
count = int(input())
list = []
for i in range(1, count + 1):
    current_num = i * factor
    list.append(current_num)
print(list)