stock = {
    "Apples": 20,
    "Bananas": 30,
    "Oranges": 22,
    "Lemons": 10,
    "Pineapple": 3
}

print("Current Stock:", stock)

while True:
    product = input("Enter an item to check (or type 'exit' to quit): ").capitalize()

    if product.lower() == "exit":
        print("Exiting program. Goodbye!")
        break

    if product in stock:
        print(f"Available stock for {product}: {stock[product]}")
        try:
            quantity = int(input(f"Enter the quantity of {product} you want to buy: "))
            if quantity <= stock[product]:
                stock[product] -= quantity
                print(f"You purchased {quantity} {product}. Remaining: {stock[product]}")
            else:
                print("Not enough stock available.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Product not found.")
