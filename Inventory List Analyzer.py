def inventory_list_analyzer():
    inventory = []

    print("Welcome to Inventory List Analyzer!")

    while True:
        item = {}
        item['name'] = input("Enter item name: ").strip()
        item['category'] = input("Enter category: ").strip().lower()
        item['quantity'] = int(input("Enter quantity: "))
        inventory.append(item)

        choice = input("Do you want to add more items? (y/n): ")
        if choice.lower() != 'y':
            break

    print("\n========== INVENTORY SUMMARY ==========")

    # Total different items
    total_items = len(inventory)
    print(f"Total Different Items: {total_items}")
    item_names = ', '.join([item['name'] for item in inventory])
    print(f"Explanation: You entered {total_items} different items: {item_names}.")

    # Total quantity
    total_quantity = sum(item['quantity'] for item in inventory)
    print(f"\nTotal Quantity in Stock: {total_quantity}")
    print("Explanation: Sum of all quantities: " +
          " + ".join(str(item['quantity']) for item in inventory) + f" = {total_quantity}")

    # Average quantity
    avg_quantity = total_quantity / total_items
    print(f"\nAverage Quantity per Item: {avg_quantity}")
    print(f"Explanation: Average = {total_quantity} total / {total_items} items")

    # Most and least stocked
    most_stocked = max(inventory, key=lambda x: x['quantity'])
    least_stocked = min(inventory, key=lambda x: x['quantity'])

    print(f"\nMost Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
    print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.")

    print(f"\nLeast Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
    print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

    # Unique categories
    unique_categories_set = {item['category'] for item in inventory}
    print("\n---------------------------------------")
    print(f"Unique Categories in Inventory: {unique_categories_set}")
    print("Explanation: Categories are taken from user input and converted to lowercase.")
    print("No duplicates are shown here.")

    # Sort by quantity (High to Low)
    print("\n---------------------------------------")
    print(" Items Sorted by Quantity (High to Low):")
    sorted_items = sorted(inventory, key=lambda x: x['quantity'], reverse=True)
    for i, item in enumerate(sorted_items, start=1):
        print(f"{i}. {item['name']} - {item['quantity']} units")
    print("Explanation: Items are sorted using the quantity field from highest to lowest.")

    # Categories in alphabetical order
    print("\n---------------------------------------")
    print(" Categories in Alphabetical Order:")
    sorted_categories = sorted(unique_categories_set)
    for i, category in enumerate(sorted_categories, start=1):
        print(f"{i}. {category}")
    print("Explanation: The set of unique categories was sorted alphabetically for display.")

    print("\n=========== END OF REPORT ===========")

# Run the program
inventory_list_analyzer()
