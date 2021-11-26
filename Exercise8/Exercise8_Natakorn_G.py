usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "loma" and passwordInput == "lom@124" :
    print("    Welcome to !")
    print("---- LomaCafe ----")
    print("What would you like to order?")
    print("1.Cappuccino = 60")
    print("2.Americano  = 60")
    print("3.Milk Tea   = 50")
    print("4.Green Tea  = 50")
    userSelected = int(input("Please select the menu "))
    if userSelected == 1:
        quantity = int(input("How many do you want? "))
        price = quantity*60
        print("Total: ", price, "THB")
    elif userSelected == 2:
        quantity = int(input("How many do you want? "))
        price = quantity * 60
        print("Total: ", price, "THB")
    elif userSelected == 3:
        quantity = int(input("How many do you want? "))
        price = quantity * 50
        print("Total: ", price, "THB")
    elif userSelected == 4:
        quantity = int(input("How many do you want? "))
        price = quantity * 50
        print("Total: ", price, "THB")
else :
    print("The username or password you entered is incorrect.")
print("Thank you")