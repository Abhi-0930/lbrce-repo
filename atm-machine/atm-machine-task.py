acc_type = "Savings"
pin = "1234"
acc_balance = 5000


def validate_pin():
    user_pin = input("Enter PIN: ")

    if user_pin == pin:
        return True

    print("Invalid PIN")
    return False


def deposit_money():
    global acc_balance

    if not validate_pin():
        return

    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount")
        return

    acc_balance += amount

    print(f"You have successfully deposited {amount} and your current balance is {acc_balance}")


def withdraw_money():
    global acc_balance

    if not validate_pin():
        return

    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
        return

    if amount > acc_balance:
        print("Insufficient Balance")
        return

    acc_balance -= amount

    print(f"You have successfully withdrawn {amount} and your current balance is {acc_balance}")


def balance_inquiry():

    if not validate_pin():
        return

    print("Account Type:", acc_type)
    print("Current Balance:", acc_balance)


while True:

    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            deposit_money()

        case 2:
            withdraw_money()

        case 3:
            balance_inquiry()

        case 4:
            print("Thank You For Banking With Us")
            break

        case _:
            print("Invalid Choice")