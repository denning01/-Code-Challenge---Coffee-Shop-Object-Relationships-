class Customer:
    all_customers = []  # Class variable to keep track of all customers
    
    def __init__(self, name):
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order  # Import inside method to avoid circular import
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
        return top_customer

    def __repr__(self):
        return f"Customer(name={self._name})"
