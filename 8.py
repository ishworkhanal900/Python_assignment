import random
a = random.randint(1,101)
b = random.randint(1,101)
print(a,"  ",b)
x = int(input("Enter the sum of the numbers above :"))
if x == (a+b):
  print("True")
else:
  print("False")
