import sys
from logic import read_customer_sample, make_customer_file, make_invoces_file, make_invoice_items_file


customer_sample_filename = sys.argv[1]
customer_filename = sys.argv[2]
invoice_filename = sys.argv[3]
invoice_item_filename = sys.argv[4]

def genereate_test_files():
    try:
        customers_ids = read_customer_sample(customer_sample_filename)
        make_customer_file(customer_filename, customers_ids)
        invoices = make_invoces_file(invoice_filename, customers_ids)
        make_invoice_items_file(invoice_item_filename, invoices)

        print("Test files generated, please check your local directory")
    
    except Exception as e:
        raise e
        
genereate_test_files()        




