# Add items to the cart
def add_item(cart):
    item = input("Enter the item name: ")
    price = float(input(f"Enter the price for {item}:"))
    if price > 0:
        cart[item] = price
        print(f"'{item}' has been added to the cart at {price}.")
    else:
        print("Please enter a valid price.")
    return cart
# View items in the cart
def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for item, price in cart.items():
            print(f"{item}: {price}")
    return cart
# Calculate the total price
def calculate_total(cart):
    total = sum(cart.values())
    print(f"The total price of your cart is: {total}")
    return total
# Main shopping cart simulation function
def main():
    cart = {}  # Initialize an empty cart
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Choose an option : ")

        if choice == "1":
            cart = add_item(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            calculate_total(cart)
        elif choice == "4":
            print("Thank you for shopping with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# call the main function to start the simulation
main()
