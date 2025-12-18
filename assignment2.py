# List of the available products and their prices

products = ["Shoes", "Bag", "Watch", "T-Shirt", "Jeans", "Perfume"]
prices = [1200, 800, 500, 300, 900, 450]

# Empty lists to store cart items and prices
cart = []
cart_prices = []

# Display available products
print("Available Products:")
for i in range(len(products)):
    print(i, "-", products[i], "₹", prices[i])
    

# Loop to add products to cart
while True:
    # Asking the user to enter product number or type 'done'
    choice = input("Enter product number to add or 'done' to stop: ")

    # If user enters 'done', stop adding products
    if choice.lower() == "done":
        break

    # Converting input to integer
    choice = int(choice)

    # Adding selected product and its price to cart
    cart.append(products[choice])
    cart_prices.append(prices[choice])

    # Display confirmation message
    print(products[choice], "added to cart")

# Loop to view and modify the cart
while True:
    # Display current cart items
    print("\nYour cart items:")
    for i in range(len(cart)):
        print(i, "-", cart[i], "₹", cart_prices[i])

    # Asking if the user wants to remove any item
    remove_item = input("Do you want to remove any item? (yes/no): ")

    # If user wants to remove an item
    if remove_item.lower() == "yes":
        # Taking index of item to remove
        remove_index = int(input("Enter item number to remove: "))

        # Removing the selected item and its price from cart
        cart.pop(remove_index)
        cart_prices.pop(remove_index)
        print("Item removed")
        continue

    # Asking the user if they want to proceed with billing
    proceed = input("Do you want to proceed with bill? (yes/no): ")

    # If user proceeds to billing
    if proceed.lower() == "yes":
        print("Final Cart Items:")
        
        # Displaying final items
        for item in cart:
            print(item)
        break
    else:
        # If user does not want to proceed
        print("Back to cart modification")

# Calculating total bill amount
total = sum(cart_prices)
print("Total Amount =", total)

# Applying discount if total amount is greater than 500
if total > 500:
    discount = total * 0.10
    total = total - discount
    print("Discount Applied")

# Display final payable amount
print("Pay =", total)

# Displays a polite message to the user at the end
print("Thank you for visiting!")