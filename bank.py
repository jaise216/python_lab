class Bank:
    def __init__(self, accno, nam, typ, bal):
        self.Account_No = accno
        self.Name = nam
        self.Account_Type = typ
        self.Balance = bal

    def deposit(self, amt):
        self.Balance = self.Balance + amt
        print("balance: ", self.Balance)

    def withdraw(self, amt):
        if amt > self.Balance:
            print("insufficient balance")
        self.Balance = self.Balance - amt
        print("balance: ", self.Balance)


na = input("enter your name ")
acc = int(input("enter your account no "))
ty = input("enter type of account ")
at = int(input("enter current balance "))
n = int(input("1. deposit  2. withdraw\n"))
b1 = Bank(na, acc, ty, at)
dep = int(input("enter the amount to be deposited "))
b1.deposit(dep)
wit = int(input("enter the amount to be withdrawn "))
b1.withdraw(wit)
print("Name: ", na)
print("Account No: ", acc)
print("Type of Account: ", ty)
