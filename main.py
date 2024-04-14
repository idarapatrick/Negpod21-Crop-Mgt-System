# Code to manage crops in the application
from products.addProduct import add_product
from products.displayProducts import display_products
from products.deleteProduct import delete_product
from products.updateProduct import update_product
from products.exit import exit_application


# Define functions for each option
def create_product_record():
    add_product()


def view_products_list():
    display_products()


def delete_product_record():
    delete_product()


def update_product_record():
    update_product()


def exiting_application():
    exit_application()


# System MENU
while True:
    print("Choose an option:")
    print("1. Create Product")
    print("2. View All Products")
    print("3. Delete Product  (by Product ID)")
    print("4. Update Product  (by Product ID)")
    print("5. Exit products menu")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_product_record()
    elif choice == '2':
        view_products_list()
    elif choice == '3':
        delete_product_record()
    elif choice == '4':
        update_product_record()
    elif choice == '5':
        exiting_application()
        break  # Exit the while loop when user chooses to exit
    else:
        print("Invalid choice.")
