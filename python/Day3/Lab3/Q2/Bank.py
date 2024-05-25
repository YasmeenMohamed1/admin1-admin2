class Bank():
    def __init__(self,name):
        self.name = name
        self.customers=[]
        self.accounts = []

    def AddCustomer(self,customer):
        self.customers.append(customer)

        for i in customer.accounts:
            self.accounts.append(i)

    def TransferMoney(self,first_account,second_acount,amount):
        if(first_account in self.accounts and second_acount in self.accounts):

            if(first_account.Withdraw(amount)):
                second_acount.Deposit(amount)

                print("Successed")

            else:
                print("Failed")

            


   

