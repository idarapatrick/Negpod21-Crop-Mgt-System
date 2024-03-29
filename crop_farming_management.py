
def introduction():
 #Prints a welcome message and application overview
  print("Welcome to the Crop Farming Management System!")
  print("This application is designed to connect farmers and buyers,")
  print("facilitating crop shipment and transactions.")
  print("We offer various agricultural services to suit your needs.\n")
introduction()


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
user_guide()

request = input().lower()

