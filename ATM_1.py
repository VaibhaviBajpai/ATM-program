class Atm:
    def __init__(self,user_id,pin): #magic method
        self.user_id= user_id
        self.pin=pin
        self.balance=0 #initial balance is zero
        self.transaction_history=[]


        #method for login 
    def login(self):
        entered_user_id=input("Enter your user id: ")
        entered_user_pin=input("enter your secret number: ")
        if (entered_user_id==self.user_id and entered_user_pin==self.pin):
            print("Login successful!")
            return True
        else:
            print("Invalid user_id or pin, please try again")
            return False 
        # method for balance check
    def check_balance(self):
        print(f"your balance is {self.balance}")

        # method for deposit
    def deposit(self,amount):
        self.balance+=amount
        self.transaction_history.append(("deposit",amount))
        print(f"{amount} Rs deposited Successfully.Your new balance is{self.balance}Rs")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.transaction_history.append(("withdraw",amount))
            print(f"{amount} Rs Withdrawn successfully!.Your new balance is {self.balance}Rs")

    def transfer(self, recipient,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            recipient.balance+=amount
            self.transaction_history.append(("Trnsfer to" + recipient.user_id,amount))
            print(f"{amount}Rs transferred  to {recipient.user_id} Successfully")
            print(f"your new balance is {self.balance}")
            
    def show_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction[0]}: Rs{transaction[1]}")
            
        #method for atm menu so that user can choose what he/she wants to do
    def main_menu(self):
        while True:
          print("Atm menu")
          print("1.Check balance")
          print("2.Deposit")
          print("3.Withdraw")
          print("4.Transfer")
          print("5.Transaction History")
          print("6 Quit")

          option=input("Enter the option (1-6): ")
          
          if(option=="1"):
              self.check_balance()
          elif(option=="2"):
               amount=float(input("enter the amount you want to deposit: Rs"))
               self.deposit(amount)
          elif(option=="3"):
              amount=int(input("enter the amount you want to withdraw: Rs"))
              self.withdraw(amount)
          elif(option=="4"):
              recipient_id=input("Enter the recipient id : ")
              recipient=Atm.users.get(recipient_id)
              if recipient:
               amount=float(input("Enter the amount you want to transfer: "))
               self.transfer(recipient,amount)
              else:
                print(f"recipient with user_id{recipient.user_id}not found ")
          elif(option=="5"):
              self.show_transaction_history()
          elif(option=="6"):
              print("Thankyou!")
              break
          else:
              print("Invalid please choose between 1-6")
        
if __name__== "__main__":
  user_id="5565"
  pin="1234"
  #creating instance of Atmclass
  my_Atm =Atm(user_id,pin)
 
  # Second user for transfer function
  recipient_user_id="1234"
  recipient_pin="4566"
  recipient_Atm=Atm(recipient_user_id,recipient_pin)

## mapping of users
  Atm.users={user_id:my_Atm,recipient_user_id:recipient_Atm}


  if my_Atm.login():# if login is successfull user can access the main menu
    my_Atm.main_menu()

