# In this snippet, we connect to the MySQL database and retrieve all the products from the products table. We then use the tabulate library to display the products in a tabular format. Finally, we close the cursor and connection to the database. This snippet can be used to display the products in a user-friendly way in the console or terminal.
import mysql.connector
from tabulate import tabulate

# Connect to the MySQL database
cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yassin@123",
        database="crops_mgmt"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()
def display_products():
    # Execute the SQL query to retrieve the products
    query = "SELECT * FROM products"
    cursor.execute(query)

    # Fetch all the products from the result set
    products = cursor.fetchall()

    # Display the products in a tabular format
    print(tabulate(products, headers=['ID', 'Name', 'Price', 'Location', 'Farmer', 'Quantity','Expiration Date'], tablefmt='pretty'))

    # Close the cursor and connection
   #  cursor.close()
   # cnx.close()
# display_products()
