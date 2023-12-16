from readers import read_customer_sample, read_customers, read_invoices, read_invoice_items
from writers import write_new_customers, write_new_invoices, write_new_invoice_items


customer_ids = read_customer_sample()
customers = read_customers(customer_ids)
invoices = read_invoices(customer_ids)
invoice_items = read_invoice_items(invoices)

write_new_customers(customers)
write_new_invoices(invoices)
write_new_invoice_items(invoice_items)
