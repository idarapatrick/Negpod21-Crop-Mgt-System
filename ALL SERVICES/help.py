import main
import Counselling
import services


def help():
    print("What do you need help with? Type your reply below: ")
    print("1. Navigation")
    print("2. Advice")
    reply = input().lower()
    if reply == "1":
       services.main()
    elif reply == "2":
       Counselling.main()
    else:
        print("Invalid option, choose either 1 0r 2")

    help()
