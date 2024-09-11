class Coffee:
    all_coffees = []  # Class variable to keep track of all coffees
    
    def __init__(self, name):
        self._name = name
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
    
    def __repr__(self):
        return f"Coffee(name={self._name})"
