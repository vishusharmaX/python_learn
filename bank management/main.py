

# Bank Account - 1
# Deposit Money - 2
# withdraw money -3
# details - 4
# update details - 5
# delete -Account -6





import json
import random
import string
from pathlib import Path



class Bank:
    database = r'D:\My Code\python yt\bank management\data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database, 'r', encoding='utf-8') as fs:
                content = fs.read().strip()
                if content:
                    data = json.loads(content)
                else:
                    data = []
        else:
            # create an empty JSON list file so updates will work later
            Path(database).write_text("[]", encoding='utf-8')
            data = []
    except Exception as err:
        print(f"The error occur due to {err}")
        data = []

            

    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar  = random.choices("!@#$%^&*",k=1)
        id  = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
        
    
            
    
    def Createaccount(self):
        info = {
            "name" : input("tell your name :- "),
            "age" : int(input("tell your age :- ")),
            "email" : input("tell your email :- "),
            "pin" : int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0,
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please not down your account number")
            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accn = input("tell your account number :-  ")
        pin = int(input("please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accn and i['pin'] == pin]
        if userdata == False:
           print("sorry no data found")
        else:
           amount  = int(input("how much want to deposit :- "))
           
           if amount > 10000 or amount < 0:
               print("sorry the amount is too much you can deposit  below 10000 and above 0")
            
           else:
            #    print(userdata)
               userdata[0]['balance']+=amount
               Bank.__update()
               print(userdata[0]['balance'])
               print("Amount deposited successfully")
               
               
    def withdrawMoney(self):
        accn = input("tell your account number :-  ")
        pin = int(input("please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accn and i['pin'] == pin]
        if userdata == False:
           print("sorry no data found")
        else:
           amount  = int(input("how much want to withdraw :- "))
           
           if userdata[0]['balance'] < amount:
               print("sorry you don't have that much money")
               
            
           else:
            #    print(userdata)
               userdata[0]['balance']-=amount
               Bank.__update()
               print(userdata[0]['balance'])
               print("Amount withdrew successfully")
    
    def showDetails(self):
        accn = input("tell your account number :-  ")
        pin = int(input("please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accn and i['pin'] == pin]
        print("Your information are:- ")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        
        # print(userdata)
    
    def updateDetails(self):
        accn = input("tell your account number :-  ")
        pin = int(input("please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accn and i['pin'] == pin]
        if userdata == False:
            print("no such user found")
        else:
            print("you cannot change the age,account number , balance")
            
            print("Fll the details for change or leabr it empty if no change")
            
            newdata = {
                "name" : input("please tell new name or press enter : "),
                "email" :input("please tell new email or press enter : "),
                "pin" : input("please tell new pin or press enter : ")
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("details update successfully")
            
    def deleteSelf(self):
        accn = input("tell your account number :-  ")
        pin = int(input("please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accn and i['pin'] == pin]
        
        if userdata == False:
            print("no such data exist")
        else:
            check = input("press y if you want to delete the account or press n")
            
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.__update()
        
              
           
user = Bank()
print("press 1 forcreating an account")
print("press 2 Deposiiting the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updateing the details")
print("press 6 for deleting your account")


check = int(input("tell your response :- "))

if check == 1:
    user.Createaccount()
if check == 2:
    user.depositMoney()
if check == 3:
    user.withdrawMoney()
if check == 4:
    user.showDetails()
if check == 5:
    user.updateDetails()
if check == 6:
    user.deleteSelf()