import mysql.connector


def main():
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Crop-Mgt-System"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Call the function to update a product in the database
    update_product(db, cursor)

    # Close the cursor and database connection
    cursor.close()
    db.close()


# Function to update a product in the database
def update_product(db, cursor):
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
    values = (name, price, location, farmer, quantity, expiration_date, product_id)

    # Execute the query
    cursor.execute(update_query, values)

    # Commit the changes to the database
    db.commit()

    print("Product updated successfully!")

if __name__ == "__main__":
    main()
