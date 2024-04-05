# Crops management system
from products.addProduct import add_product
from products.exit import exiting_application
from products.deleteProduct import delete_product
from products.displayProducts import display_products
from products.updateProduct import update_product

# System MENU
while True:
    print("Choose an option:")
    print("1. Create Product")
    print("2. View All Products")
    print("3. Delete Product  (by Product ID)")
    print("4. Update Product  (by Product ID)")
    print("5. Exit The System")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_product()
    elif choice == '2':
        display_products()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        exiting_application()
    else:
        print("Invalid choice.")
