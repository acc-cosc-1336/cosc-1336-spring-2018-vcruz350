'''
Create a product class.
Add a constructor with parameters product_id, cost, and name,
Create public attributes for product_id, cost, and name

STUDENT MUST ALSO MODIFY INVOICE item CLASS TO USE THIS CLASS
SEE INVOICE item file FOR INSTRUCTIONS
'''

class Product:

    def __init__(self, product_id, cost, name):
        self.__product_id = product_id
        self.__cost = cost
        self.__name = name

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_cost(self, cost):
        self.__cost = cost

    def set_name(self, name):
        self.__name = name

    def get_product_id(self):
        return self.__product_id
    def get_cost(self):
        return self.__cost
    def get_name(self):
        return self.__name
    
