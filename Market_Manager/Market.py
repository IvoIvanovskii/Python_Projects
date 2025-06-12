products = {}

def addProduct():
    name = input("Add the name of the product: ")
    nameLower = name.lower()
    
    if any(name.lower() == nameLower for name in products):
        print("This product already exists")
        print()
        return
    
    try:
        price = int(input("Enter price for the product "))
        products[name] = price
        print(f"{name} product added.")
    except:
        print("Invalid Price")
    
    print()

def deleteProduct():
    name = input("Enter the name of the product to delete it: ")

    if name in products:
        del products[name]
    else:
        print("This product doesn't exist.")
        
    print()
        
def showAllProducts():
    if not products:
        print("The market is out of stock. Please restock first.")
    else:
        print("Product List: \n")
        for name, price in products.items():
            print(f"{name}: {price}")
    
    print()


def main():
    while True:
        
        print("----MARKET NAME----")

        print ("Enter 1 to add a product")
        print ("Enter 2 to delete a product")
        print ("Enter 3 to show all products")
        print ("Enter 4 to exit")

        choice = input("Choose one of the options (1-4): ")

        if choice == "1":
            addProduct()
        elif choice == "2":
            deleteProduct()
        elif choice == "3":
            showAllProducts()
        elif choice == "4":
            print("Have a nice day. :)")
            break
        else:
            print("You inserted an invalid choice. Please try again.")

main()
