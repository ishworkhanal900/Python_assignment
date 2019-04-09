import math

r = float(input("Enter the length from the centre of the pentagon to its vertex: "));
s = 2*r* math.sin(math.pi/5)
area = ((3* math.sqrt(3) )/2)* s *s 
print("the area of the pentagon is ", round(area,2))
    
