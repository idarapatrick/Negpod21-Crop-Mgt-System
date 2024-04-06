
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yassin@123",
        database="crops_mgmt"
)

# Create a cursor object
cursor = db.cursor()

# Function to update a product in the database
def update_product():
    # Prompt the user for product details
    product_id = input("Enter the ID of the product to update: ")
    name = input("Enter new product name: ")
    price = input("Enter new product price: ")
    location = input("Enter new product location: ")
    farmer = input("Enter new farmer name: ")
    quantity = input("Enter new quantity: ")
    expiration_date = input("Enter new expiration date: ")

    # SQL query to update the product
    update_query = "UPDATE products SET name = %s, price = %s, location = %s, farmer = %s, quantity = %s,expiration_date=%s WHERE id = %s"
    values = (name, price, location, farmer, quantity,expiration_date, product_id)

    # Execute the query
    cursor.execute(update_query, values)

    # Commit the changes to the database
    db.commit()

    print("Product updated successfully!")

# Example usage
# update_product()

# Close the cursor and database connection
#cursor.close()
#db.close()
