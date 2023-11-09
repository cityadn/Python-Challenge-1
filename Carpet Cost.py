def carpet_cost():
    width = int(input("Width of room?\n"))
    length = int(input("Length of room\n"))
    price = int(input("Price of carpet per m2?\n"))
    area = length * width
    underlay_fee = 3 * area
    carpet_total = price * area
    gripper_fee = (width*2) + (length*2)
    carpet_cost = underlay_fee + gripper_fee + fitting_fee + carpet_total
    print(carpet_cost)

fitting_fee = 50
carpet_cost()


