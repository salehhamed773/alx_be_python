#shopping_list.py
#print\(f?['\"]Shopping\s*List\s*Manager['\"]\)
#print\(f?['\"]1.\s*Add\s*Item['\"]\)
def display_menu():
    print("/nShopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")
def main():
    shopping_list=[] # Initialize an empty shopping list
    while True:
        display_menu() # Display the menu
        choice= input("Choose an option (1-4): ")
        if (choice == 1):
            item=input("Enter the item name to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping lis.")
        elif (choice == 2):
            item =input("Enter the item name to remove: ")
            if (item in shopping_list):
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif (choice == 3):
            print("Current shopping list: ")
            if shopping_list:
                for i,item in enumerate(shopping_list,start=1):
                    print(f"{i}.{item}")
            else:
                print("The shopping list is empty.")
        elif (choice == 4):
            print("Exiting the program . Goodbye!")
            break   
        else:
              print("Invalid choice. Please choose a valid option (1-4).")
if __name__ == "__main__":
    main()
        
