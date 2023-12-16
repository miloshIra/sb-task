from writers import write_new_customer_file, write_new_invoice_items_file, write_new_invoices_files
from readers import read_customer_sample, read_customer_file, read_invoces_file, read_invoice_items_file


def genereate_test_files():
    try:
        customers_ids = read_customer_sample()
        customers = read_customer_file(customers_ids)
        invoices = read_invoces_file(customers_ids)
        invoice_items = read_invoice_items_file(invoices)

        write_new_customer_file(customers)
        write_new_invoices_files(invoices)
        write_new_invoice_items_file(invoice_items)

        print("Test files generated, please check your local directory")
    
    except Exception as e:
        raise e
        


genereate_test_files()        




