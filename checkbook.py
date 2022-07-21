import time

print("💰💰💰 Welcome to your bank terminal! 💰💰💰~")
time.sleep(.4)
print("\n")

options = (
    "What would you like to do? \n\n"
    "1) view your current balance\n"
    "2) record a debit (withdrawal)\n"
    "3) record a credit (deposit)\n"
    "4) see history of all transactions\n"
    "5) exit\n\n"
    "Enter your choice: "
)

choice = input(options)
time.sleep(.4)

while True:
    if choice == "1":
        balance = 0.00
        with open("check_book.txt", "r") as f:
            fl = f.readlines()
            for line in fl:
                balance = balance + float(line)
            print(f"Your balance is : ${round(balance, 2)}")
            choice = input(options)

    if choice == "2":
        with open("check_book.txt", "a") as f:
            debit_amount = input("How much do you want to debit? ")
            debit_amount = float(debit_amount) * -1
            debit_amount = str(debit_amount)
            f.write(debit_amount + "\n")
            print(f"Your total debit is ${debit_amount}")
            choice = input(options)

    if choice == "3":
        with open("check_book.txt", "a") as f:
            credit_amount = input("How mucbh do you want to credit? ")
            f.write(credit_amount + "\n")
            credit_amount = float(credit_amount)
            print(f"Your total credit is ${credit_amount}")
            choice = input(options)

    if choice == "4":
        with open("check_book.txt") as f:
            file_contents = f.read()
            print(file_contents)
            choice = input(options)

    if choice == "5":
        print("Have a great day 👋👋")
        time.sleep(.4)
        break
