def min(a, b, c):
# a = int(input())
# b = int(input())
# c = int(input())
    min_num = 0
    if a < b and a < c:
        min_num = a
    elif b < a and b < c:
        min_num = b
    elif c < a and c < b:
        min_num = c
    # print(min_num)
    return min_num
print(min(a=int(input()), b=int(input()), c=int(input())))