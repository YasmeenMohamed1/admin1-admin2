from Bank import Bank
from Customer import Customer
from Acount import Acount

Misr = Bank('Misr')

customr1_account1 = Acount(1,5000,1)
customr2_account1 = Acount(3,4000,2)


customer1 = Customer(1,'Yasmeen',23)
customer2 = Customer(2,'Ahmed',27)

customer1.AddAcount(customr1_account1)
customer2.AddAcount(customr2_account1)

Misr.AddCustomer(customer1)
Misr.AddCustomer(customer2)

Misr.TransferMoney(customr1_account1,customr2_account1,200)
Misr.TransferMoney(customr2_account1,customr1_account1,1000)

print(customr1_account1.balance)
print(customr2_account1.balance)

customr1_account1.ShowLastOperation()
customr2_account1.ShowLastOperation()

customr1_account1.ShowAllOperations()

Misr.TransferMoney(customr2_account1,customr1_account1,1000)
