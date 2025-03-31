def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for title in sorted(inventory):
        print(f'{title}: {inventory[title]}')

def add_book(inventory):
    title = input("Enter book title: ")
    quantity = int(input("Enter quantity: "))
    inventory[title] = inventory.get(title, 0) + quantity
    print(f'\nAdded "{title}" with quantity {quantity}.')

def remove_book(inventory):
    title = input("Enter book title to remove: ")
    if title in inventory:
        del inventory[title]
        print(f'\nRemoved "{title}" from inventory.')
    else:
        print(f'\n"{title}" not found in inventory.')

def update_quantity(inventory):
    title = input("Enter book title: ")
    if title in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[title] = quantity
        print(f'\nQuantity of "{title}" updated to {quantity}.')
    else:
        print(f'\n"{title}" not found in inventory.')

def search_book(inventory):
    title = input("Enter book title to search: ")
    if title in inventory:
        print(f'\nBook Found - Title: {title}, Quantity: {inventory[title]}')
    else:
        print(f'\n"{title}" not found in inventory.')

inventory = {}

while True:
    print("\nBook Inventory Management")
    print("1. Display Inventory")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Update Quantity")
    print("5. Search for a Book")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        display_inventory(inventory)
    elif choice == "2":
        add_book(inventory)
    elif choice == "3":
        remove_book(inventory)
    elif choice == "4":
        update_quantity(inventory)
    elif choice == "5":
        search_book(inventory)
    elif choice == "6":
        print("\nExiting")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
