def tank_volume():
    length = float(input("Enter the fish tank's length:\n"))
    depth = float(input("Enter it's depth (How deep it goes:\n"))
    height = float(input("Enter it's height:\n"))
    volume = (length * depth * height) / 1000
    print("Fish Tank volume: ", volume)
    
tank_volume()

