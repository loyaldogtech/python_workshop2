import banking_pkg.account
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("    === Automated Teller Machine ===    ")

name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0

print(name + " has been registered with a starting balance of $" + str(balance))

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        banking_pkg.account.show_balance(balance)
    elif option == "2":
        balance = banking_pkg.account.deposit(balance)
        banking_pkg.account.show_balance(balance)
    elif option == "3":
        balance = banking_pkg.account.withdraw(balance)
        banking_pkg.account.show_balance(balance)
    elif option == "4":
        banking_pkg.account.logout(name)
        break
