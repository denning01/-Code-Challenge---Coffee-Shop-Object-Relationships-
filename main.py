from customer import Customer
from coffee import Coffee
from order import Order

def main():
    customers = {}
    coffees = {}

    while True:
        print("\nOptions:")
        print("1. Add a customer")
        print("2. Add a coffee")
        print("3. Create an order")
        print("4. Show customer orders")
        print("5. Show coffee details")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter customer name: ")
            if name not in customers:
                customers[name] = Customer(name)
                print(f"Customer {name} added.")
            else:
                print("Customer already exists.")

        elif choice == '2':
            name = input("Enter coffee name: ")
            if name not in coffees:
                coffees[name] = Coffee(name)
                print(f"Coffee {name} added.")
            else:
                print("Coffee already exists.")

        elif choice == '3':
            customer_name = input("Enter customer name: ")
            coffee_name = input("Enter coffee name: ")
            price = float(input("Enter order price (1.0 to 10.0): "))

            if customer_name in customers and coffee_name in coffees:
                customer = customers[customer_name]
                coffee = coffees[coffee_name]
                order = customer.create_order(coffee, price)
                print(f"Order created: {order}")
            else:
                print("Customer or coffee does not exist.")

        elif choice == '4':
            customer_name = input("Enter customer name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                orders = customer.orders()
                print(f"{customer_name}'s orders: {orders}")
            else:
                print("Customer does not exist.")

        elif choice == '5':
            coffee_name = input("Enter coffee name: ")
            if coffee_name in coffees:
                coffee = coffees[coffee_name]
                orders = coffee.orders()
                customers_list = coffee.customers()
                print(f"Orders for {coffee_name}: {orders}")
                print(f"Customers who ordered {coffee_name}: {customers_list}")
                print(f"Total number of {coffee_name} orders: {coffee.num_orders()}")
                print(f"Average price of {coffee_name}: {coffee.average_price()}")
            else:
                print("Coffee does not exist.")

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
