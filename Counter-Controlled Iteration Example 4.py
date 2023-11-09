def Countdown(T):
    print("T minus {} to liftoff".format(T))
    for Cd in range(T-1,-1,-1):
        print(Cd)

# Main program
Countdown(10)
