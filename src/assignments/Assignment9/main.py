#Write import statements for classes invoice and invoice_item
from invoice import Invoice
from invoice_item import InvoiceItem
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
invoice = Invoice('ABC Company', '328218')

def main():
    
    keep_going = 'y'

    while keep_going == 'y':
        description = input("Enter item description: ")
        quantity = int(input("Enter qty: "))
        cost = float(input("Enter cost: "))

        invoice_item = InvoiceItem(description, quantity, cost)
        invoice.add_invoice_item(invoice_item)

        keep_going = input("Press y to continue... ")
        
        if keep_going != 'y':
            invoice.print_invoice()

main()
