import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = db.cursor()

# Update the product
product_id = 1  # Replace with the actual product ID
new_price = 9.99  # Replace with the new price

update_query = "UPDATE products SET price = %s WHERE id = %s"
values = (new_price, product_id)

cursor.execute(update_query, values)

# Commit the changes
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
