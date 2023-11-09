def pitVolume(radius, height):
    return pitVolume

def ballVol(ball_radius):
    return ballVol

pi = 3.14
packing_density = 0.75
radius = 1.0
height = 0.2
ball_diameter = 0.05
ball_radius = 0.025

pitVolume = pi * (radius**2) * height
ballVol = (4/3) * pi * (ball_radius**3)

print("The volume of the ball pit:", pitVolume)
print("The volume of a single ball:", ballVol)
ball_amount = pitVolume / (ballVol * packing_density)
print("Number of balls needed to fill pit", int(ball_amount))
