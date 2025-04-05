import os  # Importing the 'os' module to clear the screen for a better receipt display

# Define the product catalog as a dictionary
# Each product has a name, price, and stock quantity
products = {
    "Milk": {"price": 500, "stock": 10},
    "Bread": {"price": 300, "stock": 8},
    "Rice": {"price": 1200, "stock": 15},
    "Sugar": {"price": 700, "stock": 5},
    "Flour": {"price": 400, "stock": 12},
    "Eggs": {"price": 150, "stock": 30},
    "Chicken": {"price": 2500, "stock": 7},
    "Beef": {"price": 3500, "stock": 5},
    "Fish": {"price": 2000, "stock": 6},
    "Juice": {"price": 800, "stock": 10},
}

# Initialize an empty shopping cart (dictionary)
cart = {}

def display_products():
    """Display all available products, including their price and stock."""
    print("\nAvailable Products:")
    print(f"{'Product':<15}{'Price':<10}{'Stock':<10}")
    print("-" * 35)

    # Iterate through the product catalog and display each item
    for product, details in products.items():
        print(f"{product:<15}${details['price']:<10}{details['stock']:<10}")

    print("-" * 35)

def add_to_cart():
    """Allow the cashier to add products to the shopping cart while checking stock availability."""
    product = input("Enter product name: ").strip().title()  # Get product name and format it properly

    # Check if the product exists in the catalog
    if product in products:
        try:
            quantity = int(input("Enter quantity: "))  # Convert input to an integer

            # Validate if the requested quantity is within available stock
            if 0 < quantity <= products[product]["stock"]:
                # If the product is already in the cart, update the quantity
                if product in cart:
                    cart[product]["quantity"] += quantity
                else:
                    # Add new product entry to the cart
                    cart[product] = {"price": products[product]["price"], "quantity": quantity}

                # Deduct the purchased quantity from stock
                products[product]["stock"] -= quantity
                print(f"{quantity} {product}(s) added to cart.")
            else:
                print("Invalid quantity. Check stock availability.")
        except ValueError:
            print("Invalid input. Please enter a numeric quantity.")
    else:
        print("Product not found.")

def remove_from_cart():
    """Allow the cashier to remove an item from the shopping cart and restock it."""
    product = input("Enter product name to remove: ").strip().title()

    # Check if the product is in the cart
    if product in cart:
        quantity = cart[product]["quantity"]  # Get the quantity of the product in the cart

        # Restock the removed quantity back to the available stock
        products[product]["stock"] += quantity

        # Remove the item from the cart
        del cart[product]
        print(f"{product} removed from cart.")
    else:
        print("Product not in cart.")

def view_cart():
    """Display all items in the shopping cart, along with their total prices."""
    if not cart:  # Check if the cart is empty
        print("\nCart is empty.")
        return

    print("\nShopping Cart:")
    print(f"{'Product':<15}{'Quantity':<10}{'Unit Price':<10}{'Total':<10}")
    print("-" * 50)

    total = 0  # Initialize total amount
    for product, details in cart.items():
        total_price = details["price"] * details["quantity"]  # Calculate total price for the product
        total += total_price  # Add to the running total
        print(f"{product:<15}{details['quantity']:<10}{details['price']:<10}${total_price:<10}")

    print("-" * 50)
    print(f"Subtotal: ${total:.2f}")  # Display subtotal amount

def checkout():
    """Calculate the total amount, apply discount and tax, and process the payment."""
    if not cart:  # Check if the cart is empty before proceeding
        print("Cart is empty. Add items before checkout.")
        return

    # Calculate the subtotal (sum of all item prices in the cart)
    subtotal = sum(details["price"] * details["quantity"] for details in cart.values())

    # Apply a 5% discount if the subtotal is greater than $5000
    discount = 0.05 * subtotal if subtotal > 5000 else 0

    # Calculate 10% sales tax on the discounted total
    tax = 0.10 * (subtotal - discount)

    # Compute the final total amount due
    total_due = (subtotal - discount) + tax

    # Display checkout summary
    print("\nCheckout Summary:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount (5% for bills over $5000): -${discount:.2f}")
    print(f"Sales Tax (10%): +${tax:.2f}")
    print(f"Total Amount Due: ${total_due:.2f}")

    # Loop for payment processing
    while True:
        try:
            amount_paid = float(input("Enter amount received: "))  # Get the payment amount from the cashier
            if amount_paid >= total_due:  # Ensure that the payment is enough
                change = amount_paid - total_due  # Calculate change
                generate_receipt(subtotal, discount, tax, total_due, amount_paid, change)  # Print receipt
                cart.clear()  # Clear the cart after successful transaction
                break
            else:
                print("Insufficient payment. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

def generate_receipt(subtotal, discount, tax, total_due, amount_paid, change):
    """Generate and print a formatted receipt for the transaction."""
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen for better readability
    print("\n" + "=" * 40)
    print("      XYZ Supermarket - Receipt")
    print("=" * 40)

    # Display each product purchased
    for product, details in cart.items():
        total_price = details["price"] * details["quantity"]
        print(f"{product:<15} x{details['quantity']} @ ${details['price']} = ${total_price:.2f}")

    print("-" * 40)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Sales Tax: +${tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Change: ${change:.2f}")
    print("=" * 40)
    print("      Thank you for shopping with us!")
    print("=" * 40)

def main():
    """Main menu loop for the POS system."""
    while True:
        print("\n=== Point of Sale (POS) System ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")  # Get user menu choice
        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting system. Have a great day!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

# Run the main function when the script starts
if __name__ == "__main__":
    main()
