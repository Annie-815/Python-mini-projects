from datetime import datetime

def generate_invoice():
    print("\n=== Invoice Generator ===\n")

    # Company details (customize as needed)
    company_name = "Your Company Name"
    company_address = "123 Tech Lane, Nairobi, Kenya"
    company_email = "info@yourcompany.com"
    
    customer_name = input("Customer Name: ")
    customer_email = input("Customer Email: ")

    items = []
    
    while True:
        item_name = input("\nEnter item description: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        total = quantity * price
        items.append({"description": item_name, "quantity": quantity, "price": price, "total": total})

        another = input("Add another item? (y/n): ")
        if another.lower() != 'y':
            break

    # Calculate grand total
    grand_total = sum(item['total'] for item in items)

    # Date & Invoice Number
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    invoice_number = f"INV{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Generate invoice string
    invoice = f"""
{'='*60}
{company_name}
{company_address}
Email: {company_email}
{'='*60}
Invoice To: {customer_name}
Email: {customer_email}
Date: {date}
Invoice #: {invoice_number}
{'='*60}
Description\t\tQty\tUnit Price\tTotal
{'-'*60}
"""

    for item in items:
        invoice += f"{item['description'][:16]:16}\t{item['quantity']}\t{item['price']:.2f}\t\t{item['total']:.2f}\n"

    invoice += f"{'-'*60}\n"
    invoice += f"{'Total Amount':>45}: KES {grand_total:.2f}\n"
    invoice += f"{'='*60}\n"

    print(invoice)

    # Save to file
    save = input("Do you want to save the invoice to a file? (y/n): ")
    if save.lower() == 'y':
        filename = f"invoice_{invoice_number}.txt"
        with open(filename, 'w') as file:
            file.write(invoice)
        print(f"✅ Invoice saved as {filename}")

if __name__ == "__main__":
    generate_invoice()
