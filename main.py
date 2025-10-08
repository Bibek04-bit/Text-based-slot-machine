
#deposit money for betting
def deposit():
    while True: 
        amount = input("What amount would you like to deposit? Rs")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Ta pagal ho?")
        else:
            print("Please enter a number.")

    return amount

deposit()