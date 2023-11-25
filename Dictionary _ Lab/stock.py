data = input().split()

stock = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i+1])
    stock[product] = quantity

product_to_search = input().split()

for current_product in product_to_search:
    if current_product in stock:
        print(f'We have {stock[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')