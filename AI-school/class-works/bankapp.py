class BankApp:
    def __init__(self, name, mobile, pan, email, deposit_amount):
        self.name = name
        self.mobile = mobile
        self.pan = pan
        self.email = email
        self.deposit_amount = deposit_amount
        print("Data Recieved Successfully!!!")

    def GenerateAccountNumber(self):
        if (self.deposit_amount >= 5000):
            self.account_number = self.name[:2] + self.name[-2:] + self.mobile[-4:] + self.pan[:3] + self.pan[-3:]
            print("Account Generated Successfully: ", self.account_number)
            return True
        else:
            print("Account not created (minimum deposit is 5000)")
            return False

    def CreatePIN(self):
        if (self.GenerateAccountNumber() == True):
            self.pin = int(input("Please Create a 4 digit PIN: "))
            print("PIN Generated Succesfully")
            return True
        else:
            print("Please create Account first to generate pin!!!")
            return False

    def BankingOperations(self):
        operation = input("Please choose type of operation (Deposit, withdraw, balance_enq): ")
        if (operation.lower() == "deposit"):
            user_pin = int(input("Please enter your 4 digit PIN: "))
            if (user_pin == self.pin):
                user_deposit_amount = int(input("Please enter your deposit amount: "))
                self.account_balance = user_deposit_amount + self.deposit_amount
                print("Deposit Successfull, account balance: ", self.account_balance)
                return True
            else:
                print("Invalid PIN.")
                return False
        elif (operation.lower() == "withdraw"):
            user_pin = int(input("Please enter your 4 digit PIN: "))
            if (user_pin == self.pin):
                user_withdraw_amount = int(input("Please enter your withdrawl amount: "))
                if (user_withdraw_amount < self.deposit_amount):
                    self.account_balance = self.deposit_amount - user_withdraw_amount
                    print("withdraw Successfull, account balance: ", self.account_balance)
                    return True
                else:
                    print("Insufficient Funds")
                    return False
            else:
                print("Invalid PIN.")
                return False
        elif (operation.lower() == "balance enquiry"):
            user_pin = int(input("Please enter your 4 digit PIN: "))
            if (user_pin == self.pin):
                print("Account Balance: ", self.deposit_amount)
                return True
            else:
                print("Invalid PIN.")
                return False
        else:
            print("Invalid Operation")
            return False
