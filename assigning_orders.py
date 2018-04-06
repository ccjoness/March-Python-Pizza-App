class ReceivedOrder:

    def __init__(self):
        self.customer_name = customer_name()  # assuming there will be a customer name attributed to order
        self.items_ordered = order()  # taking the order given by customer
        self.run()

    def customer_name(self, name):
        #pull the name from the customer order
        return name

    def order(self, items):
        #print items out separated out for easy reading
        return items



