# -*- coding: utf-8 -*-
"""cart.ipy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SWvIeUUz-IFcaD51TH0fD3hlnH89Wl-R
"""

# Catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount Rules
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 0.05,
    "bulk_10_discount": 0.1,
    "tiered_50_discount": 0.5
}

# Fees
gift_wrap_fee_per_unit = 1
shipping_fee = 5
units_per_package = 10

# Function to calculate the discount amount
def calculate_discount(quantity, price, rule):
    if rule == "flat_10_discount":
        return min(10, quantity * price)
    elif rule == "bulk_5_discount" and quantity > 10:
        return quantity * price * discount_rules[rule]
    elif rule == "bulk_10_discount" and quantity > 20:
        return quantity * price * discount_rules[rule]
    elif rule == "tiered_50_discount" and quantity > 30:
        return (quantity - 15) * price * discount_rules[rule]
    else:
        return 0

# Function to calculate the total cost
def calculate_total_cost(cart):
    subtotal = 0
    discount_name = ""
    discount_amount = 0
    gift_wrap_total = 0

    for product, quantity, is_gift_wrapped in cart:
        price = catalog[product]
        total_amount = quantity * price
        subtotal += total_amount

        # Check which discount rule is applicable
        for rule in discount_rules:
            discount = calculate_discount(quantity, price, rule)
            if discount > discount_amount:
                discount_amount = discount
                discount_name = rule

        # Add gift wrap fee
        gift_wrap_total += quantity * gift_wrap_fee_per_unit

        # Calculate shipping fee
        packages = (quantity - 1) // units_per_package + 1
        shipping_fee_total = packages * shipping_fee

        # Output details for each product
        print(f"Product: {product}\nQuantity: {quantity}\nTotal Amount: ${total_amount}\n")

    # Output overall details
    print("----------------------------")
    print(f"Subtotal        :  ${subtotal}")
    print(f"Discount Applied: {discount_name} (${discount_amount})")
    print(f"Shipping Fee    : ${shipping_fee_total}")
    print(f"Gift Wrap Fee   : ${gift_wrap_total}")
    print(f"Total           : ${subtotal - discount_amount + shipping_fee_total + gift_wrap_total}")

# Main program
cart = []

# Gather product quantity and gift wrap information
for product, _ in catalog.items():
    quantity = int(input(f"Enter quantity for {product}: "))
    is_gift_wrapped = input(f"Is {product} gift wrapped? (y/n): ").lower() == "y"
    cart.append((product, quantity, is_gift_wrapped))

# Calculate and display the total cost
calculate_total_cost(cart)