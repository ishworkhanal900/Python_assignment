v0 = float(input("Enter starting velocity in meter per sec: "))
v1 = float(input("Enter ending velocity in meter per sec: "))
t = float(input("Enter the span time in sec : "))
avg_acce = (v1-v0)/t
print("the average acceleration is",round(avg_acce,3))
    
