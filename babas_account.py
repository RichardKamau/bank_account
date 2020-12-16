
"""
pv = p * (pow((1 + r/100/n),n * t))

print(pv)

class Bank_Account:
    def __init__(self):

        def deposit(self):
            amount=float(input("Enter amount to be deposited: ")
                         self.balance += amount
                         print("\n Amount Deposited:", amount)

        def withdraw(self):
            amount = float(input("Enter amount to be Withdrawn: "))
            if self.balance>=amount:
                self.balance-=amount
                print("\n You Withdrew:", amount)
            else:
                print("\n Insufficient balance ")

        def display(self):
            print("\n Net Available Balance=", self.balance)


# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()


def compound_interest():
    p = float(input("What's the principle? "))
    r = float(input("What's the rate? "))
    n = int(input("How many periods? "))
    t = int(input("How many payments per period? "))


    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    print("Your balance at the end of the period will be $", round(balance,2), "\n")
    
    print("You earned $", round(ci,2), "during the period.")

    percent = (ci/balance) * 100
    print("This is", round(percent,2),"% return on investment.")

compound_interest()
"""

def mortgage_payment(self,loan,n,rate):
    p = loan*(rate/12/100*pow((1+rate/12/100),n))/(pow((1+rate/12/100),n)-1)
    print(round(p,2))
mortgage_payment(75000,360,3.375)
        
