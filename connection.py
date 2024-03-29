import mysql.connector

# Establishing a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    if connection.is_connected():
        print("Connected to MySQL database")

    # Perform operations

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Closing database connection
    if 'connection' in locals():
        connection.close()
        print("MySQL connection is closed")
