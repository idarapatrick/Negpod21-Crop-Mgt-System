def welcome():
    """Introduces the application and its functionalities."""
    print("Welcome to the Crop Farming Management System!")
    print("This application helps you manage your farming activities with ease.")
    print("Here's what you can do:")
    print("* Keep records of your crops in different planting seasons")
    print("* Access pest and disease control guides")
    print("* Connect with transportation services to move your goods to consumers")
    print("\nWe are constantly improving, and will continually add new features to better your expereince")


welcome()


def user_guide():
    """Prints the user guide content within the program."""
    user_guide_text = """
**User Guide:**

1. To see a list of available services, type 'services'.
2. To add products to your inventory, type 'products'
3. To learn how to control pest and crop diseases, type 'control'
4. To connect with a transport service, type 'transport'
5. For help, type 'help'.
6. To exit, type 'quit'.
"""
    # Print the user guide text using a multi-line string
    print(user_guide_text)


user_guide()

# to access services

# Code to manage crops in the application
from products.addProduct import add_product
from products.displayProducts import display_products
from products.deleteProduct import delete_product
from products.updateProduct import update_product
from products.exit import exit_application


# Define functions for each option
def products():
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
            break  # Exit the while loop when the user chooses to exit
        else:
            print("Invalid choice.")


# Call the products function to start the menu
products()


request = input("** ").lower()
if request == "services":
  print("\nOur Available Services: ")
  print("Inventory Management")
  print("Transportation")
  print("Pest/Disease Control Guides")
elif request == "quit":
  print("Thank you!")
  exit(0)
elif request == "products":
    products()
else:
  print("Invalid input")
  exit(0)

