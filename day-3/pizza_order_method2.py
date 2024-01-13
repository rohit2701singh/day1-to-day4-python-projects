rate = {
    "pizza": {
        "s": 100,
        "m": 150,
        "l": 250,
    },
    "pepperoni": {
        "y": {
            "s": 50,
            "m": 80,
            "l": 120,
        },
        "n": 0
    },
    "cheese": {
        "y": 35,
        "n": 0,
    },
}

user_pizza_size = input("what size pizza? s/m/l: ")

add_pepperoni = input("want pepperoni? y/n: ")
if add_pepperoni == "y":
    pepperoni_size = input("pepperoni size? s/m/l: ")
    pepperoni_price = rate["pepperoni"][add_pepperoni][pepperoni_size]
else:
    pepperoni_price = rate["pepperoni"][add_pepperoni]

add_cheese = input("want cheese?y/n: ")
pizza_price = rate["pizza"][user_pizza_size]

cheese_price = rate["cheese"][add_cheese]

total = pizza_price + pepperoni_price + cheese_price
print(f"your total price is: ${total}")
