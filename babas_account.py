
"""
pv = p * (pow((1 + r/100/n),n * t))

print(pv)
"""




def compound_interest():
    p = float(input("What's the principle? "))
    r = float(input("What's the rate? "))
    n = int(input("How many periods? "))
    t = int(input("How many payments per period? "))


    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    print("Balance at the end of the period ", round(balance,2))
    print("Interest earned is ", round(ci,2))

    percent = (ci - balance) * 100
    print (percent)

compound_interest()
