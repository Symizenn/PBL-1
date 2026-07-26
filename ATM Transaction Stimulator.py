balance = 0
while True:
    print("MENU")
    print("1.CHECK ACCOUNT BALANCE")
    print("2.DEPOSIT MONEY")
    print("3.WITHDRAW MONEY")
    print("4.EXIT")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print("Your current balance is:", balance)
    elif ch == 2:
        amt = float(input("Enter amount to deposit:"))
        print("Your amount successfully deposited")
        if amt > 0:
            balance = balance + amt
        else:
            print("Ivalid amount")
    elif ch == 3:
        amt = float(input("Enter amount to withdraw:"))
        if amt > 0:
            balance = balance - amt
        else:
            print("Invalid amount")
    elif ch == 4:
        print("Thankyou")
        break
    else:
        print("Invalid Choice")
