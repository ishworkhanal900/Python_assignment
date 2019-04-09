num = int(input("Enter a Number: "))
result = 0

while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)
print("Sum of all digits is: ", result)
