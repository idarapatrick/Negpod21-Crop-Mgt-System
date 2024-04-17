import mysql.connector
from tabulate import tabulate

def main():
    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",  # Your mysql username here
        password="1234",  # Your mysql password here
        database="Crop-Mgt-System"
    )

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    # Call the function to display products in the database
    display_products(cursor)

    # Close the cursor and connection
    cursor.close()
    cnx.close()

def display_products(cursor):
    # Execute the SQL query to retrieve the products
    query = "SELECT * FROM products"
    cursor.execute(query)

    # Fetch all the products from the result set
    products = cursor.fetchall()

    # Display the products in a tabular format
    print(tabulate(products, headers=['ID', 'Name', 'Price', 'Location', 'Farmer', 'Quantity','Expiration Date'], tablefmt='pretty'))

if __name__ == "__main__":
    main()
