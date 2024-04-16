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
    password="Yassin@123",
    database="crops_mgmt"
)

# Create a cursor object
cursor = cnx.cursor()

# Create an order
order = Order()

# Ask the user what they wish to purchase and their location
print("What do you wish to purchase?")
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
while True:
    add_more = input("Do you want to add a product to the order? (yes/no): ")
    if add_more.lower() == 'yes':
        product_id = input("Enter the ID of the product to update: ")

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
    else:
        break

# Print the total price of the order
print("Total price of the order is:", order.total_price())

# Don't forget to close the cursor and connection
cursor.close()
cnx.close()
