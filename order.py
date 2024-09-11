class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer  # Import inside method to avoid circular import
        from coffee import Coffee    # Import inside method to avoid circular import
        
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

        # Add this order to the coffee and customer
        coffee._orders.append(self)
        customer._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"Order(customer={self._customer.name}, coffee={self._coffee.name}, price={self._price})"
