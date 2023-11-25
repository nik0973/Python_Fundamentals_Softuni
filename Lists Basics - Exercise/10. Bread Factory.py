events = input().split("|")
total_coines = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_item = event.split("-")
    type_of_event = event_item[0]
    event_value = int(event_item[1])
    #type_of_event, event_value = event.split("-")
    #event_value = int(event_value)
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coines += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coines >= event_value:
            total_coines -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_is_open = False
            break
if factory_is_open:
    print(f"Day completed!")
    print(f"Coins: {total_coines}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {type_of_event}.")