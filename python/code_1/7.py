#is it a triangle?

angle1 = float(input("Enter the angle 1 : "))
angle2 = float(input("Enter the angle 2 : "))
angle3 = float(input("Enter the angle 3 : "))

if (angle1 + angle2 + angle3) != 180:
    print("This is not a triangle !")
else:
    print("This is a triangle !")