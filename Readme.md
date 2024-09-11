# readme 
Coffee Order Management System
This is a simple Coffee Order Management System implemented in Python. It allows users to add customers, add different types of coffee, create orders for customers, and view details about customer orders and coffee statistics.


Options in the Menu
Add a Customer: Enter the customer's name to add them to the system.
Add a Coffee: Enter the name of the coffee to add it to the system.
Create an Order: Provide the customer's name, coffee name, and price to create an order.
Show Customer Orders: View all orders associated with a specific customer.
Show Coffee Details: View all orders for a specific coffee, the customers who ordered it, the total number of orders, and the average price.
Exit: Exit the application.
Classes Overview
The system is built around three main classes:

Customer:

Represents a customer.
Has a name property.
Contains methods for creating and managing customer orders.
Coffee:

Represents a type of coffee.
Has a name property.
Contains methods for managing and analyzing coffee orders.
Order:

Represents an order made by a customer for a specific type of coffee.
Contains information about the customer, coffee, and price.
Functionality
Adding Customers and Coffees:

Customers and coffees are stored in dictionaries (customers and coffees) with their names as keys.
Creating an Order:

When creating an order, the customer and coffee names are validated against the existing records to ensure they exist.
The order is created with a valid price between 1.0 and 10.0.
Displaying Orders and Coffee Details:

The system allows viewing all orders of a specific customer.
Coffee statistics such as total orders and average price are displayed for analysis.
