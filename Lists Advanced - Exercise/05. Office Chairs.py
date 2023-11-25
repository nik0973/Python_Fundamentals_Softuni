def check_chairs(rooms):
    free_chairs = 0
    for number in range(1, rooms +1):
        free, chairs = input().split()
        dif = len(free) - int(chairs)
        if dif < 0:
            print(f"{abs(dif)} more chairs needed in room {number}")
        free_chairs += dif
    return free_chairs

rooms_count = int(input())
total = check_chairs(rooms_count)
if total >= 0:
    print(f"Game On, {total} free chairs left")


