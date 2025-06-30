from db import connect

def addCustomer():
    db = connect()
    cursor = db.cursor()
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email: ")
    address = input("Address: ")

    cursor.execute("INSERT INTO customers (first_name, last_name, email, address) VALUES (%s, %s, %s, %s)", (firstName, lastName, email, address))
    db.commit()
    print("Customer added.\n")

    cursor.close()
    db.close()

def viewCustomers():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT first_name, last_name, email FROM customers")
    customers = cursor.fetchall()

    print("Customer List:\n")
    for cust in customers:
        print(f"{cust[0]} {cust[1]} - {cust[2]}")
    print()

    cursor.close()
    db.close()
