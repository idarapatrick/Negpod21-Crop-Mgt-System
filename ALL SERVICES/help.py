<<<<<<< HEAD
#!/usr/bin/python3
def main():
    print(" Hello, thank you for your visit")
    print("Please , call 0781280833 or dial *860# for further assistance" )
    if __name__ == "__main__":
     main()
=======
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
>>>>>>> 33099a0781b0f0dfd64b8afa6319ba81c4854049
