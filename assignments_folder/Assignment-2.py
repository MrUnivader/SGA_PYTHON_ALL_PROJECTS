# Initialize available stock dictionary
available_stock = {
    "apple": 50,
    "milk": 20,
    "bread": 15,
    "eggs": 30
}

# List to store the bill details
bill_list = []
total_amount = 0.0

print("--- Grocery Billing System ---")
while True:
    item_name = input("Enter item name (or 'exit' to calculate bill): ").lower()
    
    if item_name == 'exit':
        break
        
    if item_name not in available_stock:
        print("Item not found in inventory.")
        continue
        
    quantity = int(input(f"Enter quantity for {item_name}: "))
    
    # Check if stock is sufficient
    if quantity <= available_stock[item_name]:
        price_per_unit = float(input(f"Enter price per unit for {item_name}: "))
        
        # Store purchase in list of tuples
        bill_list.append((item_name, quantity, price_per_unit))
        
        # Update the stock dictionary
        available_stock[item_name] -= quantity
        
    else:
        print(f"Insufficient stock. Only {available_stock[item_name]} units available.")

# Print the total bill
print("\n--- Final Bill ---")
for item in bill_list:
    i_name, qty, price = item
    cost = qty * price
    total_amount += cost
    print(f"{i_name} : {qty} x {price} = {cost}")

print(f"\nTotal Amount to Pay: {total_amount}")
print(f"Updated Stock: {available_stock}")