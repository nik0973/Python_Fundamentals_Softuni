budget = float(input())
price_flour_1kg = float(input())
price_eggs_1pack = price_flour_1kg * 0.75
price_milk_1l = price_flour_1kg * 1.25
price_for_1loaf = price_eggs_1pack + price_flour_1kg + (price_milk_1l * 0.25)
loaves = 0
colored_eggs = 0
remaining_sum = budget
while price_for_1loaf <= budget:
    remaining_sum = budget - price_for_1loaf
    loaves += 1
    budget -= price_for_1loaf
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_sum:.2f}BGN left.")






