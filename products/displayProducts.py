import mysql.connector
from tabulate import tabulate


def display_products():
    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yassin@123",
        database="crops_mgmt"
    )

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    try:
        # Execute the SQL query to retrieve the products
        query = "SELECT * FROM products"
        cursor.execute(query)

        # Fetch all the products from the result set
        products = cursor.fetchall()

        # Display the products in a tabular format
        print(tabulate(products, headers=['ID', 'Name', 'Price', 'Location', 'Farmer', 'Quantity','Expiration Date'], tablefmt='pretty'))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

# Call the function to display the products


display_products()
