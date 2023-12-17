from logic import read_customer_sample, make_customer_file, make_invoces_file, make_invoice_items_file


def genereate_test_files():
    try:
        customers_ids = read_customer_sample()
        make_customer_file(customers_ids)
        invoices = make_invoces_file(customers_ids)
        make_invoice_items_file(invoices)

        print("Test files generated, please check your local directory")
    
    except Exception as e:
        raise e
        


genereate_test_files()        




