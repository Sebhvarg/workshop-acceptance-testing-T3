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

    def update_quantity(self, name, new_quantity):
        if name not in self.products:
            return False, f"Product '{name}' not found."
        self.products[name].quantity = int(new_quantity)
        return True, f"Quantity of '{name}' updated to {new_quantity}."
    def remove_product(self, name):
        if name not in self.products:
            return False, f"Product '{name}' not found."
        del self.products[name]
        return True, f"Product '{name}' removed successfully."
    def add_product(self, name, category, price, quantity):
        if name in self.products:
            return False, f"Product '{name}' already exists."
        self.products[name] = Product(name, category, price, quantity)
        return True, f"Product '{name}' added successfully."
    def search_product(self, name):
        """Feature 5: Search for a specific product by name"""
        if name not in self.products:
            return False, f"Product '{name}' not found."
        return True, self.products[name]  
    
    def list_products(self):
        return list(self.products.values())
   
   

def main():
    inventory = Inventory()
    inventory.add_product(Product("Coffee", "Beverage", 5.5, 10))
    inventory.add_product(Product("Sugar", "Food", 2.0, 20))

    
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
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                _, msg = inventory.add_product(name, category, price, quantity)
                print(msg)
            except ValueError:
                print("Error: Price must be a number and Quantity must be an integer.")
        
        elif choice == '3':
            name = input("Product Name: ")
            try:
                quantity = int(input("New Quantity: "))
                success, msg = inventory.update_quantity(name, quantity)
                print(msg)
            except ValueError:
                print("Error: Quantity must be an integer.")
                
        elif choice == '4':
            name = input("Product Name: ")
            success, msg = inventory.remove_product(name)
            print(msg)

        elif choice == '5':
            name = input("Product Name: ")
            success, result = inventory.search_product(name)
            if success:
                print(f"Found: {result}")
            else:
                print(result)

        elif choice == '2':
            products = inventory.list_products()
            if not products:
                print("Inventory is empty.")
            else:
                for p in products:
                    print(p)

        elif choice == '6':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
