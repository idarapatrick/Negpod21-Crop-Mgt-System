import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute the SQL query to retrieve the products
query = "SELECT * FROM products"
cursor.execute(query)

# Fetch all the products from the result set
products = cursor.fetchall()

# Display the products
for product in products:
    print(product)

# Close the cursor and connection
cursor.close()
cnx.close()
