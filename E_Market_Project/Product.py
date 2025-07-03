from db import connect

def addProduct():
    db = connect()
    cursor = db.cursor()
    productName = input("Enter the name of the product you want to add: ")
    name_lower = productName.lower()

    cursor.execute("SELECT product_name FROM products WHERE LOWER(product_name) = %s ", (name_lower,))
    if cursor.fetchone():
     print ("This product already exists.")
    else:
       try:
          price = float(input("Enter the price of the product you just added: "))
          quantity = int(input("Enter quantity for the product: "))
          cursor.execute("INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)", (productName, price, quantity))
          db.commit()
          print (f"{productName} added successfully. ")
       except ValueError:
          print("Invalid price was added.")

    cursor.close()
    db.close()

def viewProducts():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT product_name, price, quantity FROM products ORDER BY price ASC")
    results = cursor.fetchall()

    if not results:
        print("The store is out of stock.\n")
    else:
        print("Product List:\n")
        for name, price, quantity in results:
            print(f"{name}: ${price:.2f}. Quantity: {quantity}")
        print()

    cursor.close()
    db.close()

def updatePrice():
    db = connect()
    cursor = db.cursor()
    productName = input("Enter the product name whose price you want to change. ")
    nameLower = productName.lower

    cursor.execute("SELECT product_name FROM products WHERE LOWER(product_name) = %s", (nameLower,))

    if cursor.fetchone():
       try:
          newPrice = float(input("Enter the wanted price: "))
          cursor.execute("UPDATE products SET price = %s WHERE LOWER(product_name) = %s", (newPrice, nameLower))

          print(f"Price has been changed successfuly for {productName}.")

       except ValueError:
          print(f"Entered invalid price for {productName}.")
    else:
       print("Product not found")

    cursor.close()
    db.close()

def searchProduct():
   db = connect()
   cursor = db.cursor()
   productName = input("Enter the product name you want to see. ")
   nameLower = productName.lower

   cursor.execute("SELECT product_name, price, quantity FROM products WHERE LOWER(product_name) = %s", (nameLower,))
   result = cursor.fetchone

   if result:
      name, price, quantity = result
      print (f"The product you are viewing is: {name}, price is {price}, and quantity is: {quantity}")

   else:
      print("The product you are trying to find does not exist.")

    
   cursor.close()
   db.close
      


    
          

          


    