import csv


def write_new_customer_file(customers) -> csv:
    """ This function takes the Customer object list and writes it into a csv file """
    
    with open ('new_customers.csv', 'w', newline='') as file:
        fieldnames = ['CUSTOMER_CODE', 'FIRSTNAME', 'LASTNAME']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for customer in customers:
            writer.writerow({'CUSTOMER_CODE':customer.customer_code, 'FIRSTNAME':customer.firstname, 'LASTNAME':customer.lastname})


def write_new_invoices_files(invoices) -> csv:
    """ This function takes the Invoice objects list and writes it into a csv file """

    with open('new_invoices.csv', 'w', newline='') as file:
        fieldnames = ['CUSTOMER_CODE', 'INVOICE_CODE', 'AMOUNT', 'DATE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for invoice in invoices:
            writer.writerow({'CUSTOMER_CODE':invoice.customer_code, 'INVOICE_CODE':invoice.invoice_code, 'AMOUNT':invoice.amount, 'DATE': invoice.date})


def write_new_invoice_items_file(invoice_items) -> csv:
    """ This function takes the InvoiceItems objects list and writes it into a csv file """

    with open('new_invoice_items.csv', 'w', newline='') as file:
        fieldnames = ['INVOICE_CODE', 'ITEM_CODE', 'AMOUNT', 'QUANTITY']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in invoice_items:
            writer.writerow({'INVOICE_CODE': item.invoice_code, 'ITEM_CODE':item.item_code, 'AMOUNT':item.amount, 'QUANTITY': item.quantity})

        
