'''
Create a customer class
Add a constructor with parameters first, last, and phone_number
Create public attributes for first, last, and phone_number

STUDENT MUST ALSO MODIFY INVOICE CLASS TO USE THIS CLASS
SEE INVOICE file FOR INSTRUCTIONS
'''

class Customer:
    def __init__(self, first, last, phone_number):
        self.__first = first
        self.__last = last
        self.__phone_number = phone_number

    def set_first(self, first):
        self.__first = first

    def set_last(self, last):
        self.__last = last

    def set_phone_number(self, pone_number):
        self.phone_number = phone_number

    def get_first(self):
        return self.__first
    def get_last(self):
        return self.__last
    def get_phone_number(self):
        return self.__phone_number
