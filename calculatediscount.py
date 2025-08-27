def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Only apply discount if it's 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied


# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")