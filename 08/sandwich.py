def order_sandwich(*toppings):
    print(f"\nOrder sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
order_sandwich('pepperoni')
order_sandwich('geeen peppers', 'extra cheese')
order_sandwich('mushrooms', 'geeen peppers', 'extra cheese')