

import orderingproduct
import Counselling
import PestFighting
import displayProducts
import exit
import updateProduct
import deleteProduct


def main():
    welcome()


def welcome():
    print("Welcome Again, client!")
    print("You have entered the services section of the application, and here are the services we offer:")
    print("1. Services related to agri-products shipping")
    print("2. Services related to farmers counselling")
    print("3. Services related to pests and diseases fighting")
    print("4. Press four if you wish to see the list of available agri-products")
    print("5. Press five if you wish to delete a product from your wallet")
    print("6.If you wish to add a product to your wallet press six")
    print("7. Press seven if you want to exit")
    print("*If you wish to order agro-products, please press one")
    print("* If you want to speak to one of our farming experts, please press 2")
    print("*If you wish to get any information related to pests and related diseases, press 3")
    print("Choose any number between 1 and 3 to continue", end="")
    answer_choice = int(input())
    if answer_choice == 1:
        orderingproduct.main()
    if answer_choice == 2:
        Counselling.main()
    if answer_choice == 3:
        PestFighting.main()
    if answer_choice == 4:
        displayProducts.main()
    if answer_choice == 5:
        deleteProduct.main()
    if answer_choice == 6:
        updateProduct.main()
    if answer_choice == 7:
        exit.main()


if __name__ == "__main__":
    welcome()
