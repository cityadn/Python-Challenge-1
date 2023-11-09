#Passing by Value
#Subroutine to calculate deductions from pay
def subtract_deductions(pay,percent):
    return (pay*percent)/100

def calculate_pay(pay):
    pay = pay - subtract_deductions(pay,22)
    return pay
    
#Main Program
pay = 2000
result = calculate_pay(pay)
print(result)

