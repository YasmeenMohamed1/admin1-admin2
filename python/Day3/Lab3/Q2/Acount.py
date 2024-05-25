import datetime

class Acount:
    def __init__(self,id,balance,customer_id):
        self.id=id
        self.balance=balance
        self.customer_id = customer_id
        self.operations = []
    

    def Deposit(self, amount):
        self.balance += amount
        self.operations.append(f"This {amount}$ deposited into your account in this time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def Withdraw(self, amount):
        if amount > self.balance:
            print(f"Theres is no enough money ({amount}$)")
            return False
        else:
            self.balance -= amount
            self.operations.append(f"This {amount}$ withdrawed from your account in this time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")

            return True
        
    def ShowLastOperation(self):
            print("The last operation is : " , self.operations[-1])
            
    
    def ShowAllOperations(self):
            print("All Operations : ")
            for i in self.operations:
                 print(i)
            
