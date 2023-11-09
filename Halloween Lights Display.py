#Hallowe'en Lights Display Problem
import random
import time
def pause(milliseconds):
    global count
    Time = milliseconds / 100
    time.sleep(Time)
    print("Light = LOW ({})\n".format(count))
#Main Program
total = 0
count = 0
while total == 0:
    count = count + 1
    print("Light = HIGH ({})\n".format(count))
    milliseconds = random.randint(1, 1000)
    pause(milliseconds)
