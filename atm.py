import time
print("Please insert Your CARD")
time.sleep(5)
password=12345
pin=int(input("Enter your ATM Pin "))
balance=5000
if(pin==password):
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
        print("Your Current Balance is {balance}")
    if(option==2):
        withdraw_amount=int(input("please enter withdraw_amount: "))
        balance=balance=withdraw_amount
        