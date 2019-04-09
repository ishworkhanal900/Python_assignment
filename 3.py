import math
height = float(input('Height of cylinder: '))
radius = float(input('Radius of cylinder: '))
area = radius * radius * math.pi
volume = area * height
print("Area is: ", round(area,2))
print("Volume is: ", round(volume,2))
