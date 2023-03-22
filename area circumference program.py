import math

d = float(input("What is the diameter of your circle? "))

r = d/2

p = math.pi

a = float(p * (r ** 2))

c = float(2 * 3.1415 * r)

b = str(a)

d = str(c)

print("The circumference is " + d)
print("The area is " + b)
