balance = 100000
card ="CANARA ATM CARD"
password =9898

c = input("Insert the card: ")

if c == card:
    print("Welcome SARVANI")
    p = int(input("Enter the password: "))

    if p == password:
        print("1. Balance Enquiry")
        print("2. Withdraw")

        option = int(input("Enter option: "))

        if option == 1:
            print("Account Balance:", balance)

        elif option == 2:
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance")

        else:
            print("Invalid Option")

    else:
        print("Incorrect Password")

else:
    print("Invalid Card")
