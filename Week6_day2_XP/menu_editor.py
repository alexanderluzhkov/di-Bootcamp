from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMenu:")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")

        choice = input("Please choose an option: ").strip().upper()
        
        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please choose again.")

def view_item():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item: {item.item_name}, Price: {item.item_price}")
    else:
        print("Item not found.")

def add_item_to_menu():
    name = input("Enter the name of the item to add: ")
    price = int(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    item.save()
    print(f"Item '{name}' was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)
    item.delete()
    print(f"Item '{name}' was deleted successfully.")

def update_item_from_menu():
    old_name = input("Enter the current name of the item to update: ")
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = MenuItem(old_name, 0)
    item.update(new_name, new_price)
    print(f"Item '{old_name}' was updated successfully.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nRestaurant Menu:")
    for item in items:
        print(f"Item: {item.item_name}, Price: {item.item_price}")

if __name__ == "__main__":
    show_user_menu()
