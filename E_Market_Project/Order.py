from db import connect
from datetime import date

def registerOrder():
    db = connect()
    cursor = db.cursor()
    customerID = input("Customer ID: ")
    productID = input("Product ID: ")
    total = float(input("Total amount to pay: "))
    orderDate = date.today()

    cursor.execute("""INSERT INTO orders (customer_id, product_id, full_amount, order_date) VALUES (%s, %s, %s, %s)""", (customerID, productID, total, orderDate))
    db.commit()
    print("Order placed.\n")

    cursor.close()
    db.close()

def deleteOrder():
    db = connect()
    cursor = db.cursor()
    order_id = input("Order ID to delete: ")

    cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
    db.commit()
    print("Order deleted.\n")

    cursor.close()
    db.close()
