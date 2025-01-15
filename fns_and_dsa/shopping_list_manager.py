shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Example usage:
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        elif choice == "1":
            item = input("Enter the item to add: ").strip()
            print(f"Item '{item}' added to the list.")
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            print(f"Item '{item}' removed from the list.")
        elif choice == "3":
            print("Displaying the shopping list...")
        else:
            print("Invalid choice. Please try again.")
    
        
