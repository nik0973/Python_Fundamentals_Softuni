version = [int(n) for n in input().split('.')]
version[-1] += 1
for n in range(len(version)-1, 0, -1):
    if version[n] > 9:
        version[n] = 0
        if n -1 >= 0:
            version[n-1] += 1
print(".".join(str(j) for j in version))