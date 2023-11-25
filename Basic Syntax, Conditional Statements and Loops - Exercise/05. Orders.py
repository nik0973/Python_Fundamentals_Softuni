number_of_orders = int(input())
price_total = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or \
            days < 1 or days > 31 or capsules < 1 or capsules > 2000:
        continue
    price = price_per_capsule * days * capsules
    print(f"The price for the coffee is: ${price:.2f}")
    price_total += price
print(f"Total: ${price_total:.2f}")



