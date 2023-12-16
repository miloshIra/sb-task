import csv
from models import Customer, Invoice, InvoiceItem


def read_customer_sample() -> set:
    """ This function is ment to read the customer_sample csv file and 
        return a set of customer_codes """
    
    customer_ids = set()

    with open ('customer_sample.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            customer_ids.add(row["CUSTOMER_CODE"])

    return customer_ids


def read_customer_file(customer_ids:set) -> list:
    """ This function reads the customer csv file and
            returns a list of customers whos customer_code is part of the customers_ids set """

    customers = []

    with open ('customer.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row['CUSTOMER_CODE'] in customer_ids:
                customers.append(Customer(row['CUSTOMER_CODE'], row['FIRSTNAME'], row['LASTNAME'] ))

    return customers


def read_invoces_file(customer_ids:set) -> list:
    """ This function reads the invoices csv file and
        returns a list of Invoice objects if their customer_codes are in the customer_ids set """

    invoices = []

    with open ('invoice.csv','r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row["CUSTOMER_CODE"] in customer_ids:
                invoices.append(Invoice(row['CUSTOMER_CODE'], row['INVOICE_CODE'], row['AMOUNT'], row['DATE']))

    return invoices


def read_invoice_items_file(invoices:list) -> list:
    """ This function reads the invoce items csv file and 
        returns a list of InvoiceItems objects if their invoice_code is in the list of invoices """
    
    invoice_items = []
    invoice_ids = [invoice.invoice_code for invoice in invoices]

    with open('invoice_items.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['INVOICE_CODE'] in invoice_ids:
                invoice_items.append(InvoiceItem(row['INVOICE_CODE'], row['ITEM_CODE'], row['AMOUNT'], row['QUANTITY']))
    
    return invoice_items











