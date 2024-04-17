import mysql.connector

def main():
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Your mysql username here
        password="1234",  # Your mysql password here
        database="Crop-Mgt-System"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Call the add_product function with db and cursor as arguments
    add_product(db, cursor)

# Function to add a product to the database
def add_product(db, cursor):
    # Prompt the user for product details
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    location = input("Enter product location: ")
    farmer = input("Enter farmer name: ")
    quantity = input("Enter quantity: ")
    expiration_date = input("Enter expiration date: ")

    # SQL query to insert a new product
    query = "INSERT INTO products (name, price, location, farmer, quantity,expiration_date) VALUES (%s, %s, %s, %s, %s,%s)"
    values = (name, price, location, farmer, quantity, expiration_date)

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes into the database
    db.commit()
    print("Product added successfully!")

if __name__ == "__main__":
    main()
