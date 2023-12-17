import csv
from models import Customer, Invoice, InvoiceItem


def read_customer_sample(filename) -> set:
    """ This function is ment to read the customer_sample csv file and 
        return a set of customer_codes """
    
    customer_ids = set()

    with open (filename, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            customer_ids.add(row["CUSTOMER_CODE"])

    return customer_ids


def make_customer_file(filename, customer_ids:set) -> list:
    """ This function reads the customer csv file and
            creates a new customer csv file of customers whos customer_code is part of the customers_ids set """

    customers = []

    with open (filename, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row['CUSTOMER_CODE'] in customer_ids:
                customers.append(Customer(row['CUSTOMER_CODE'], row['FIRSTNAME'], row['LASTNAME'] ))

    
    with open ('new_customers.csv', 'w', newline='') as file:
        fieldnames = ['CUSTOMER_CODE', 'FIRSTNAME', 'LASTNAME']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for customer in customers:
            writer.writerow({'CUSTOMER_CODE':customer.customer_code, 'FIRSTNAME':customer.firstname, 'LASTNAME':customer.lastname})

    print("New customer file created")


def make_invoces_file(filename, customer_ids:set) -> list:
    """ This function reads the invoices csv file and
        returns a list of Invoice objects if their customer_codes are in the customer_ids set 
        and writes them to a new invoices csv file """

    invoices = []

    with open (filename,'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row["CUSTOMER_CODE"] in customer_ids:
                invoices.append(Invoice(row['CUSTOMER_CODE'], row['INVOICE_CODE'], row['AMOUNT'], row['DATE']))

    with open('new_invoices.csv', 'w', newline='') as file:
        fieldnames = ['CUSTOMER_CODE', 'INVOICE_CODE', 'AMOUNT', 'DATE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for invoice in invoices:
            writer.writerow({'CUSTOMER_CODE':invoice.customer_code, 'INVOICE_CODE':invoice.invoice_code, 'AMOUNT':invoice.amount, 'DATE': invoice.date})

    print("New invoices file created")
    return invoices


def make_invoice_items_file(filename, invoices:list) -> list:
    """ This function reads the invoce items csv file and 
        returns a list of InvoiceItems objects if their invoice_code is in the list of invoices
        and writes them to a new invoice items csv file """
    
    invoice_items = []
    invoice_ids = [invoice.invoice_code for invoice in invoices]

    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['INVOICE_CODE'] in invoice_ids:
                invoice_items.append(InvoiceItem(row['INVOICE_CODE'], row['ITEM_CODE'], row['AMOUNT'], row['QUANTITY']))

    with open('new_invoice_items.csv', 'w', newline='') as file:
        fieldnames = ['INVOICE_CODE', 'ITEM_CODE', 'AMOUNT', 'QUANTITY']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in invoice_items:
            writer.writerow({'INVOICE_CODE': item.invoice_code, 'ITEM_CODE':item.item_code, 'AMOUNT':item.amount, 'QUANTITY': item.quantity})
    
    print("New invoices items file created")











