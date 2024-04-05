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

# Function to delete a product from the database
def delete_product():
    # Prompt the user for the ID of the product to delete
    product_id = input("Enter the ID of the product to delete: ")

    # Prompt for confirmation
    confirm = input("Are you sure you want to delete this product? (Y/N): ")
    if confirm.upper() != "Y":
        print("Deletion cancelled.")
        return

    # Prepare the SQL query
    sql = "DELETE FROM products WHERE id = %s"

    # Execute the query
    cursor.execute(sql, (product_id,))

    # Commit the changes
    db.commit()

    print("Product deleted successfully!")

# Example usage
delete_product()

# Close the cursor and database connection
cursor.close()
db.close()
