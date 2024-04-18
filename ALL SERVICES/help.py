# help.py
import Counselling
import services  # Import the main module

def help():
    while True:
        print("What do you need help with? Type your reply below: ")
        print("1.Services")
        print("2. Advice")
        reply = input().lower()
        if reply == "1":
            services.main()  # Call the welcome function in the main module
        elif reply == "2":
            Counselling.main()
        else:
            print("Invalid option, choose either 1 or 2")
            continue

        another_help = input("Do you need help with anything else? (yes/no): ").lower()
        if another_help != 'yes':
            break

help()
