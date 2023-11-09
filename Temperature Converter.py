#Temperature Converter Problem

#Subroutine to convert Centigrade to Farenheit
C = 30
def CtoF():
    global C
    return (C * 1.8) + 32
    
#Subroutine to convert Fahrenheit to Centigrade

def FtoC():
    global F
    F = CtoF()
    return (F/ 1.8) - 32

#Main Program
CtoF()
FtoC()
print(C,"degrees C is", F, "degrees F")
