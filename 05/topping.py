requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
available_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese', 'pepperoni', 'pineapple']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}.")
    else :
        print(f"worry, we don't have {requested_topping}.")

print("Finished making your pizza")