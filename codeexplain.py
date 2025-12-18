cart_prices= [1200, 800, 500, 300, 900, 450]
# Calculating total bill amount
total = sum(cart_prices)
print("Total Amount =", total)

# Applying discount if total amount is greater than 500
if total > 500:
    discount = total * 0.10
    total = total - discount
    print("Discount Applied",discount)

# Display final payable amount
print("Pay =", total)