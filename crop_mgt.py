
def welcome():
    """Introduces the application and its functionalities."""
    print("Welcome to the Crop Farming Management System!")
    print("This application helps you manage your farming activities with ease.")
    print("Here's what you can do:")
    print("* Track crop information (planting, harvest, etc.)")
    print("* Access pest and disease control guides")
    print("* Connect with other farmers in a community forum (future implementation)")
    print("\nWe are constantly improving, and will continually add new features to better your expereince")


welcome()


def user_guide():
  """Prints the user guide content within the program."""
  user_guide_text = """
  **User Guide:**

  1. To see a list of available services, type 'services'.
  2. To connect with a buyer/seller, type 'connect' (feature under development).
  3. To learn more about specific services, type 'info <service_name>'. (e.g., info crop_shipment)
  4. For help, type 'help'.
  5. To exit, type 'quit'.
  """
  #Print the user guide text using a multi-line string
  print(user_guide_text)

request = input().lower()
