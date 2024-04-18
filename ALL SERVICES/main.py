# Code to manage crops in the application
import services
import help
import exit

def main():
    def welcome():
     """Introduces the application and its functionalities."""
    print("Welcome to the Crop Farming Management System!")
    print("This application helps you manage your farming activities with ease.")
    print("Here's what you can do:")
    print("* Keep records of your crops in different planting seasons")
    print("* Access pest and disease control guides")
    print("* Connect with transportation services to move your goods to consumers")
    print("\nWe are constantly improving, and will continually add new features to better your expereince")


    welcome()


def user_guide():
    """Prints the user guide content within the program."""
    user_guide_text = """
**User Guide:**

1. To see a list of available services, type 'services'.
2. For help, type 'help'.
6. To exit, type 'quit'.
"""
    # Print the user guide text using a multi-line string
    print(user_guide_text)


user_guide()


# System MENU
while True:
    print("Choose an option:")
    print("1. access our services center")
    print("2. Help")
    print("3.quit")
    choice = input("Enter your choice: ")

    if choice == 'services':
        services.main()
    elif choice == 'help':
        help.main()
    elif choice == 'quit':
        exit.main()
        break  # Exit the while loop when the user chooses to exit
    else:
        print("Invalid choice.")
if __name__ == "__main__":
    main()
