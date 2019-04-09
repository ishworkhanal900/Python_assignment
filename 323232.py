import random
a = random.randint(0,4)
b = random.randint(0,4)
print(a,"  ",b)
x = int(input("Enter the sum of the numbers above :"))
if x == (a+b):
  print("True")
else:
  print("False")
