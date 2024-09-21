class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.membership_points = 0

    def add_points(self, points):
        self.membership_points += points
        print(f"{self.name} earned {points} points! Total points: {self.membership_points}")

    def redeem_points(self, points):
        if points <= self.membership_points:
            self.membership_points -= points
            print(f"{self.name} redeemed {points} points! Remaining points: {self.membership_points}")
        else:
            print(f"Not enough points to redeem. {self.name} has only {self.membership_points} points.")

    def __str__(self):
        return f"Customer: {self.name}, Points: {self.membership_points}"


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_products(self):
        print(f"\nProducts available in {self.name}:")
        for product in self.products:
            print(product)

    def purchase(self, customer_name, product_name):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        product = next((p for p in self.products if p.name == product_name), None)

        if customer and product:
            print(f"{customer.name} purchased {product.name} for ${product.price:.2f}")
            customer.add_points(int(product.price))  # Earn 1 point per dollar spent
        else:
            print("Customer or product not found.")


def main():
    store = Store("Local Convenience Store")
    
    # Add products to the store
    store.add_product(Product("Soda", 1.50))
    store.add_product(Product("Chips", 2.00))
    store.add_product(Product("Candy", 0.75))

    # Add customers to the store
    store.add_customer(Customer("Alice"))
    store.add_customer(Customer("Bob"))

    while True:
        print("\nMenu:")
        print("1. Display Products")
        print("2. Purchase Product")
        print("3. Redeem Points")
        print("4. Show Customer Points")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == "1":
            store.display_products()

        elif choice == "2":
            customer_name = input("Enter your name: ")
            product_name = input("Enter the product name you want to purchase: ")
            store.purchase(customer_name, product_name)

        elif choice == "3":
            customer_name = input("Enter your name: ")
            points_to_redeem = int(input("Enter the number of points to redeem: "))
            customer = next((c for c in store.customers if c.name == customer_name), None)
            if customer:
                customer.redeem_points(points_to_redeem)
            else:
                print("Customer not found.")

        elif choice == "4":
            customer_name = input("Enter your name: ")
            customer = next((c for c in store.customers if c.name == customer_name), None)
            if customer:
                print(customer)
            else:
                print("Customer not found.")

        elif choice == "5":
            print("Thank you for visiting the store!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
