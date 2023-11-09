#Cassini Problem
#Suboroutine to find if the bit sequence is correct or not

def oddParity(bitSequence):
    counter = 0
    binary = str(bitSequence)

    
    for i in range(0, len(binary)):
        if binary[i] == '1':
            counter = counter + 1
    print(bitSequence, "contains", counter, "ones")

    
    if (counter % 2) == 0:
        print("This sequence is incorrect and must be corrected")
    else:
        print("This sequence is correct")

        
bitSequence = int(input("Enter the bit sequence(8 digits):\n"))
oddParity(bitSequence)


