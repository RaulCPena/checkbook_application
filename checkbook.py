import time

# welcome prompt
print("\n~~~ Welcome to your terminal checkbook! ~~~\n\n")


time.sleep(.3)
print(
"What would you like to do?\n\n"

"1) view current balance\n"
"2) record a debit (withdraw)\n"
 "3) record a credit (deposit)\n"
"4) exit\n"
 )

user_input = input("Please enter your choice: ")
print()
print(f"You have chosen {user_input}")
