# simple E-commerce cart system.

#lists of available products with price.
products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphone": 2000,
    "Keyboard": 1500
}

#Empty cart dictionary
cart = {}

def show_menu():
    print("\n--- E-Commerce CART MENU ---")
    print("1. View products")
    print("2. Add  to cart")
    print("3. View cart")
    print("4. Remove from cart")
    print("5. Total Bill")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    #view products
    if choice == "1":
        print("\nAvailable Products:")
        for item, price in products.items():
            print(f"{item} - {price}")

    #add to cart
    elif choice == "2":
        item = input("Enter Product name to add:")
        if item in products:
            cart[item] = products[item]
            print(f"{item} added to cart.")
        else:
            print("Product not found.")

    #view to cart.
    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("\n Your cart:")
            for item, price in cart.iems():
                print(f"{item} - {price}")

    #Remove from cart.
    elif choice == "4":
        item = input("Enter product name to remove:")
        if item in cart:
            cart.pop(item)
            print(f"{item} removed from cart.")
        else:
            print("Item not in cart.")

    #Total bill
    elif choice =="5":
        total = sum(cart.values())
        print(f"Total Amount: {total}")

    #exit
    elif choice == "6":
        print("Thank you for shopping! Goodbye.")
        break
    else:
        print("Invalid choice. Please try again. ")
