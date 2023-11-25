activity = input()
coffee = 0
while activity != "END":
    if activity.lower() == "coding" \
            or activity.lower() == "dog" \
            or activity.lower() == "cat"\
            or activity.lower() == "movie":
        if activity.islower():
            coffee += 1
        elif activity.isupper():
            coffee += 2
        else:
            coffee = coffee
    activity = input()
if coffee > 5:
    print(f"You need extra sleep")
else:
    print(coffee)