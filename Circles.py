import random

def circle_properties(area, arc_length):
    return area
    return arc_length

p = 3.14

diameter = random.randint(0, 100)
radius = diameter / 2
area = (radius**2) * p
circumferance = diameter * p
arc_angle = random.randint(0, 359)
arc_length = (circumferance * arc_angle) / 360
circle_properties(area, arc_length)
print("radius:", radius)
print("area:", area)
print("circumferance:", circumferance)
print("arc length:", arc_length)




