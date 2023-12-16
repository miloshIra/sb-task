
class Customer():
    def __init__(self, customer_code:str, firstname:str, lastname:str):
        self.customer_code = customer_code
        self.firstname = firstname
        self.lastname = lastname


class Invoice():
    def __init__(self, customer_code:str, invoice_code:str, amount:float, date:str):
        self.customer_code = customer_code
        self.invoice_code = invoice_code
        self.amount = amount
        self.date = date


class InvoiceItem():
    def __init__(self, invoice_code:str, item_code:str, amount:float, quantity:int):
        self.invoice_code = invoice_code
        self.item_code = item_code
        self.amount = amount
        self.quantity = quantity



