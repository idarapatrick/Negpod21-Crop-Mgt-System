import main
import Counselling


def help():
    print("What do you need help with? Type your reply below: ")
    print("1. Navigation")
    print("2. Advice")
    reply = input().lower()
    if reply == "1":
       user_guide()
    elif reply == "2":
       Couselling.main()
    else:
        print("Invalid option, choose either 1 0r 2")

    help()
