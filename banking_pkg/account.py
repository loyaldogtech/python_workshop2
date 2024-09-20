def show_balance(balance):
    print("Balance: $" + str(balance))

def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    return balance - amount

def logout(name):
    print("Goodbye " + name)
