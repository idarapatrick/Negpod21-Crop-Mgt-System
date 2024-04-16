import mysql.connector

class Product:
    def __init__(self, id, name, price, location, farmer, quantity, expiration_date):
        self.id = id
        self.name = name
        self.price = price
        self.location = location
        self.farmer = farmer
        self.quantity = quantity
        self.expiration_date = expiration_date

class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({
            'product': product,
            'quantity': quantity
        })

    def total_price(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

# Establish the connection
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Crop-Mgt-System"  # Removed leading space
)

# Create a cursor object
cursor = cnx.cursor()

# Create an order
order = Order()

print("What do you wish to purchase? These are the available products with the first number being the product id:")
print("2. BANANA")
print("4. Pineapple")
print("9. Oranges")
print("6. Watermelon")
print("23. Milk")
print("3. Mangoes")
print("Enter a Product: ", end="")
product_choice = int(input())
if product_choice == 1:
    print("The cost of One BANANA IS 5$")
elif product_choice == 2:
    print("THE COST OF ONE PINEAPPLE IS 3000$")
elif product_choice == 3:
    print("The cost of one orange is 12$")
elif product_choice == 4:
    print("The cost of watermelon is 1000$")
elif product_choice == 5:
    print("The cost of one liter of Milk is 12$")
elif product_choice == 6:
    print("The cost of Mango is 3000$")
else:
    print("Invalid choice. Please enter a number between 1 and 6.")

answer = input("Do you wish to continue with the purchase? (yes/no): ")
if answer.lower() == 'no':
    print("Okay, no problem. Have a great day!")
    exit(0)  # This will stop the execution of the script
elif answer.lower() == 'yes':
    # Corrected the print statement
    print("Great! Let's continue with the purchase.")
else:
    print("Invalid response. Please answer with 'yes' or 'no'.")

print("Where is your location? Please choose from the following provinces of Rwanda:")
print("1. Southern")
print("2. Northern")
print("3. Eastern")
print("4. Western")
print("5. Kigali City")
location = input("Enter the number of your choice: ")

# Print the available route based on the user's choice
if location == '1':
    print("The available route is: HUYE-KAMONYI-KIGALI")
elif location == '2':
    print("The available route is: NYAGATARE-MUSANZE-KIGALI")
elif location == '3':
    print("The available route is: KIREHE-RWAMAGANA-KIGALI")
elif location == '4':
    print("The available route is: RUSIZI-KARONGI-NYAMAGABE-HUYE-MUHANGA-RUHANGO-KAMONYI-KIGALI")
elif location == '5':
    print("A drone will deliver the product")

# Add products to the order
product_count = 0  # Counter to track the number of products added
while True:
    if product_count == 0:
        add_more = input("Do you want to add a product to the order? (yes/no): ")
    else:
        add_more = input("Do you want to add another product to the order? (yes/no): ")

    if add_more.lower() not in ['yes', 'no']:
        raise ValueError("Invalid response. Please answer with 'yes' or 'no'.")
    elif add_more.lower() == 'yes': 
        product_id = input("Enter the number your preferred product ID : ")

        # Now you can execute SQL queries
        query = ("SELECT * FROM products WHERE id = %s")
        cursor.execute(query, (product_id,))

        # Fetch the result
        result = cursor.fetchone()

        # Create a Product object from the result
        product = Product(*result)

        quantity = int(input("Enter quantity: ")) # convert input to int for quantity

        # Add the product to the order
        order.add_product(product, quantity)

        product_count += 1  # Increment the counter after a product is added
    else:
        break


# Print the total price of the order
print("Total price of the order is:", order.total_price())  # Corrected the method call

# Don't forget to close the cursor and connection
cursor.close()
cnx.close()
