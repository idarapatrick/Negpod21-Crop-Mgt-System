
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
    
else:
  print("Invalid input")
  exit(0)
