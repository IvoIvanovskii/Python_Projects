from db import connect

def addProduct():
    db = connect()
    cursor = db.cursor()
    productName = input("Enter the name of the product you want to add: ")
    name_lower = productName.lower()

    cursor.execute("SELECT product_name FROM products WHERE LOWER(product_name) = %s ", (name_lower,))
    if cursor.fetchone():
     print ("This prodcut already exists.")
    else:
       try:
          price = float(input("Enter the price of the product you just added: "))
          quantity = int(input("Enter quantity for the product: "))
          cursor.execute("INSERT INTO products (product_name, price) VALUES (%s, %s)", (productName, price))
          db.commit()
          print (f"{productName} added successfully. ")
       except ValueError:
          print("Invalid price was added.")

    cursor.close()
    db.close()

def viewProducts():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT product_name, price FROM products")
    results = cursor.fetchall()

    if not results:
        print("The store is out of stock.\n")
    else:
        print("Product List:\n")
        for name, price in results:
            print(f"{name}: ${price:.2f}")
        print()

    cursor.close()
    db.close()

