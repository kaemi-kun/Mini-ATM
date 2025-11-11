#plan
#1. login system i.e username + pin authentication
#2. Max 3 pin attempts
#3. main menu
#4. balace management
#5. transaction history
#6. input validation
#7. logout option
#8. daily withdrawl limit
#9. change pin option
#10. simple receipt generator
#11. admin mode

#pre-made dectionary for users
users = {
    "Admin":{
        "pin":"606060"
    },
    "Suryam":{
        "pin":"202004",
        "balance":50000,
        "history":[]
    },
    "Shrutika":{
        "pin":"182005",
        "balance":100000,
        "history":[]
    },
    "Kaiser":{
        "pin":"123456",
        "balance":15000,
        "history":[]
    },
    "Mahesh Dalle":{
        "pin":"343434",
        "balance":100000,
        "history":[]
    },
    "Mukesh":{
        "pin":"901256",
        "balance":40000,
        "history":[]
    }
}

#login system
def login():
    global name
    name = input("Enter your username : ")
    if name in users:
        user_data = users[name]
        attempts = 3
        while attempts > 0:
            pin = input("Enter your pin : ")
            if pin == user_data["pin"] and pin != "606060":
                menu()
                break
            elif pin == "606060":
                print("Welcome admin")
                admin()
            else:
                print("Invalid pin")
                attempts -= 1
        if attempts == 0:
            print("Entered wrong PIN 3 times. Acoount is locked")
    else:
        print("Invalid username T_T")

def admin():
    user_data = users[name]
    while True:
        print("1.Access all user files")
        print("2.Change the admin pin")
        print("3.Logout")
        b = int(input())
        if b == 1:
            print(users)
        elif b == 2:
            password = input("Enter new pin")
            user_data["pin"] = password
            print("pin changed successfully")
        elif b == 3:
            print("Thank you for visiting our ATM")
            break
        else:
            print("Instruction not defined")
            

def menu():
    user_data = users[name]
    while True:
        print("1.View balance")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.View transaction history")
        print("5.Logout")
        a = int(input())
        
        if a == 1:
            print(user_data["balance"])
            
        elif a == 2:
            deposit = int(input("Enter money to be deposited : "))
            user_data["balance"] = user_data["balance"] + deposit
            print(f"Money deposited! Available balance : {user_data['balance']}\n")
            user_data["history"].append(f"Deposited {deposit}")
            
        elif a == 3:
            withdraw = int(input("Enter money to be withdrawn : "))
            if user_data["balance"] >= withdraw and withdraw < 20000:
                user_data["balance"] = user_data["balance"] - withdraw
                print(f"Money withdrawn successfully!. Available balance : {user_data['balance']}\n")
                user_data["history"].append(f"Withdrawn {withdraw}")
                
            elif withdraw >20000:
                print("Daily withdrawl limit exceeded.")
                
            else:
                print("Insufficient balance\n")
                
        elif a == 4:
            for item in user_data["history"]:
                print(item)
             
        elif a == 5:
            print("Thank you for visiting our ATM")
            break
        else:
            print(" instrunction not defined.")
            

login()
