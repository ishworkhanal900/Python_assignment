height = float(input("Input your height in inches: "))
weight = float(input("Input your weight in pounds: "))
kg = 0.45359237 * weight
metre = 0.0254 * height
bmi = kg/(metre * metre)
print("Your body mass index is: ", round(bmi, 2))