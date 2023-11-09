#Currency Converter Problem
 # 1 GBP = 1.1267 EUROS
EUR = 1.1267
 # 1 GBP = 1.36 USD 
USD = 1.36
 # 1 GBP = 8.80587 YUAN
YUAN = 8.80587
 # 1 GBP = 138.645 YEN
YEN = 138.645
exchange = input("What currency do you want?:\n")
gbp = input("How much (in gbp):\n")
#Subroutine to convert currencies
def currencies():
    global EUR
    global USD
    global YUAN 
    global YEN
    global money
    if exchange == 'EURO':
        money = float(gbp) * EUR
    elif exchange == 'USD':
        money = float(gbp) * USD
    elif exchange == 'YUAN':
        money = float(gbp) * YUAN
    elif exchange == 'YEN':
        money = float(gbp) * YEN
#Main Program
currencies()
print(money)




