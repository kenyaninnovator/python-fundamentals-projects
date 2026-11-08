# Game Shop Inventory Manager

# 1. Our shop database using a Python Dictionary
shop_inventory = {
    "health potion": 10,
    "iron sword": 3,
    "shield": 5
}

print("=== WELCOME TO THE SHOP MANAGEMENT SYSTEM ===")
print(f"Current Stock Levels: {shop_inventory}")

# 2. Take user input to see what item they want to manage
item_to_check = input("\nWhich item do you want to manage? (health potion / iron sword / shield): ").lower()

if item_to_check in shop_inventory:
    print(f"\n[FOUND] We currently have {shop_inventory[item_to_check]} units of '{item_to_check}' left.")
    
    # 3. Action logic for managing stock
    action = input("Type 'add' to restock or 'sell' to decrease stock: ").lower()
    
    if action == "add":
        shop_inventory[item_to_check] += 1
        print(f"✔️ Restocked! New '{item_to_check}' count: {shop_inventory[item_to_check]}")
    elif action == "sell":
        if shop_inventory[item_to_check] > 0:
            shop_inventory[item_to_check] -= 1
            print(f"💵 Item sold! New '{item_to_check}' count: {shop_inventory[item_to_check]}")
        else:
            print("❌ Error: Out of stock! Cannot sell this item.")
    else:
        print("❌ Invalid command. Only 'add' or 'sell' are allowed.")
else:
    print("❌ Error: That item does not exist in our shop database.")
