import sys

account_balance = 1000.00
pin = "7992"
transaction_history = []

def display_balance():
    print(f"\nCurrent Balance:{account_balance:.2f}")

def deposit_money():
    global account_balance
    amount = float(input("Enter the deposit amount:"))
    if amount > 0:
        account_balance += amount             #Add the deposited amount to your current balance
        transaction_history.append(f"Deposited:{amount:.2f}")
        print(f"Successfully deposited {amount:.2f}")
        display_balance()
    else:
        print("Invalid Amount!!")

def withdraw_money():
    global account_balance
    amount = float(input("Enter the amount to Withdraw:"))
    if amount > account_balance:
        print("Insufficient Balance:")
    elif amount <= 0:
        print("Invalid Amount")
    else:
        account_balance-=amount
        transaction_history.append(f"Withdrwan:{amount:.2f}")
        print(f"Successfully withdrawn {amount:.2f}")
        display_balance()

def view_statement():
    print("\n--Statement--")
    if not transaction_history:
        print("No Transaction yet....!!")
    else:
        for transaction in transaction_history:
            print(transaction)
    display_balance()
    print("-------------")


def atm_menu():
    print("Welcome To SBI ATM.")
    entered_pin=(input("Please Enter The PIN."))
    if entered_pin!=pin:
        print("Invalid PIN,Exiting")
        return
    
    while True:
        print("\n1.Display Balance \n2.Withdraw Money \n3.Deposit Money \n4.Statement Record \n5.Exit")
        choice=(input("Select option(1-5):"))

        if choice == '1':
            display_balance()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            view_statement()
        elif choice == '5':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid Choice!!!,Please Try Again")

if __name__ == "__main__":

    atm_menu()
