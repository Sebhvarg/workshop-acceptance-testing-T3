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

    def add_product(self, product):
        self.products[product.name] = product    
    
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

                product = Product(name, category, price, quantity)
                inventory.add_product(product)

                print("Product added successfully.")

            except ValueError:
                print("Error: Price must be a number and Quantity must be an integer.")

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
