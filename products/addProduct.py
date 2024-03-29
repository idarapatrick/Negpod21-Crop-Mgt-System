import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to add a product to the database
def add_product(name, price, quantity):
    # SQL query to insert a new product
    query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    values = (name, price, quantity)

    # Execute the query
    cursor.execute (query, values)

    # Commit the changes into the database
    db.commit()

    print("Product added successfully!")

# Example usage.
add_product("Apple", 0.99, 100)

# Close the database connection
db.close()