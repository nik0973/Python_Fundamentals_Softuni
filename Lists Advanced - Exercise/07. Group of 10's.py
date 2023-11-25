group = [int(n) for n in input().split(", ")]
group_lenght = 10
while len(group) > 0:
    current_list = []
    for number in group:
        if number <= group_lenght:
            current_list.append(number)
    print(f"Group of {group_lenght}'s: {current_list}")
    group = [s for s in group if s not in current_list]
    group_lenght += 10