class Order:

    def __init__(self, index, customer_name, order_date, quantity, type, origin):
        self.index = index
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.type = type
        self.origin = origin