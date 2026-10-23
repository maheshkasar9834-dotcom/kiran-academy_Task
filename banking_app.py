balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: Rs.", balance)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Balance is Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Money deposited successfully!")
            print("Updated Balance: Rs.", balance)
        else:
            print("Amount must be greater than zero!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")

        elif amount <= balance:
            balance = balance - amount
            print("Money withdrawn successfully!")
            print("Remaining Balance: Rs.", balance)

        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using Kiran Bank!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")