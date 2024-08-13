import time
print("Please insert Your CARD")
time.sleep(5)
password=12345
pin=int(input("Enter your ATM Pin "))
balance=5000
if(pin==password):
    while True:
        print("""
            1==balance
            2==withdraw balance
            3==deposit balance
            4==exit
            """
            )
        try:
            option=int(input("Please Enter Your Choice: "))
        except:
            print("Please Enter Valid Choice: ")

        if(option==1):
            print(f"Your Current Balance is {balance}")
        if(option==2):
            withdraw_amount=int(input("please enter withdraw_amount: "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your updated current balance is {balance}")
        if(option==3):
            deposit_amount=int(input("Enter your Deposit Amount: "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated current balance is {balance}")
        if(option==4):
            break
else:
    print("Wrong Pin! Please Enter again.....")