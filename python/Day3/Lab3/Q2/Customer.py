class Customer():
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
        self.accounts=[]


    def AddAcount(self,account):
        self.accounts.append(account)

