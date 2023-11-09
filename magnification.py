real_size = int(input("Enter the measured size of the cell(in cm)\n"))
virtual_size = int(input("Enter the size of a cell (in micrometres)\n"))

def calculation():
    global real_size
    global virtual_size
    global magnification
    magnification = (virtual_size*10000) / real_size
    
    
calculation()
print("magnification = ", magnification, "X")
