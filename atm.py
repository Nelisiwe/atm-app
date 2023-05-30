import time
print("Please enter you Card :")
time.sleep(5)
pin = int(input("Enter you ATM PIN :"))
balance = 5000
if pin == 1234:
    while True:
        print("1 = Check Balance")
        print("2 = Withdraw")  
        print("3 = Deposit")  
        print("4 = Exit")
        try:
            option = int(input("Choose any obtion above :"))
        except:
            print("Please choose the valid option :")
        if option == 1:
            print("----------------------------------")
            print(f"Your current balance is {balance}")  
        if option == 2:
            withdraw = int(input("Enter you Withdraw Amount :")) 
            print("----------------------------------") 
            balance = balance - withdraw
            print(f"{withdraw} is debited from your Account :")
            print(f"Your current balance is {balance}")     
        if option == 3:
            deposit = int(input("Enter your Deposit Amount :"))             
            balance = balance + deposit
            print("----------------------------------") 
            print(f"{deposit} is credited to your Account")
            print(f"Your current balance is {balance}") 
        if option ==4:
            print("Thank you.... Have a nice day")  
            break  
    
else:
    print("You entered the wrong pin...Try again")                                                        

