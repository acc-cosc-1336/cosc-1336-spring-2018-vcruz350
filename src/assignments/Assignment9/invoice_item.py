class InvoiceItem:

    def __init__(self, description, quantity, cost):
        self.description = description
        self.quantity = quantity
        self.cost = cost

    def get_extended_cost(self):
        '''
        Write a statement to multiply quantity * cost and return the result
        :return:  extended cost
        '''
        extended_cost = self.quantity * self.cost
        return extended_cost

    def get_description(self):
        return self.description
