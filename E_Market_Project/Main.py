from Product import addProduct, viewProducts
from Customer import addCustomer, viewCustomers
from Order import registerOrder, deleteOrder

def menu():
    while True:
        print("\n E-MARKET MENU")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Register Order")
        print("6. Delete Order")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == '1':
            addProduct()
        elif choice == '2':
            viewProducts()
        elif choice == '3':
            addCustomer()
        elif choice == '4':
            viewCustomers()
        elif choice == '5':
            registerOrder()
        elif choice == '6':
            deleteOrder()
        elif choice == '7':
            print("Goodbye! See you next time :)\n")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
