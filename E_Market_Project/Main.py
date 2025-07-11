from Product import addProduct, viewProducts, searchProduct, updatePrice, deleteProduct
from Customer import addCustomer, viewCustomers
from Order import registerOrder, deleteOrder
from Visualisation import generate_market_visuals  # <-- Import the visualization function

def menu():
    while True:
        print("\n E-MARKET MENU")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Price on a Product")
        print("5. Delete a Product")  
        print("6. Add Customer")
        print("7. View Customers")
        print("8. Register Order")
        print("9. Delete Order")
        print("10. Show Market Visualisation")  
        print("11. Exit")  

        choice = input("Choose an option (1-11): ")

        if choice == '1':
            addProduct()
        elif choice == '2':
            viewProducts()
        elif choice == '3':
            searchProduct()
        elif choice == '4':
            updatePrice()
        elif choice == '5':
            deleteProduct()
        elif choice == '6':
            addCustomer()
        elif choice == '7':
            viewCustomers()
        elif choice == '8':
            registerOrder()
        elif choice == '9':
            deleteOrder()
        elif choice == '10':
            generate_market_visuals()  
        elif choice == '11':
            print("Goodbye! See you next time :)\n")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()