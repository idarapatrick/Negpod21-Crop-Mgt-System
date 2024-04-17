import mysql.connector


def main():
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Your mysql username here
        password="1234",  # Your mysql password here
        database="Crop-Mgt-System"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Call the function to delete a product from the database
    delete_product(db, cursor)

    # Close the cursor and database connection
    cursor.close()
    db.close()


def delete_product(db, cursor):
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


if __name__ == "__main__":
    main()
