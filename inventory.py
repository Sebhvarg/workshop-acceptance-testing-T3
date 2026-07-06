import sys

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} | Category: {self.category} | Price: ${self.price:.2f} | Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def remove_product(self, name):
        if name not in self.products:
            return False, f"Product '{name}' not found."
        del self.products[name]
        return True, f"Product '{name}' removed successfully."

def main():
    inventory = Inventory()
    
    print("Welcome to Inventory Manager")
    while True:
        print("\n--- Menu ---")
        print("1. Add product")
        print("2. List products")
        print("3. Update quantity")
        print("4. Remove product")
        print("5. Search product")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            name = input("Name: ")
            category = input("Category: ")
            try:
                
            except ValueError:
                print("Error: Price must be a number and Quantity must be an integer.")
                
        elif choice == '4':
            name = input("Product Name: ")
            success, msg = inventory.remove_product(name)
            print(msg)
                
        elif choice == '6':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
